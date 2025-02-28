# Part of initial code by fieldOfView 2018
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

from typing import Optional, List, Any, TYPE_CHECKING

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

from UM.Logger import Logger
from UM.Message import Message

from UM.i18n import i18nCatalog


from PyQt6.QtCore import Qt, QObject, pyqtSlot, pyqtSignal, pyqtProperty, QMetaType

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
    
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        # set the preferences to store the default value
        self._preferences = CuraApplication.getInstance().getPreferences()
        
        # Add preferences with their default if we don't already have them
        self._preferences.addPreference("stacksofshapes/shapesize", 20)
        self._preferences.addPreference("stacksofshapes/symbolsize", 50)
        self._preferences.addPreference("stacksofshapes/symbolheight", 5)

        # Get values from preferences
        self._shape_size = float(self._preferences.getValue("stacksofshapes/shapesize"))  
        self._symbol_size = float(self._preferences.getValue("stacksofshapes/symbolsize"))
        self._symbol_height = float(self._preferences.getValue("stacksofshapes/symbolheight"))

        self._shape_list_dialog = None
        
        self._shapelist_qml = os.path.abspath(os.path.join(os.path.dirname(__file__), "qml", "StacksOfShapesDialog.qml"))

        self._qml_categories_icon_folder = "../categories/"
        self._qml_models_icon_folder = "../models/"
        # self._settings_qml = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qml", "settings.qml")
        #self._settings_qml = os.path.abspath(os.path.join(os.path.dirname(__file__), "qml", "settings.qml"))

        # Set the default to use the Shapes dictionary
        self._current_type_dict = self.Shapes
        self._category_names = list(self.Shapes.keys())
        self._shape_names: list = []
        self._current_type = ShapeTypes.SHAPE
        self._current_category: str = ""
        
        self._controller = CuraApplication.getInstance().getController()

        #self.selectCategory("Basics")
        
        self.setMenuName(catalog.i18nc("@item:inmenu", "Stacks of Shapes"))
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Open Shape List"), self.showShapelistPopup)

    _shape_category_basics: str = catalog.i18nc("shape_category", "Basics")
    _shape_category_spherical: str = catalog.i18nc("shape_category", "Spherical")
    _shape_category_prisms: str = catalog.i18nc("shape_category", "Prisms")
    _shape_category_pyramids: str = catalog.i18nc("shape_category", "Pyramids")
    _shape_category_platonics: str = catalog.i18nc("shape_category", "Platonic Solids")
    _shape_category_tetrominoes: str = catalog.i18nc("shape_category", "Tetrominoes")

    PATH_KEY: str = "path"
    TOOLTIP_KEY: str = "tooltip"

    Shapes = {
        _shape_category_basics: {
            catalog.i18nc("shape_name", "Cube"): {
                PATH_KEY: "platonics/hexahedron.stl",
                TOOLTIP_KEY: "The corners are sharp. Don't poke your eyes out.",
            },
            catalog.i18nc("shape_name", "Sphere"): {
                PATH_KEY: "spherical/sphere.stl",
                TOOLTIP_KEY: "This one has zero corners. Your eyes are safe.",
            },
        },
        _shape_category_spherical: {
            catalog.i18nc("shape_name", "Sphere"): {
                PATH_KEY: "spherical/sphere.stl",
                TOOLTIP_KEY: "",
            },
            catalog.i18nc("shape_name", "Three Quarter Spherical Sector"): {
                PATH_KEY: "spherical/three_quarter_spherical_sector.png",
                TOOLTIP_KEY: "",
            },
            catalog.i18nc("shape_name", "Hemisphere"): {
                PATH_KEY: "spherical/hemisphere.stl",
                TOOLTIP_KEY: "",
            },
            catalog.i18nc("shape_name", "Spherical Quadrant"): {
                PATH_KEY: "spherical/spherical_quadrant.stl",
                TOOLTIP_KEY: "",
            },
            catalog.i18nc("shape_name", "Spherical Octant"): {
                PATH_KEY: "spherical/spherical_octant.stl",
                TOOLTIP_KEY: "",
            },
            catalog.i18nc("shape_name", "Spherical Octant (Corner)"):{
                PATH_KEY: "spherical/spherical_octant_corner.stl",
                TOOLTIP_KEY: "",
            },
        },
        _shape_category_prisms: {
            catalog.i18nc("shape_name", "Rectangular Prism"): {
                PATH_KEY: "prisms/prism_rectangular.stl",
                TOOLTIP_KEY: "",
            },
            catalog.i18nc("shape_name", "Hexagonal Prism"): {
                PATH_KEY: "prisms/prism_hexagonal.stl",
                TOOLTIP_KEY: "",
            },
            catalog.i18nc("shape_name", "Octangonal Prism"): {
                PATH_KEY: "prisms/prism_octagonal.stl",
                TOOLTIP_KEY: ""
            },
            catalog.i18nc("shape_name", "Triangular Prism (Equilateral)"): {
                PATH_KEY: "prisms/prism_triangular_equilateral.stl",
                TOOLTIP_KEY: "",
            },
            catalog.i18nc("shape_name", "Triangular Prism (Right)"): {
                PATH_KEY: "prisms/prism_triangular_right.stl",
                TOOLTIP_KEY: ""
            },
            catalog.i18nc("shape_name", "Trapezium Prism"): {
                PATH_KEY: "prisms/prism_trapezium.stl",
                TOOLTIP_KEY: ""
            },
            catalog.i18nc("shape_name", "Rhombic Prism"): {
                PATH_KEY: "prisms/prism_rhombic.stl",
                TOOLTIP_KEY: ""
            },
            catalog.i18nc("shape_name", "Parallelogram Prism"): {
                PATH_KEY: "prisms/prism_parallelogram.stl",
                TOOLTIP_KEY: ""
            }
        },
        _shape_category_pyramids: {
            catalog.i18nc("shape_name", "Triangular Pyramid (3 sides)"): {
                PATH_KEY: "platonics/tetrahedron.stl",
                TOOLTIP_KEY: "",
            },
            catalog.i18nc("shape_name", "Square Pyramid (4 sides)"): {
                PATH_KEY: "pyramids/pyramid_square.stl",
                TOOLTIP_KEY: "",
            },
            catalog.i18nc("shape_name", "Pentagonal Pyramid (5 sides)"): {
                PATH_KEY: "pyramids/pyramid_pentagon.stl",
                TOOLTIP_KEY: "",
            },
            catalog.i18nc("shape_name", "Hexagonal Pyramid (6 sides)"): {
                PATH_KEY: "pyramids/pyramid_hexagon.stl",
                TOOLTIP_KEY: ""
            },
            catalog.i18nc("shape_name", "Octagonal Pyramid (8 sides)"): {
                PATH_KEY: "pyramids/pyramid_octagon.stl",
                TOOLTIP_KEY: "",
            }
        },
        _shape_category_platonics: {
            catalog.i18nc("shape_name", "Tetrahedron (4 sides)"): {
                PATH_KEY: "platonics/tetrahedron.stl",
                TOOLTIP_KEY: "",
            },
            catalog.i18nc("shape_name", "Hexahedron (6 sides)"): {
                PATH_KEY: "platonics/hexahedron.stl",
                TOOLTIP_KEY: catalog.i18nc("shape_tooltip_platonic", "Technically the term is *regular* hexahedron.\nBut I've gotten nerdy enough already."),
            },
            catalog.i18nc("shape_name", "Octahedron (8 sides)"): {
                PATH_KEY: "platonics/octahedron.stl",
                TOOLTIP_KEY: "",
            },
            catalog.i18nc("shape_name", "Dodecahedron (12 sides)"): {
                PATH_KEY: "platonics/dodecahedron.stl",
                TOOLTIP_KEY: "",
            },
            catalog.i18nc("shape_name", "Icosahedron (20 sides)"): {
                PATH_KEY: "platonics/icosahedron.stl",
                TOOLTIP_KEY: "",
            }
        },
        _shape_category_tetrominoes: {
            catalog.i18nc("shape_name", "J"): {
                PATH_KEY: "tetrominoes/tetromino_j.stl",
                TOOLTIP_KEY: "",
            },
            catalog.i18nc("shape_name", "L"): {
                PATH_KEY: "tetrominoes/tetromino_l.stl",
                TOOLTIP_KEY: "",
            },
            catalog.i18nc("shape_name", "S"): {
                PATH_KEY: "tetrominoes/tetromino_s.stl",
                TOOLTIP_KEY: "",
            },
            catalog.i18nc("shape_name", "T"): {
                PATH_KEY: "tetrominoes/tetromino_t.stl",
                TOOLTIP_KEY: "",
            },
            catalog.i18nc("shape_name", "Z"): {
                PATH_KEY: "tetrominoes/tetromino_z.stl",
                TOOLTIP_KEY: ""
            },
            catalog.i18nc("shape_name", "Square"): {
                PATH_KEY: "tetrominoes/tetromino_square.stl",
                TOOLTIP_KEY: "Also known as the \"O\""
            },
            catalog.i18nc("shape_name", "Straight"): {
                PATH_KEY: "tetrominoes/tetromino_straight.stl",
                TOOLTIP_KEY: "Also known as the \"I\""
            }
        }
    }

    Shape_Category_Tooltips = {
        _shape_category_basics: "",
        _shape_category_spherical: "Spheres. And parts of them. Keep your \"ball\" jokes to yourself.",
        _shape_category_prisms: "",
        _shape_category_pyramids: "",
        _shape_category_platonics: "3D objects where all faces and angles are exactly the same.\nOften used as dice.",
        _shape_category_tetrominoes: "The different shapes possible when combining four cubes."
    }

    _symbols_category_arrows = catalog.i18nc("symbol_category", "Arrows")
    _symbols_category_hearts = catalog.i18nc("symbol_category", "Hearts")

    Symbols = {
        _symbols_category_arrows: {
            catalog.i18nc("symbol_name", "Straight Arrow"): {
                PATH_KEY: "2d/arrows/arrow_single.stl",
                TOOLTIP_KEY: "",
            },
        },
        _symbols_category_hearts: {
            catalog.i18nc("symbol_name", "Heart"): {
                PATH_KEY: "2d/hearts/heart.stl",
                TOOLTIP_KEY: "Not anatomically correct.",
            },
        }
    }

    Symbol_Category_Tooltips = {
        _symbols_category_arrows: catalog.i18nc("category_tooltip", "They point at things.\nRotate or mirror them and they can point at other things."),
        _symbols_category_hearts: ""
    }

    @pyqtSlot(str, result=str)
    def getCategoryTooltip(self, value):
        log("d", f"getCategoryTooltip called. self._current_type = {self._current_type} and value passed to function is {value}")
        tooltip_text: str = ""
        match self._current_type:
            case ShapeTypes.SHAPE:
                tooltip_text = self.Shape_Category_Tooltips.get(value)
            case ShapeTypes.SYMBOL:
                tooltip_text = self.Symbol_Category_Tooltips.get(value)
            case _:
                return ""  # Frankly I'm more concerned _current_type isn't one of the things it should be
        log("d", f"getCategoryTooltip got tooltip text {tooltip_text}")
        return tooltip_text

    # Pop up the shape list
    def showShapelistPopup(self):
        if self._shape_list_dialog:  # You've got to be cruel to the code to be kind to the user
            self._shape_list_dialog.destroy()
            self._shape_list_dialog = None

        if self._shape_list_dialog is None:
            self._createShapelistPopup()
        self._shape_list_dialog.show()
            
    def _createShapelistPopup(self):
        #qml_file_path = os.path.join(os.path.dirname(__file__), "qml", "settings.qml")
        dialog_context = {
            "manager": self,
        }
        self._shape_list_dialog = CuraApplication.getInstance().createQmlComponent(self._shapelist_qml, dialog_context)
    
    categoryListChanged = pyqtSignal()
    shapeListChanged = pyqtSignal()

    @pyqtProperty(list, notify=categoryListChanged)
    def categoryList(self):
        return self._category_names
    
    def setShapeList(self, value):
        log("e", ">>>>>>>>>>>>> setShapeList setter FUNCTION WAS CALLED! <<<<<<<<<<<<<<<<<<")
        log("d", f"setShapeList: category_name argument passed = {value}")
        self.updateShapeList(value)
        log("d", f"setShapeList: after updateShapeList, self._shape_names = {self._shape_names} and self.shapeList = {self.shapeList}")

    
    #@pyqtProperty(list, notify=shapeListChanged, fset=setShapeList)
    #def shapeList(self):
    #    return self._shape_names
    @pyqtProperty(list, notify=shapeListChanged, fset=setShapeList)
    def shapeList(self):
        shape_list_to_return = self._shape_names # Assuming self._shape_names is now the list of dicts as in Step 59A
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
    def selectCategory(self, category_name):
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

    def updateShapeList(self, category_name = "", clear_only: bool = False):
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
    def selectType(self, type_name):
        log("d", f"StackOfShapes.selectType called with {type_name}")
        match type_name:
            case ShapeTypes.SHAPE.value:
                log("d", f"StackOfShapes.selectType matched Shape")
                self._current_type = ShapeTypes.SHAPE
                self._current_type_dict = self.Shapes
            case ShapeTypes.SYMBOL.value:
                log("d", f"StackOfShapes.selectType matched Symbol")
                self._current_type = ShapeTypes.SYMBOL
                self._current_type_dict = self.Symbols
            case _:
                log("d", f"StackOfShapes.selectType matched... nothing?")
                return  # We shouldn't be here.
        self.updateCategoryList()
        self._current_category = ""
        self.updateShapeList(clear_only=True)

    _current_type_changed = pyqtSignal()

    @pyqtProperty(str, notify = _current_type_changed)
    def CurrentType(self) -> str:
        return self._current_type.value

    def updateCategoryList(self, clear_only: bool = False):
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
        self._registerShapeStl(value, self.getModelPath(value))

    def getModelPath(self, model: str) -> str:
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
        log("i", f"StacksOfShapes QML Log: {value}")

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
        image_path = f"{self._qml_categories_icon_folder}{value}.png"
        abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "qml", image_path))
        log("d", f"getCategoryImage got relative image path: {image_path} which a abspath is {abs_path}")
        if os.path.exists(abs_path):
            return image_path
        else:
            return ""
        # I tried about three zillion ways to get it to work with absolute paths.
        # It's possible it just doesn't like Windows, considering the closest I got,
        # it removed the : after the drive letter.

    @pyqtSlot(str, result=str)
    def getShapeImage(self, value: str) -> str:
        model_relative_path = f"{self._qml_models_icon_folder}{self.getModelPath(value)}".replace("stl", "png")
        abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "qml", model_relative_path))
        log("d", f"getShapeImage got relative image path {model_relative_path} with an abspath of {abs_path}")
        if os.path.exists(abs_path):
            return model_relative_path
        else:
            return ""
           
    def _registerShapeStl(self, mesh_name, mesh_filename=None, **kwargs) -> None:
        if mesh_filename is None:
            mesh_filename = mesh_name + ".stl"
        
        model_definition_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models", mesh_filename)
        log("d", f"_registerShapeStl going to load {model_definition_path}")
        log("d", f"self._shape_size = {self._shape_size}")
        mesh =  trimesh.load(model_definition_path)
        
        # addShape
        self._addShape(mesh_name,self._toMeshData(mesh), **kwargs)

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
    
    def _createShape(self, shape_type):
        Logger.log("i", f"StacksOfShapes._createShape called with {shape_type}")
        
    # Initial Source code from  fieldOfView
    # https://github.com/fieldOfView/Cura-SimpleShapes/blob/bac9133a2ddfbf1ca6a3c27aca1cfdd26e847221/SimpleShapes.py#L70
    def _addShape(self, mesh_name, mesh_data: MeshData, ext_pos = 0 , hole = False , thin = False , mode = "" ) -> None:
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
 
        stack = node.callDecoration("getStack") # created by SettingOverrideDecorator that is automatically added to CuraSceneNode
        settings = stack.getTop()
        # Remove All Holes
        if hole :
            definition = stack.getSettingDefinition("meshfix_union_all_remove_holes")
            new_instance = SettingInstance(definition, settings)
            new_instance.setProperty("value", True)
            new_instance.resetState()  # Ensure that the state is not seen as a user state.
            settings.addInstance(new_instance) 
        # Print Thin Walls    
        if thin :
            definition = stack.getSettingDefinition("fill_outline_gaps")
            new_instance = SettingInstance(definition, settings)
            new_instance.setProperty("value", True)
            new_instance.resetState()  # Ensure that the state is not seen as a user state.
            settings.addInstance(new_instance)
 
        if len(mode) :
            definition = stack.getSettingDefinition("magic_mesh_surface_mode")
            new_instance = SettingInstance(definition, settings)
            new_instance.setProperty("value", mode)
            new_instance.resetState()  # Ensure that the state is not seen as a user state.
            settings.addInstance(new_instance)

        # node.setSetting(SceneNodeSettings.AutoDropDown, True)  # I don't even know where this line came from
            
        active_build_plate = application.getMultiBuildPlateModel().activeBuildPlate
        node.addDecorator(BuildPlateDecorator(active_build_plate))

        node.addDecorator(SliceableObjectDecorator())

        application.getController().getScene().sceneChanged.emit(node)