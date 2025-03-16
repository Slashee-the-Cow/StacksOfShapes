# Stacks of Shapes copyright Slashee the Cow 2025-

# Version history
# 1.0.0:    Initial release.


import os
import sys
import math
import numpy
import trimesh
from enum import Enum, auto
from pathlib import Path
import time
from threading import Timer
import tempfile

from typing import Optional, List, Any, TYPE_CHECKING

from UM.Version import Version
from UM.Extension import Extension
from UM.Application import Application
from cura.CuraApplication import CuraApplication

from UM.Mesh.MeshData import MeshData, calculateNormalsFromIndexedVertices
from UM.Resources import Resources
from UM.Settings.SettingInstance import SettingInstance
from cura.Scene.CuraSceneNode import CuraSceneNode
from UM.Scene.SceneNode import SceneNode
from UM.Scene.Selection import Selection
from UM.Scene.SceneNodeSettings import SceneNodeSettings
from cura.Scene.SliceableObjectDecorator import SliceableObjectDecorator
from cura.Scene.BuildPlateDecorator import BuildPlateDecorator
from UM.Operations.AddSceneNodeOperation import AddSceneNodeOperation
from UM.Operations.RemoveSceneNodeOperation import RemoveSceneNodeOperation
from UM.Operations.SetTransformOperation import SetTransformOperation
from UM.Operations.TranslateOperation import TranslateOperation
from UM.Math.Vector import Vector
from UM.Math.AxisAlignedBox import AxisAlignedBox

from UM.Logger import Logger
from UM.Message import Message

from UM.i18n import i18nCatalog

from PyQt6.QtCore import Qt, QObject, pyqtSlot, pyqtSignal, pyqtProperty, QMetaType, QUrl

from .SymbolsData import *
from .ShapesData import *

class ShapeTypes(Enum):
    SHAPE = "SHAPE"
    SYMBOL = "SYMBOL"

