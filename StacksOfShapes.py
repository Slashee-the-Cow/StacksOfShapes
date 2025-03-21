# Stacks of Shapes copyright Slashee the Cow 2025-

# Version history
# 1.0.0:    Initial release.

import os
import sys
import math
import numpy
import trimesh
from enum import Enum
import time

from UM.Version import Version
from UM.Extension import Extension
from UM.Application import Application
from cura.CuraApplication import CuraApplication

from UM.Mesh.MeshData import MeshData
from UM.Resources import Resources
from cura.Scene.CuraSceneNode import CuraSceneNode
from UM.Scene.SceneNode import SceneNode
from UM.Operations.TranslateOperation import TranslateOperation
from UM.Math.Vector import Vector
from UM.Math.AxisAlignedBox import AxisAlignedBox

from UM.Logger import Logger
from UM.Message import Message

from UM.i18n import i18nCatalog

from PyQt6.QtCore import Qt, QObject, pyqtSlot, pyqtSignal, pyqtProperty, QUrl

from .SymbolsData import *
from .ShapesData import *

class ShapeTypes(Enum):
    SHAPE = "SHAPE"
    SYMBOL = "SYMBOL"

DEBUG_MODE = False

def log(level, message):
    """Wrapper function for logging messages using Cura's Logger, but with debug mode so as not to spam you."""
    if level == "d" and DEBUG_MODE:
        Logger.log("d", message)
    elif level == "i":
        Logger.log("i", message)
    elif level == "w":
        Logger.log("w", message)
    elif level == "e":
        Logger.log("e", message)
    elif level == "c":
        Logger.log("c", message)
    elif DEBUG_MODE:
        Logger.log("w", f"Invalid log level: {level} for message {message}")

# Suggested solution from fieldOfView . in this discussion solved in Cura 4.9
# https://github.com/5axes/Calibration-Shapes/issues/1
# Cura are able to find the scripts from inside the plugin folder if the scripts are into a folder named resources
Resources.addSearchPath(
    os.path.join(os.path.abspath(os.path.dirname(__file__)),'resources')
)  # Plugin translation file import

catalog = i18nCatalog("stacksofshapes")

if catalog.hasTranslationLoaded():
    Logger.log("i", "Stacks of Shapes translation loaded")

