# Stacks of Shapes - Copyright Slashee the Cow 2025-

# Version history
# 1.0.0:    Initial release.

import os
import math
import numpy
import trimesh
from enum import Enum

from UM.Version import Version
from UM.Extension import Extension
from UM.Application import Application
from cura.CuraApplication import CuraApplication

from UM.Mesh.MeshData import MeshData, calculateNormalsFromIndexedVertices
from UM.Resources import Resources
from cura.Scene.CuraSceneNode import CuraSceneNode
from cura.Scene.SliceableObjectDecorator import SliceableObjectDecorator
from cura.Scene.BuildPlateDecorator import BuildPlateDecorator
from UM.Scene.SceneNode import SceneNode
from UM.Operations.AddSceneNodeOperation import AddSceneNodeOperation

from UM.Logger import Logger
from UM.Message import Message

from UM.i18n import i18nCatalog

from PyQt6.QtCore import QObject, pyqtSlot, pyqtSignal, pyqtProperty

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
        transform tools" tip in the shape list window.
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
        """Wrapper for QML to add shape to the scene"""
        # self._registerShapeStl(value, self.getModelPath(value))
        log("d", f"loadModel() run with value = {value}")
        stl_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "models", self.getModelPath(value)))
        log("d", f"loadModel() got stl_file_path = {stl_file_path}")
        self._addShapeStl(value, stl_file_path)

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

    def _addShapeStl(self, mesh_name, mesh_path) -> None:
        
        mesh =  trimesh.load(mesh_path)
        
        self._addShape(mesh_name,self._toMeshData(mesh))

    #----------------------------------------
    # Initial Source code from the awesome fieldOfView - with some amendments by Slashee
    #----------------------------------------  
    def _toMeshData(self, tri_node: trimesh.base.Trimesh, target_size: float = None) -> MeshData:
        """Generate MeshData suitable for adding to a scene node.

        Args:
            tri_node (trimesh.base.Trimesh): Starting mesh (usually done by using trimesh.load() and passing it to this.)
            target_size (float, optional): Manually enter scaled size for meshes to become. Figures out values if None. Defaults to None.

        Returns:
            MeshData: The model correctly scaled, rotated and ready to be added to the scene.
        """
        if target_size is None:
            match self._current_type:
                case ShapeTypes.SHAPE:
                    target_size = self._shape_size
                case ShapeTypes.SYMBOL:
                    target_size = self._symbol_size
                case _:  # This shouldn't happen. But be prepared for anything.
                    target_size = 20

        # How to scale to a target size
        # 1 - Get the bounding box of the model
        bounds_list: list[numpy.ndarray] = tri_node.bounds
        bounds: tuple[numpy.ndarray, numpy.ndarray] = (bounds_list[0], bounds_list[1])
        min_point: numpy.ndarray = bounds[0]
        max_point: numpy.ndarray = bounds[1]

        # 2 - Calculate the dimensions of the bounding box
        dimensions: numpy.ndarray = max_point - min_point

        if self._current_type == ShapeTypes.SHAPE:
            # 3 - Get the size of the largest dimension
            max_bound = numpy.max(dimensions)
            # 4 - Calculate the scaling factor based on the largest dimension and the target size
            if max_bound > 0:  # Make sure we handle a degenerate mesh gracefully
                scale_factor = target_size / max_bound
            else:
                scale_factor = 1
            # 5 - Scale your mesh by that much
            tri_node.apply_scale(scale_factor)
        elif self._current_type == ShapeTypes.SYMBOL:
            # 3 - Get the larger of the X and Y dimeensions
            max_bound_xy = max(dimensions[0], dimensions[1])
            # 4 - Calculate the scaling factor based on the largest dimension and target size
            if max_bound_xy > 0:
                scale_factor_xy = target_size / max_bound_xy
            else:
                scale_factor_xy = 1
            
            # 5 - Get Z size and figure out the scaling factor by that
            if dimensions[2] > 0:
                scale_factor_z = self._symbol_height / dimensions[2]
            else:
                scale_factor_z = 1
            # 6 - Put your scaling factors in a vector-ish
            scale_vector =  [scale_factor_xy, scale_factor_xy, scale_factor_z]
            # 7 - Actually do the scaling already
            tri_node.apply_scale(scale_vector)
        else: # Defensive default case - SHOULD NEVER HAPPEN, but for robustness
            log("w", f"Unexpected shape type in _toMeshData: {self._current_type}. Defaulting to uniform scaling.")
            max_bound = numpy.max(dimensions)
            scale_factor = target_size / max_bound if max_bound > 0 else 1
            tri_node.apply_scale(scale_factor) # Apply uniform scale as fallback


        # Rotate the part to lay down on the build plate
        tri_node.apply_transform(trimesh.transformations.rotation_matrix(math.radians(90), [-1, 0, 0]))
        
        tri_faces = tri_node.faces
        tri_vertices = tri_node.vertices

        # Initial code from fieldOfView
        # https://github.com/fieldOfView/Cura-SimpleShapes/blob/bac9133a2ddfbf1ca6a3c27aca1cfdd26e847221/SimpleShapes.py#L45
        indices = []
        vertices = []

        index_count = 0
        face_count = 0
        for tri_face in tri_faces:
            face = []
            for tri_index in tri_face:
                vertices.append(tri_vertices[tri_index])
                face.append(index_count)
                index_count += 1
            indices.append(face)
            face_count += 1

        vertices = numpy.asarray(vertices, dtype=numpy.float32)
        indices = numpy.asarray(indices, dtype=numpy.int32)
        normals = calculateNormalsFromIndexedVertices(vertices, indices, face_count)

        mesh_data = MeshData(vertices=vertices, indices=indices, normals=normals)

        return mesh_data
        
    # Initial code from fieldOfView
    # https://github.com/fieldOfView/Cura-SimpleShapes/blob/bac9133a2ddfbf1ca6a3c27aca1cfdd26e847221/SimpleShapes.py#L70
    def _addShape(self, mesh_name: str, mesh_data: MeshData, ext_pos = 0) -> None:
        application = CuraApplication.getInstance()

        new_node = CuraSceneNode()

        new_node.setMeshData(mesh_data)
        new_node.setSelectable(True)
        if not mesh_name:
            new_node.setName("Stack shape: " + str(id(mesh_data)))
        else:
            new_node.setName(mesh_name)

        scene = self._controller.getScene()
        op = AddSceneNodeOperation(new_node, scene.getRoot())
        op.push()

        extruder_stack = application.getExtruderManager().getActiveExtruderStacks() 
        
        extruder_nr=len(extruder_stack)
        # Logger.log("d", "extruder_nr= %d", extruder_nr)
        # default_extruder_position  : <class 'str'>
        if ext_pos>0 and ext_pos<=extruder_nr :
            default_extruder_position = int(ext_pos-1)
        else :
            default_extruder_position = int(application.getMachineManager().defaultExtruderPosition)
        # Logger.log("d", "default_extruder_position= %s", type(default_extruder_position))
        default_extruder_id = extruder_stack[default_extruder_position].getId()
        # Logger.log("d", "default_extruder_id= %s", default_extruder_id)
        new_node.callDecoration("setActiveExtruder", default_extruder_id)
 
        # node.setSetting(SceneNodeSettings.AutoDropDown, True)  # I don't even know where this line came from
            
        active_build_plate = application.getMultiBuildPlateModel().activeBuildPlate
        new_node.addDecorator(BuildPlateDecorator(active_build_plate))

        new_node.addDecorator(SliceableObjectDecorator())

        application.getController().getScene().sceneChanged.emit(new_node)