DEBUG_MODE = True

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
    _fixed_version_minimum = Version("5.10")  # Workaround for a race condition fixed in 5.10 (hopefully) that causes instant CTD on loading simple objects
    _race_condition_version = False
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        # set the preferences to store the default value
        self._preferences = CuraApplication.getInstance().getPreferences()
        
        # Add preferences with their default if we don't already have them
        self._preferences.addPreference("stacksofshapes/shapesize", 20)
        self._preferences.addPreference("stacksofshapes/symbolsize", 50)
        self._preferences.addPreference("stacksofshapes/symbolheight", 5)
        self._preferences.addPreference("stacksofshapes/restore_auto_slice", False)

        # Get values from preferences
        self._shape_size = float(self._preferences.getValue("stacksofshapes/shapesize"))  
        self._symbol_size = float(self._preferences.getValue("stacksofshapes/symbolsize"))
        self._symbol_height = float(self._preferences.getValue("stacksofshapes/symbolheight"))
        if bool(self._preferences.getValue("stacksofshapes/restore_auto_slice")):
            self._preferences.setValue(self.AUTO_SLICE_KEY, True)
            self._preferences.setValue("stacksofshapes/restore_auto_slice", False)

        self._shape_list_dialog = None
        
        self._shapelist_qml = os.path.abspath(os.path.join(os.path.dirname(__file__), "qml", "StacksOfShapesDialog.qml"))

        self._qml_categories_icon_folder: str = "../categories/"  # Relative path from QML folder to category thumbnails
        self._qml_models_icon_folder:str = "../models/"  # Relative path from QML folder to model files.
        # self._settings_qml = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qml", "settings.qml")
        #self._settings_qml = os.path.abspath(os.path.join(os.path.dirname(__file__), "qml", "settings.qml"))

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

        # There's a race condition bug in Cura versions < 5.10 that results in CTDs if simple geometry is loaded while auto slice is on.
        # This is used as a flag to disable auto slicing if running an older version.
        # https://github.com/Ultimaker/Cura/issues/19904
        self._race_condition_version: bool = Version(Application.getInstance().getVersion()) < self._fixed_version_minimum
        log("d", f"self._race_condition_version = {self._race_condition_version}")
        """self._original_auto_slice_value: bool | None = None
        self._race_condition_workaround_active: bool  = False
        self._preferences_listener_exists: bool = False
        #self.selectCategory("Basics")"""
        #log("i", f"cura_version = {Application.getInstance().getVersion()} and == Version(5.9) is {Application.getInstance().getVersion() == Version(5.9)} and \"5.9.0\" < Version(5.10) is {'5.9.0' < Version(5.10)}")
        
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
        """Wrapper that gets the 'alternate' tooltip for a category."""
        return self.getCategoryTooltip(value, True)

    @pyqtSlot(str, result=str)
    def getCategoryTooltip(self, value: str, alt: bool = False) -> str:
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
        from scratch regardless of if it's already open."""
        if self._shape_list_dialog:
            # Even if it does already exist, we want to start from a fresh slate
            self.destroyShapeList()

        if self._shape_list_dialog is None:
            self._createShapelistPopup()

        """if self._race_condition_version:
            self._race_condition_workaround_active = True
            if self._original_auto_slice_value is None:
                if bool(self._preferences.getValue(self.AUTO_SLICE_KEY)):
                    self._original_auto_slice_value = True
                    self._preferences.setValue("stacksofshapes/restore_auto_slice", True)
                    self._preferences.setValue(self.AUTO_SLICE_KEY, False)
            if not self._preferences_listener_exists:
                self._preferences.preferenceChanged.connect(self._`preference_l`istener)
                self._preferences_listener_exists = True
            if self._shape_list_dialog:
                self._shape_list_dialog.closing.connect(self.destroyShapeList)"""

        self._shape_list_dialog.show()

    """race_condition_workaround_change = pyqtSignal()

    @pyqtProperty(bool, notify=race_condition_workaround_change)
    def is_workaround_active(self):
        return self._race_condition_workaround_active"""
    
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
        Run by other functions, shouldn't be called by itself."""
        #qml_file_path = os.path.join(os.path.dirname(__file__), "qml", "settings.qml")
        dialog_context = {
            "manager": self,
            "race_version": self._race_condition_version,
        }
        self._shape_list_dialog = CuraApplication.getInstance().createQmlComponent(self._shapelist_qml, dialog_context)
    
    categoryListChanged = pyqtSignal()
    shapeListChanged = pyqtSignal()

    @pyqtProperty(list, notify=categoryListChanged)
    def categoryList(self) -> list[str]:
        return self._category_names
    
    def setShapeList(self, value: str) -> None:
        """This should *NEVER* be called. Use selectCategory() instead.
        It exists only because PyQt doesn't always seem satisfied if a property doesn't have a setter."""
        log("e", ">>>>>>>>>>>>> setShapeList setter FUNCTION WAS CALLED! <<<<<<<<<<<<<<<<<<")
        log("d", f"setShapeList: category_name argument passed = {value}")
        self.updateShapeList(value)
        log("d", f"setShapeList: after updateShapeList, self._shape_names = {self._shape_names} and self.shapeList = {self.shapeList}")

    
    #@pyqtProperty(list, notify=shapeListChanged, fset=setShapeList)
    #def shapeList(self):
    #    return self._shape_names
    @pyqtProperty(list, notify=shapeListChanged, fset=setShapeList)
    def shapeList(self) -> dict:
        shape_list_to_return = self._shape_names
        log("d", f"shapeList property - About to return shape list (length: {len(shape_list_to_return)}):")
        if not shape_list_to_return: # Handle empty list case
            log("d", f"  Shape list is empty.")
        else:
            for index, shape_item in enumerate(shape_list_to_return):
                log("d", f"  Item index {index}:")
                log("d", f"    Type of item: {type(shape_item)}") # Log type of the item itself
                log("d", f"    Representation (repr) of item: {repr(shape_item)}") # Log full representation - very detailed
                if isinstance(shape_item, dict): # If it's a dictionary, log its keys and value types
                    log("d", f"    Dictionary Keys and Value Types:")
                    for key, value in shape_item.items():
                        log("d", f"      Key: '{key}' (Type: {type(key)}), Value Type: {type(value)}, Value (repr): {repr(value)}")
                else: # If it's NOT a dictionary (unexpected), log warning
                    log("w", f"    WARNING: Item is NOT a dictionary! Type: {type(shape_item)}, Value (repr): {repr(shape_item)}")

        return shape_list_to_return
    
    @pyqtSlot(str)
    def selectCategory(self, category_name: str) -> None:
        """
        Switches between categories of shapes (the groups on the left).

        Args:
            category_name (str): The category to switch to. Will be ignored if it is the current category.
        """
        if category_name == self._current_category:  # Nothing to do here, don't want to waste time recomposing a ListView
            return
        log("d", f"Current category is {self._current_category} - Trying to access shapes category: {category_name}")
        self.updateShapeList(category_name)

    """def updateShapeList(self, category_name = "", clear_only: bool = False):
        if clear_only:
            log("d", f"updateShapeList called with clear_only")
            self._shape_names = []
            self.shapeListChanged.emit()
            return
        #log("d", f"In updateShapeList. Before clearing, self.shapeList = {self.shapeList}")
        self._shape_names = []
        if category_name in self._current_type_dict:
            self._shape_names = self._current_type_dict.get(category_name)
            log("d", f"updateShapeList: self._shape_names = {self._shape_names} which is type {type(self._shape_names)}")
            self._current_category = category_name
        #log("d", f"For {category_name} we got {self._shape_names}")
        self.shapeListChanged.emit()"""

    def updateShapeList(self, category_name = "", clear_only: bool = False) -> None:
        if clear_only:
            log("d", f"updateShapeList called with clear_only")
            self._shape_names = []
            self.shapeListChanged.emit()
            return
        log("d", f"In updateShapeList. Before clearing, self.shapeList = {self.shapeList}")
        self._shape_names = [] # Clear the old list (but now it will hold DICTS, not strings)
        if category_name in self._current_type_dict: # e.g., self._current_type_dict is self.Shapes
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
        """
        Switches between shape types (currently just shapes and symbols).

        Args:
            type_name (str): The type to switch to. Will be a no-op if it doesn't match a name.
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
        return self._current_type.value

    def updateCategoryList(self, clear_only: bool = False) -> None:
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
        #self._expected_title = value
        self._addShapeLoad(value, stl_file_path)

    def getModelPath(self, model: str) -> str:
        """Gets filename of selected model based on model name."""
        return self._current_type_dict[self._current_category][model].get(self.PATH_KEY)

    """def loadModel(self, shape_name):
    # ... (path logic and mesh loading from above) ...

    if not mesh: # Check if mesh loading was successful
        return

    try:
        scene = Application.getInstance().getController().getScene() # Get the scene
        if scene:
            mesh_instance = MeshInstance(mesh) # Create a MeshInstance from the loaded mesh
            scene.getRoot().addChild(mesh_instance) # Add MeshInstance to the scene root
            self.logMessage(f"Added shape '{shape_name}' to the scene.")
        else:
            self.logMessage("Error: Scene not available.")
    except Exception as e:
        self.logMessage(f"Exception during scene addition: {e}")"""

    @pyqtSlot(str)
    def logMessage(self, value: str) -> None:
        """Wrapper function so QML can log stuff since its own logging doesn't get into Cura's logs."""
        log("d", f"StacksOfShapes QML Log: {value}")

    _shape_size_changed = pyqtSignal()
    
    def SetShapeSize(self, value: int) -> None:
        #Logger.log("d", f"Attempting to set ShapeSize from pyqtProperty: {value}")
        self._preferences.setValue("stacksofshapes/shapesize", value)
        self._shape_size = value
        self._shape_size_changed.emit()

    @pyqtProperty(int, notify = _shape_size_changed, fset=SetShapeSize)
    def ShapeSize(self) -> int:
        #Logger.log("d", f"ShapeSize pyqtProperty accessed: {self._shape_size}, cast to {int(self._shape_size)}")
        return int(self._shape_size)
    
    _symbol_size_changed = pyqtSignal()

    def SetSymbolSize(self, value: int) -> None:
        self._preferences.setValue("stacksofshapes/symbolsize", value)
        self._symbol_size = value  # There's an IntValidator on the TextField so it should be alright
        self._symbol_size_changed.emit()

    @pyqtProperty(int, notify = _symbol_size_changed, fset=SetSymbolSize)
    def SymbolSize(self) -> int:
        return int(self._symbol_size)
    
    _symbol_height_changed = pyqtSignal()

    def SetSymbolHeight(self, value: float) -> None:
        self._preferences.setValue("stacksofshapes/symbolheight", value)
        self._symbol_height = value
        self._symbol_height_changed.emit()

    @pyqtProperty(float, notify = _symbol_height_changed, fset=SetSymbolHeight)
    def SymbolHeight(self) -> float:
        return float(self._symbol_height)
    
    @pyqtSlot(str, result=str)
    def getCategoryImage(self, value: str) -> str:
        image_path = f"{self._qml_categories_icon_folder}{self._current_type_category_thumbnails.get(value)}"
        abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "qml", image_path))
        log("d", f"getCategoryImage got relative image path: {image_path} which a abspath is {abs_path}")
        if os.path.exists(abs_path):
            return image_path
        else:
            return ""

    @pyqtSlot(str, result=str)
    def getShapeImage(self, value: str) -> str:
        model_relative_path = f"{self._qml_models_icon_folder}{self.getModelPath(value)}".replace("stl", "webp" if self._current_type != ShapeTypes.SYMBOL else "svg")
        abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "qml", model_relative_path))
        log("d", f"getShapeImage got relative image path {model_relative_path} with an abspath of {abs_path}")
        if os.path.exists(abs_path):
            return model_relative_path
        else:
            return ""
           
    """def _registerShapeStl(self, mesh_name, mesh_filename=None, **kwargs) -> None:
        if mesh_filename is None:
            mesh_filename = mesh_name + ".stl"
        
        model_definition_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models", mesh_filename)
        log("d", f"_registerShapeStl going to load {model_definition_path}")
        log("d", f"self._shape_size = {self._shape_size}")
        #mesh =  trimesh.load(model_definition_path)
        
        # addShape
        #self._addShapeSimple(mesh_name,self._toMeshData(mesh), 2000)

    #----------------------------------------
    # Initial Source code from the awesome fieldOfView - with some amendments by Slashee
    #----------------------------------------  
    def _toMeshData(self, tri_node: trimesh.base.Trimesh, target_size: float = None) -> MeshData:
        if target_size is None:
            match self._current_type:
                case ShapeTypes.SHAPE:
                    target_size = self._shape_size
                case ShapeTypes.SYMBOL:
                    target_size = self._symbol_size
                case _:  # This shouldn't happen. But be prepared for anything.
                    target_size = 20

        # How to scale to a target size: the Slashee contribution
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
            max_bound_xy = max(dimensions[0], dimensions[1])
            if max_bound_xy > 0:
                scale_factor_xy = target_size / max_bound_xy
            else:
                scale_factor_xy = 1
            
            if dimensions[2] > 0:
                scale_factor_z = self._symbol_height / dimensions[2]
            else:
                scale_factor_z = 1
            
            scale_vector =  [scale_factor_xy, scale_factor_xy, scale_factor_z]
            tri_node.apply_scale(scale_vector)
        else: # Defensive default case - SHOULD NEVER HAPPEN, but for robustness
            log("w", f"Unexpected shape type in _toMeshData: {self._current_type}. Defaulting to uniform scaling.")
            max_bound = numpy.max(dimensions)
            scale_factor = target_size / max_bound if max_bound > 0 else 1
            tri_node.apply_scale(scale_factor) # Apply uniform scale as fallback


        # Rotate the part to laydown on the build plate
        # Modification from 5@xes
        tri_node.apply_transform(trimesh.transformations.rotation_matrix(math.radians(90), [-1, 0, 0]))
        tri_faces = tri_node.faces
        tri_vertices = tri_node.vertices

        # Following Source code from  fieldOfView
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
    
    _reset_timer = Timer
    
    # Initial Source code from  fieldOfView
    # https://github.com/fieldOfView/Cura-SimpleShapes/blob/bac9133a2ddfbf1ca6a3c27aca1cfdd26e847221/SimpleShapes.py#L70
    def _addShape(self, mesh_name, mesh_data: MeshData, ext_pos = 0) -> None:
        application = CuraApplication.getInstance()
        global_stack = application.getGlobalContainerStack()
        if not global_stack:
            return

        node = CuraSceneNode()

        node.setMeshData(mesh_data)
        node.setSelectable(True)
        if len(mesh_name)==0:
            node.setName("TestPart" + str(id(mesh_data)))
        else:
            node.setName(str(mesh_name))

        scene = self._controller.getScene()
        op = AddSceneNodeOperation(node, scene.getRoot())
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
        node.callDecoration("setActiveExtruder", default_extruder_id)
 
        # node.setSetting(SceneNodeSettings.AutoDropDown, True)  # I don't even know where this line came from
            
        active_build_plate = application.getMultiBuildPlateModel().activeBuildPlate
        node.addDecorator(BuildPlateDecorator(active_build_plate))

        node.addDecorator(SliceableObjectDecorator())

        application.getController().getScene().sceneChanged.emit(node)
        """
    
    """def _addShapeSimple(self, mesh_name: str, mesh_data: MeshData, add_delay_ms: float = 0) -> None: # Corrected signature with 'self'
        """"""
        Adds a shape to the Cura scene with minimal essential functionality, primarily for
        race condition testing.  Version 3 - Minimal but (hopefully) functional.

        :param mesh_name: Name to give to the scene node.
        :param mesh_data: MeshData object representing the shape.
        :param add_delay_ms:  Optional delay in milliseconds.
        """"""
        application = CuraApplication.getInstance()
        #global_stack = application.getGlobalContainerStack()
        #if not global_stack:
        #    return
        original_auto_slice_value = bool(self._preferences.getValue("general/auto_slice"))
        if original_auto_slice_value == True:
            self._preferences.setValue("general/auto_slice", False)
        log("d", f"preference general/auto_slice was {original_auto_slice_value}")

        node = CuraSceneNode()

        node.setMeshData(mesh_data)
        node.setSelectable(True)
        node.setName(mesh_name if mesh_name else "StackShape")

        scene = self._controller.getScene()
        op = AddSceneNodeOperation(node, scene.getRoot())
        op.push()

        extruder_stack = application.getExtruderManager().getActiveExtruderStacks() 
        default_extruder_position = int(application.getMachineManager().defaultExtruderPosition)
        default_extruder_id = extruder_stack[default_extruder_position].getId()
        node.callDecoration("setActiveExtruder", default_extruder_id)

        active_build_plate = application.getMultiBuildPlateModel().activeBuildPlate
        node.addDecorator(BuildPlateDecorator(active_build_plate))
        
        node.addDecorator(SliceableObjectDecorator())
                
        application.getController().getScene().sceneChanged.emit(node)

        if original_auto_slice_value == True:
            self._reset_timer = Timer(add_delay_ms/1000, self.resetAutoSlice, [original_auto_slice_value, node], {})
            self._reset_timer.start()
        return
    
    def resetAutoSlice(self, value: bool, node: CuraSceneNode) -> None:
        # Jiggle the node using TranslateOperation
        translation_vector = Vector(0.01, 0, 0) # Tiny translation in X direction (0.01mm)
        translate_op = TranslateOperation(node, translation_vector) # Create TranslateOperation
        translate_op.push() # Push the translation operation
        translation_vector = Vector(-0.01, 0, 0) # Tiny translation in X direction (0.01mm)
        translate_op = TranslateOperation(node, translation_vector) # Create TranslateOperation
        translate_op.push() # Push the translation operation
        # Give Cura a bit of time to catch up
        time.sleep(0.02)
        log("d", f"resetAutoSlice run with a value of {value}")
        self._preferences.setValue("general/auto_slice", value)
        time.sleep(0.02)
        translation_vector = Vector(0.01, 0, 0) # Tiny translation in X direction (0.01mm)
        translate_op = TranslateOperation(node, translation_vector) # Create TranslateOperation
        translate_op.push() # Push the translation operation
        translation_vector = Vector(-0.01, 0, 0) # Tiny translation in X direction (0.01mm)
        translate_op = TranslateOperation(node, translation_vector) # Create TranslateOperation
        translate_op.push() # Push the translation operation"""
    
    def _reset_scene_node_scale(self, scene_node: SceneNode) -> None:
        """
        Resets the scale of a SceneNode to make its current scaling appear as 100% by baking the scaling into the mesh.

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
            # Give it half a sec to catch up in case we're too quick off the mark.
            # Or something. Figure it can't hurt.
            time.sleep(0.1)
            bbox_mesh_data = node_to_process.getBoundingBoxMesh()
            if bbox_mesh_data:
                aabox: AxisAlignedBox = bbox_mesh_data.getExtents()
                if aabox:
                    size_x = aabox.width
                    size_y = aabox.depth
                    size_z = aabox.height
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
                else:
                    log("w", "_on_file_loaded couldn't get bounding box from MeshData")
            else:
                log("w", "_on_file_load couldn't get bounding box MeshData")

            self._reset_scene_node_scale(node_to_process)

        
            if is_symbol:
                # Due to how they aren't centred in OpenSCAD, the symbols can start way off course
                # We fix this by forcing them into the centre
                current_position = node_to_process.getPosition()
                translation_vector = Vector(-current_position.x, -current_position.y, -current_position.z)
                translate_op = TranslateOperation(node, translation_vector) # Create TranslateOperation
                translate_op.push() # Push the translation operation
            else:  # Due to a lack of by-model "drop down model" in older versions of Cura, we make sure everything spawns at Z0.
                current_position = node_to_process.getPosition()
                translation_vector = Vector(0,0, -current_position.z)
                translate_op = TranslateOperation(node, translation_vector) # Create TranslateOperation
                translate_op.push() # Push the translation operation
        
        if self._reset_tiny_scaling:
            self._preferences.setValue("mesh/scale_tiny_meshes", True)
            self._reset_tiny_scaling = False

        """if self._reset_auto_slice:
            self._reenable_auto_slice = Timer(5, self._enable_auto_slice)
            self._reenable_auto_slice.start()
        if self._reset_tiny_scaling:
            self._reenable_scale_tiny = Timer(1,self._enable_scale_tiny)
            self._reenable_scale_tiny.start()"""

        self._is_file_processing = False
        self._expected_filename = None
        self._expected_title = None

    """_reenable_auto_slice: Timer | None = None

    def _enable_auto_slice(self) -> None:
        self._preferences.setValue("general/auto_slice", True)
        self._reset_auto_slice = False"""

    def _addShapeLoad(self, mesh_name: str, stl_file_path: str) -> None:
        log("d", f"addShapeLoad() run with mesh_name = {mesh_name} and stl_file_path = {stl_file_path}")
        application = CuraApplication.getInstance()

        global_stack = application.getGlobalContainerStack()
        if not global_stack:
            return # Something's wrong with Cura
        
        # Some of the models are only a few mm big so we disable automatic scaling
        # so that the user doesn't get an "auto scaled" toast they need to manually dismiss
        if bool(self._preferences.getValue("mesh/scale_tiny_meshes")):
            self._preferences.setValue("mesh/scale_tiny_meshes", False)
            self._reset_tiny_scaling = True
        """if bool(self._preferences.getValue("general/auto_slice")):
            self._preferences.setValue("general/auto_slice", False)
            self._reset_auto_slice = True
            if not self._reenable_auto_slice:
                self._reenable_auto_slice = Timer(3, self._enable_auto_slice)
                self._reenable_auto_slice.start()
            else:
                self._reenable_auto_slice.cancel()
                time.sleep(0.02)
                self._reenable_auto_slice.start()"""

        
        file_url = QUrl.fromLocalFile(stl_file_path)
        self._is_file_processing = True
        self._expected_title = mesh_name
        self._expected_filename = os.path.basename(stl_file_path)
        log("d", f"addShapeLoad() about to run readLocalFile, file_url = {file_url}, _expected_title = {self._expected_title}, _expected_filename = {self._expected_filename}")
        application.readLocalFile(file_url, add_to_recent_files = False)