#This class is the extension and doubles as QObject to manage the qml    
class StacksOfShapes(QObject, Extension):
    
    AUTO_SLICE_KEY = "general/auto_slice"
    _fixed_version_minimum = Version("5.10")  # Minimum version to check for that contains a fix for a bug which causes a CTD if auto slice is enabled
    _unbroken_version_maximum = Version("5.6")  # Sorry, couldn't think of a better name. Versions this and below are fine, in my testing. So now I can more precisly target my victims.
    _race_condition_version = False  # Stores whether current version is <_fixed_version_minimum so I don't have to keep checking it.
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        # Grab a handle for Cura's preference handler
        self._preferences = CuraApplication.getInstance().getPreferences()
        
        # Add preferences with their defaults
        self._preferences.addPreference("stacksofshapes/shapesize", 20)
        self._preferences.addPreference("stacksofshapes/symbolsize", 50)
        self._preferences.addPreference("stacksofshapes/symbolheight", 5)
        self._preferences.addPreference("stacksofshapes/restore_auto_slice", False)
        self._preferences.addPreference("stacksofshapes/hide_tip", False)

        # Get values from preferences
        self._shape_size = float(self._preferences.getValue("stacksofshapes/shapesize"))  
        self._symbol_size = float(self._preferences.getValue("stacksofshapes/symbolsize"))
        self._symbol_height = float(self._preferences.getValue("stacksofshapes/symbolheight"))
        if bool(self._preferences.getValue("stacksofshapes/restore_auto_slice")):  # For some reason it didn't re-enable it after it last disabled it
            self._preferences.setValue(self.AUTO_SLICE_KEY, True)
            self._preferences.setValue("stacksofshapes/restore_auto_slice", False)
        self._display_tip = not bool(self._preferences.getValue("stacksofshapes/hide_tip"))  # Poor form, I get it.

        # Handle for the QML shape list window.
        self._shape_list_dialog = None
        
        # Absolute path to QML file for shape list window.
        self._shapelist_qml = os.path.abspath(os.path.join(os.path.dirname(__file__), "qml", "StacksOfShapesDialog.qml"))

        self._qml_categories_icon_folder: str = "../categories/"  # Relative path from QML folder to category thumbnails
        self._qml_models_icon_folder:str = "../models/"  # Relative path from QML folder to model files.

        # Set the default to use the Shapes dictionary
        self._current_type_dict = Shapes
        self._category_names = list(Shapes.keys())
        self._shape_names: list = []
        self._current_type = ShapeTypes.SHAPE
        self._current_category: str = ""
        self._current_type_category_thumbnails = Shape_Category_Thumbnail_Filenames
        self._current_type_category_tooltips = Shape_Category_Tooltips

        self._is_file_processing: bool = False
        self._expected_filename: str | None = None
        self._expected_title: str | None = None
        CuraApplication.getInstance().fileCompleted.connect(self._on_file_loaded)
        self._reset_tiny_scaling: bool = False
        self._reset_auto_slice: bool = False
        self._symbol_filenames = self._collect_symbol_filenames()
        self._controller = CuraApplication.getInstance().getController()

        # There's a race condition bug in Cura versions 5.7.0 - 5.9.1 (by my testing) that results in CTDs if simple geometry is loaded while auto slice is on.
        # This is used as a flag to disable auto slicing if running an older version.
        # https://github.com/Ultimaker/Cura/issues/19904
        current_version = Application.getInstance().getVersion().split("-")[0]  # Fix for version comparison not working on the beta + patch build I've been testing with
        self._race_condition_version: bool = current_version < self._fixed_version_minimum and current_version > self._unbroken_version_maximum
        log("i", f"self._race_condition_version = {self._race_condition_version}, reported version = {current_version}")
        log("i", f"current_version < _fixed_version_minimum = {current_version < self._fixed_version_minimum} current_version > _unbroken_version_maximum = {current_version > self._unbroken_version_maximum}")
        
        self.setMenuName(catalog.i18nc("@item:inmenu", "Stacks of Shapes"))
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open Shape List"), self.showShapeListPopup)

    PATH_KEY: str = "path"
    TOOLTIP_KEY: str = "tooltip"
    ALT_TOOLTIP_KEY: str = "altTooltip"

    def _collect_symbol_filenames(self) -> set[str]:
        """Creates a set() of filenames for all symbols to check against when loading models."""
        symbol_filenames = set()
        for category_key in Symbols.keys():
            #log("d", f"_collect_symbol_filenames trying to get keys for category_key {category_key}")
            for symbol_key in Symbols[category_key].keys():
                #log("d", f"_collect_symbol_filenames trying to get data for symbol_key {symbol_key}")
                symbol_data = Symbols[category_key][symbol_key]
                filename = os.path.basename(symbol_data[self.PATH_KEY])
                symbol_filenames.add(filename)
        log("d", f"_collect_symbol_filenames got {symbol_filenames}")
        return symbol_filenames
    
    @pyqtSlot(str, result=str)
    def getCategoryAltTooltip(self, value: str) -> str:
        """Wrapper that gets the alternate tooltip for a category."""
        return self.getCategoryTooltip(value, True)

    @pyqtSlot(str, result=str)
    def getCategoryTooltip(self, value: str, alt: bool = False) -> str:
        """Helper function for the QML windows which gets a tooltip for a category."""
        log("d", f"getCategoryTooltip called. self._current_type = {self._current_type} and value passed to function is {value} and alt is {alt}")
        if alt:
            value += "_alt"
        tooltip_text: str = ""
        log("d", f"getCategoryTooltip trying to get value for key {value}")
        tooltip_text = self._current_type_category_tooltips.get(value)
        log("d", f"getCategoryTooltip got tooltip text {tooltip_text}")
        return tooltip_text

    # Pop up the shape list
    def showShapeListPopup(self) -> None:
        """Destroys shape window if it already exists, then creates a new one
        from scratch regardless of if it's already open.
        """
        if self._shape_list_dialog:
            # Even if it does already exist, we want to start from a fresh slate
            self.destroyShapeList()

        if self._shape_list_dialog is None:
            self._createShapelistPopup()

        self._shape_list_dialog.show()
   
    @pyqtSlot()
    def justDestroyShapeList(self) -> None:
        """Wrapper for destroyShapeList() that can be called from QML."""
        self.destroyShapeList()
    
    def destroyShapeList(self) -> None:
        """Calls destroy() on _shape_list_dialog and sets it to None so it starts from a fresh slate."""
        if self._shape_list_dialog:
            self._shape_list_dialog.destroy()
            self._shape_list_dialog = None
    
    def _createShapelistPopup(self):
        """Actually creates and shows the shape list dialog.
        Run by other functions, shouldn't be called by itself.
        """

        dialog_context = {
            "manager": self,
            "race_version": self._race_condition_version,
        }
        self._shape_list_dialog = CuraApplication.getInstance().createQmlComponent(self._shapelist_qml, dialog_context)
    
    categoryListChanged = pyqtSignal()
    shapeListChanged = pyqtSignal()
    displayTipChanged = pyqtSignal()

    def setDisplayTip(self, value: bool):
        """Setter for if the "use Cura's transform tools" tip in the shape list is visible this session."""
        self._display_tip = value
        self.displayTipChanged.emit()

    @pyqtProperty(bool, notify=displayTipChanged, fset=setDisplayTip)
    def displayTip(self) -> bool:
        """Returns current value whether to display the "You can
        use use Cura's transform tools" tip in the shape list.
        """
        return self._display_tip
    
    @pyqtSlot()
    def disableDisplayTip(self) -> None:
        """Permanently hides the "You can use Cura's
        transform tools" tip in the shape list window
        """
        self._display_tip = False
        self.displayTipChanged.emit()
        self._preferences.setValue("stacksofshapes/hide_tip", True)

    @pyqtProperty(list, notify=categoryListChanged)
    def categoryList(self) -> list[str]:
        """Returns categories for the current Type"""
        return self._category_names
    
    def setShapeList(self, value: str) -> None:
        """This should *NEVER* be called. Use selectCategory() instead.
        It exists only because PyQt doesn't always seem satisfied if shapeList doesn't have a setter.
        """
        raise RuntimeError("Setter for shapeList property was called.\nThis function only exists because PyQt seemingly wouldn't work without it and should never be used.\nUse selectCategory() instead.")

    
    #@pyqtProperty(list, notify=shapeListChanged, fset=setShapeList)
    #def shapeList(self):
    #    return self._shape_names
    @pyqtProperty(list, notify=shapeListChanged, fset=setShapeList)
    def shapeList(self) -> dict:
        """Gets "list" of shapes (actually a dict) to display in right column."""
        shape_list_to_return = self._shape_names
        log("d", f"shapeList property - About to return shape list (length: {len(shape_list_to_return)}):")
        if not shape_list_to_return: # I don't intend to create any empty categories, but you never know.
            log("d", f"shapeList is False when in category {self._current_category}")

        return shape_list_to_return
    
    @pyqtSlot(str)
    def selectCategory(self, category_name: str) -> None:
        """Switches between categories of shapes (the groups on the left).

        Args:
            category_name (str): The category to switch to. Will be ignored if it is the current category.
        """
        if category_name == self._current_category:  # Nothing to do here, don't want to waste time recomposing a ListView
            return
        log("d", f"Current category is {self._current_category} - Trying to access shapes category: {category_name}")
        self.updateShapeList(category_name)

    def updateShapeList(self, category_name: str = "", clear_only: bool = False) -> None:
        """Packs shape name and data (which is a dict) into its own dict for the QML data model"""
        if clear_only:
            log("d", f"updateShapeList called with clear_only")
            self._shape_names = []
            self.shapeListChanged.emit()
            return
        log("d", f"In updateShapeList. Before clearing, self.shapeList = {self.shapeList}")
        self._shape_names = []
        if category_name in self._current_type_dict:
            category_shapes = self._current_type_dict[category_name] # Get the dictionary of shapes for this category
            for shape_name, shape_data in category_shapes.items(): # Iterate through shape names and their data (dictionaries)
                shape_item = { # Create a new dictionary for each shape
                    "shapeName": shape_name, # Store the shape name
                    "shapeData": shape_data  # Store the original shape data dictionary
                }
                self._shape_names.append(shape_item) # Add this dictionary to the list
            self._current_category = category_name
        log("d", f"For {category_name} we got {[item['shapeName'] for item in self._shape_names]}") # Log just the shape names for clarity in logs
        self.shapeListChanged.emit()

    @pyqtSlot(str)
    def selectType(self, type_name: str) -> None:
        """Switches between shape types (currently just shapes and symbols).

        Sets values for the various dictionaries to load content from to references to that particular type.

        Args:
            type_name (str): The type to switch to. Will be a no-op if it doesn't match a name in ShapeTypes enum.
        """
        log("d", f"StackOfShapes.selectType called with {type_name}")
        match type_name:
            case ShapeTypes.SHAPE.value:
                log("d", f"StackOfShapes.selectType matched Shape")
                self._current_type = ShapeTypes.SHAPE
                self._current_type_dict = Shapes
                self._current_type_category_thumbnails = Shape_Category_Thumbnail_Filenames
                self._current_type_category_tooltips = Shape_Category_Tooltips
            case ShapeTypes.SYMBOL.value:
                log("d", f"StackOfShapes.selectType matched Symbol")
                self._current_type = ShapeTypes.SYMBOL
                self._current_type_dict = Symbols
                self._current_type_category_thumbnails = Symbol_Category_Thumbnail_Filenames
                self._current_type_category_tooltips = Symbol_Category_Tooltips
            case _:
                log("w", f"StackOfShapes.selectType matched... nothing?")
                return  # We shouldn't be here.
        self.updateCategoryList()
        self._current_category = ""
        self.updateShapeList(clear_only=True)

    _current_type_changed = pyqtSignal()

    @pyqtProperty(str, notify = _current_type_changed)
    def CurrentType(self) -> str:
        """Getter for current type of models (shapes, symbols)"""
        return self._current_type.value

    def updateCategoryList(self, clear_only: bool = False) -> None:
        """Sets list of current categories for active model type"""
        log("d", f"StackOfShapes.updateCategoryList run. self._current_type = {self._current_type} and self._current_type_dict = {self._current_type_dict}")
        if clear_only:
            log("d", f"updateCategoryList called with clear_only")
            self._category_names = []
            self.categoryListChanged.emit()
            return
        if self._current_type_dict is not None:  # It shouldn't be None. But you never know.
            self._category_names = []  # Shouldn't be necessary when the next one should replace it entirely.
            self._category_names = list(self._current_type_dict.keys())
            self.categoryListChanged.emit()

    
    @pyqtSlot(str)
    def loadModel(self, value: str) -> None:
        # self._registerShapeStl(value, self.getModelPath(value))
        log("d", f"loadModel() run with value = {value}")
        stl_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "models", self.getModelPath(value)))
        log("d", f"loadModel() got stl_file_path = {stl_file_path}")
        self._addShapeLoad(value, stl_file_path)

    def getModelPath(self, model: str) -> str:
        """Gets filename of selected model based on model name."""
        return self._current_type_dict[self._current_category][model].get(self.PATH_KEY)

    @pyqtSlot(str)
    def logMessage(self, value: str) -> None:
        """Wrapper function so QML can log stuff since its own logging doesn't get into Cura's logs."""
        log("d", f"StacksOfShapes QML Log: {value}")

    _shape_size_changed = pyqtSignal()
    
    def SetShapeSize(self, value: int) -> None:
        """Setter for the "Shape size" property"""
        #Logger.log("d", f"Attempting to set ShapeSize from pyqtProperty: {value}")
        self._preferences.setValue("stacksofshapes/shapesize", value)
        self._shape_size = value
        self._shape_size_changed.emit()

    @pyqtProperty(int, notify = _shape_size_changed, fset=SetShapeSize)
    def ShapeSize(self) -> int:
        """Getter for "Shape size" property"""
        #Logger.log("d", f"ShapeSize pyqtProperty accessed: {self._shape_size}, cast to {int(self._shape_size)}")
        return int(self._shape_size)
    
    _symbol_size_changed = pyqtSignal()

    def SetSymbolSize(self, value: int) -> None:
        """Setter for "Symbol size" property"""
        self._preferences.setValue("stacksofshapes/symbolsize", value)
        self._symbol_size = value  # There's an IntValidator on the TextField so it should be alright
        self._symbol_size_changed.emit()

    @pyqtProperty(int, notify = _symbol_size_changed, fset=SetSymbolSize)
    def SymbolSize(self) -> int:
        """Getter for "Symbol size" property"""
        return int(self._symbol_size)
    
    _symbol_height_changed = pyqtSignal()

    def SetSymbolHeight(self, value: float) -> None:
        """Setter for "Symbol height" property"""
        self._preferences.setValue("stacksofshapes/symbolheight", value)
        self._symbol_height = value
        self._symbol_height_changed.emit()

    @pyqtProperty(float, notify = _symbol_height_changed, fset=SetSymbolHeight)
    def SymbolHeight(self) -> float:
        """Getter for "Symbol height" property"""
        return float(self._symbol_height)
    
    @pyqtSlot(str, result=str)
    def getCategoryImage(self, value: str) -> str:
        """Gets the absolute path for a category's thumbnail.

        Builds based on the category's name and combining several paths relative to the root of the plugin.

        Args:
            value (str): The category name to get the thumbnail for.

        Returns:
            str: Absolute path to image file.
        """
        image_path = f"{self._qml_categories_icon_folder}{self._current_type_category_thumbnails.get(value)}"
        abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "qml", image_path))
        log("d", f"getCategoryImage got relative image path: {image_path} which a abspath is {abs_path}")
        if os.path.exists(abs_path):
            return image_path
        else:
            return ""

    @pyqtSlot(str, result=str)
    def getShapeImage(self, value: str) -> str:
        """Gets absolute path for a shape's thumbnail based on model filename.

        Args:
            value (str): File name and relative path for model.

        Returns:
            str: Absolute path to image.
        """
        model_relative_path = f"{self._qml_models_icon_folder}{self.getModelPath(value)}".replace("stl", "webp" if self._current_type != ShapeTypes.SYMBOL else "svg")
        abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "qml", model_relative_path))
        log("d", f"getShapeImage got relative image path {model_relative_path} with an abspath of {abs_path}")
        if os.path.exists(abs_path):
            return model_relative_path
        else:
            return ""
           
    
    
    def _reset_scene_node_scale(self, scene_node: SceneNode) -> None:
        """Resets the scale of a SceneNode to make its current scaling appear as 100% by baking the scaling into the mesh.

        Args:
            scene_node (SceneNode): The node to reset the scale of.
        """
        #transformed_mesh = scene_node.getMeshDataTransformed()
        transformed_mesh = MeshData(vertices = scene_node.getMeshDataTransformedVertices(), normals = scene_node.getMeshDataTransformedNormals(), indices = scene_node.getMeshData().getIndices())
        scene_node.setScale(Vector(1.0,1.0,1.0))
        scene_node.setMeshData(transformed_mesh)


    def _on_file_loaded(self, file_name: str) -> None:
        """Listener invoked on file load to see if it's ours to see if we need to manipulate it."""
        log("d",f"_on_file_loaded saw {file_name}")
        if not self._is_file_processing or os.path.basename(file_name) != self._expected_filename:
            return

        node_to_process = None
        scene = CuraApplication.getInstance().getController().getScene()
        basename = os.path.basename(file_name)
        is_symbol = basename in self._symbol_filenames

        for node in scene.getRoot().getChildren():
            if isinstance(node, CuraSceneNode) and node.getName() == basename:
                node_to_process = node
                log("d", f"Found child node that seems like what we want: {node_to_process}")
                break
        if not node_to_process:
            return  # Extremely unlikely that another load will arrive between our user's click and us checking. But just in case.
        node_to_process.setName(self._expected_title)
        if node_to_process:
            local_transformation_before_scale = node_to_process.getLocalTransformation()
            log("d", f"Local transformation matrix before scaling: {local_transformation_before_scale}")
            # Give it half a sec to catch up in case we're too quick off the mark.
            # Or something. Figure it can't hurt.
            #time.sleep(0.1)
            log("d", f"_on_file_loaded node world position before scaling: {node_to_process.getWorldPosition()}")
            bbox_mesh_data = node_to_process.getBoundingBoxMesh()
            if bbox_mesh_data:
                aabox: AxisAlignedBox = bbox_mesh_data.getExtents()
                if aabox:
                    size_x = aabox.width
                    size_y = aabox.depth
                    size_z = aabox.height
                    #node_to_process.setCenterPosition(Vector(0,-size_z,0))
                    log("d", f"_on_file_loaded got w/d/h of {aabox.width} x {aabox.depth} x {aabox.height}")

                    if is_symbol:
                        max_xy_size = max(size_x, size_y)
                        if max_xy_size > 0:
                            scale_factor_xy = self._symbol_size / max_xy_size
                            scale_factor_z = self._symbol_height / size_z
                            log("d", f"_on_file_loaded scaling symbol by xy {scale_factor_xy} and z {scale_factor_z} for a desired xy of {self.SymbolSize} and z of {self.SymbolHeight}")
                            node_to_process.scale(Vector(scale_factor_xy, scale_factor_z, scale_factor_xy))
                        else:
                            log("w", f"_on_file_loaded tried scaling symbol {basename} but its max_xy_size was <= 0")
                    else:
                        max_size = max(size_x, size_y, size_z)
                        if max_size > 0:
                            scale_factor = self._shape_size / max_size
                            log("d", f"_on_file_loaded scaling shape by {scale_factor}")
                            node_to_process.scale(Vector(scale_factor,scale_factor,scale_factor))
                        else:
                            log("w", f"_on_file_loaded tried scaling shape {basename} but its max size was <= 0")
                    local_transformation_after_scale = node_to_process.getLocalTransformation()     
                    log("d", f"Local transformation matrix after scaling: {local_transformation_after_scale}")
                else:
                    log("w", "_on_file_loaded couldn't get bounding box from MeshData")
            else:
                log("w", "_on_file_load couldn't get bounding box MeshData")

            self._reset_scene_node_scale(node_to_process)
            local_transformation_after_scale = node_to_process.getLocalTransformation()     
            log("d", f"Local transformation matrix after resetting scale to 1: {local_transformation_after_scale}")
            bbox_mesh_data = node_to_process.getBoundingBoxMesh()
            if bbox_mesh_data:
                aabox: AxisAlignedBox = bbox_mesh_data.getExtents()
                if aabox:
                    new_size_x = aabox.width
                    new_size_y = aabox.depth
                    new_size_z = aabox.height
            node_to_process.setCenterPosition(Vector(0,-(new_size_z-size_z)/2,0))
            scene.sceneChanged.emit(node_to_process)
            time.sleep(.2)  # Can take a little bit to recalculate the mesh.
            if is_symbol:
                # Due to how they aren't centred in OpenSCAD, the symbols can start way off course
                # We fix this by forcing them into the centre
                current_position = node_to_process.getPosition()
                log("d", f"file_loaded > is_symbol > going to translate, current position is {current_position}")
                #translation_vector = Vector(-current_position.x, -current_position.y, -current_position.z)
                origin_position = Vector(0,0,0)
                #log("d", f"file_loaded > is_symbol > going to translate, translation vector is {translation_vector}")
                move_op = TranslateOperation(node_to_process, origin_position, set_position=True) # Create TranslateOperation
                move_op.push() # Push the translation operation
                new_position = node_to_process.getPosition()
                log("d", f"file_loaded > is_symbol > has translated, new position is {new_position}")
            else:  # Due to a lack of by-model "drop down model" in older versions of Cura, we make sure everything spawns at Z0.
                current_position = node_to_process.getPosition()
                Logger.log("d", f"file_loaded > is_symbol:else > going to translate, current position is {current_position}, current scale is {node_to_process.getScale()}")
                origin = Vector(0,0,0)
                move_op = TranslateOperation(node_to_process, origin, set_position=True)
                move_op.push()
                new_position = node_to_process.getPosition()
                Logger.log("d", f"file_loaded > is_symbol:else > has translated, new position is {new_position}")
            scene.sceneChanged.emit(node_to_process)
            
        
        if self._reset_tiny_scaling:
            self._preferences.setValue("mesh/scale_tiny_meshes", True)
            self._reset_tiny_scaling = False

        self._is_file_processing = False
        self._expected_filename = None
        self._expected_title = None


    def _addShapeLoad(self, mesh_name: str, stl_file_path: str) -> None:
        """Adds a shape to the scene by Cura's standard "load" function.

        Args:
            mesh_name (str): What the shape should appear as in the object list.
            stl_file_path (str): Path to model file to load.
        """
        log("d", f"addShapeLoad() run with mesh_name = {mesh_name} and stl_file_path = {stl_file_path}")
        application = CuraApplication.getInstance()

        """global_stack = application.getGlobalContainerStack()
        if not global_stack:
            return # Something's wrong with Cura"""
        
        # Some of the models are only a few mm big so we disable automatic scaling
        # so that the user doesn't get an "auto scaled" toast they need to manually dismiss
        if bool(self._preferences.getValue("mesh/scale_tiny_meshes")):
            self._preferences.setValue("mesh/scale_tiny_meshes", False)
            self._reset_tiny_scaling = True
        
        file_url = QUrl.fromLocalFile(stl_file_path)
        self._is_file_processing = True
        self._expected_title = mesh_name
        self._expected_filename = os.path.basename(stl_file_path)
        log("d", f"addShapeLoad() about to run readLocalFile, file_url = {file_url}, _expected_title = {self._expected_title}, _expected_filename = {self._expected_filename}")
        application.readLocalFile(file_url, add_to_recent_files = False)
