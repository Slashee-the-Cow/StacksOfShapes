# Part of initial code by fieldOfView 2018
# Stacks of Shapes copyright Slashee the Cow 2025-

# Utah Teapot model by zzubnik  -  https://www.thingiverse.com/thing:852078 under the Creative Commons Public Domain licence

# Version history
# 1.0.0:    Initial release.


import os
import sys
import math
import numpy
import trimesh
from enum import Enum, auto

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


from PyQt6.QtCore import Qt, QObject, pyqtSlot, pyqtSignal, pyqtProperty

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

        # Get values from preferences
        self._shape_size = float(self._preferences.getValue("stacksofshapes/shapesize"))  
        self._symbol_size = float(self._preferences.getValue("stacksofshapes/symbolsize"))

        self._shape_list_dialog = None
        
        self._shapelist_qml = os.path.abspath(os.path.join(os.path.dirname(__file__), "qml", "shapeslist.qml"))
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
        """self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a cube"), self.addCube)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a cylinder"), self.addCylinder)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a sphere"), self.addSphere)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a tube"), self.addTube)
        self.addMenuItem("", lambda: None)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a Calibration Cube"), self.addCalibrationCube)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a Layer Adhesion Test"), self.addLayerAdhesion)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a Retract Test"), self.addRetractTest)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a XY Calibration Test"), self.addXYCalibration)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a Dimensional Accuracy Test"), self.addDimensionalTest)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a Tolerance Test"), self.addTolerance)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a Hole Test"), self.addHoleTest)
        
        # self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a Junction Deviation Tower"), self.addJunctionDeviationTower)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a Bridge Test"), self.addBridgeTest)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a Thin Wall Test"), self.addThinWall)
        # self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a Thin Wall Test Cura 5.0"), self.addThinWall2)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add an Overhang Test"), self.addOverhangTest)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a Flow Test"), self.addFlowTest)
        
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a Support Test"), self.addSupportTest)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a Lithophane Test"), self.addLithophaneTest)
        
        # self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a MultiCube Calibration"), self.addMultiCube)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a Bed Level Calibration"), self.addBedLevelCalibration)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a Backlash Test"), self.addBacklashTest)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a Linear/Pressure Adv Tower"), self.addPressureAdvTower)
        self.addMenuItem("  ", lambda: None)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a Cube bi-color"), self.addCubeBiColor)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add a Bi-Color Calibration Cube"), self.addHollowCalibrationCube)
        self.addMenuItem(catalog.i18nc("@item:inmenu", "Add an Extruder Offset Calibration Part"), self.addExtruderOffsetCalibration)        
        self.addMenuItem("   ", lambda: None)"""
        #self.addMenuItem(catalog.i18nc("@item:inmenu", "Set default size"), self.showSettingsPopup)

    
    Shapes = {
        catalog.i18nc("shape_category", "Basics"): {
            catalog.i18nc("shape_name", "Cube"): "platonics/hexahedron.stl",
            catalog.i18nc("shape_name", "Sphere"): "basics/sphere.stl",
        },
        catalog.i18nc("shape_category", "Platonic Solids"): {
            catalog.i18nc("shape_name", "Tetrahedron (4 sides)"): "platonics/tetrahedron.stl",
            catalog.i18nc("shape_name", "Hexahedron (6 sides)"): "platonics/hexahedron.stl",
            catalog.i18nc("shape_name", "Octahedron (8 sides)"): "platonics/octahedron.stl",
            catalog.i18nc("shape_name", "Dodecahedron (12 sides)"): "platonics/dodecahedron.stl",
            catalog.i18nc("shape_name", "Icosahedron (20 sides)"): "platonics/icosahedron.stl",
        }
    }

    Symbols = {
        catalog.i18nc("symbol_category", "Arrows"): {
            catalog.i18nc("symbol_name", "Straight Arrow"): "2d/arrows/arrow_single.stl",
        },
        catalog.i18nc("symbol_category", "Hearts"): {
            catalog.i18nc("symbol_name", "Heart"): "2d/hearts/heart.stl"
        }
    }

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

    
    @pyqtProperty(list, notify=shapeListChanged, fset=setShapeList)
    def shapeList(self):
        return self._shape_names
    
    @pyqtSlot(str)
    def selectCategory(self, category_name):
        if category_name == self._current_category:  # Nothing to do here, don't want to waste time recomposing a ListView
            return
        log("d", f"Current category is {self._current_category} - Trying to access shapes category: {category_name}")
        self.updateShapeList(category_name)

    def updateShapeList(self, category_name = "", clear_only: bool = False):
        if clear_only:
            log("d", f"updateShapeList called with clear_only")
            self._shape_names = []
            self.shapeListChanged.emit()
            return
        log("d", f"In updateShapeList. Before clearing, self.shapeList = {self.shapeList}")
        self._shape_names = []
        if category_name in self._current_type_dict:
            self._shape_names = list(self._current_type_dict[category_name].keys())
            self._current_category = category_name
        log("d", f"For {category_name} we got {self._shape_names}")
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
                log("d", f"StackOfShapes.selectType matched Symbol")
                return  # We shouldn't be here.
        self.updateCategoryList()
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
        self._registerShapeStl(value, self._current_type_dict[self._current_category][value])

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
          
           
    def _registerShapeStl(self, mesh_name, mesh_filename=None, **kwargs) -> None:
        if mesh_filename is None:
            mesh_filename = mesh_name + ".stl"
        
        model_definition_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models", mesh_filename)
        log("d", f"_registerShapeStl going to load {model_definition_path}")
        log("d", f"self._shape_size = {self._shape_size}")
        mesh =  trimesh.load(model_definition_path)
        
        # addShape
        self._addShape(mesh_name,self._toMeshData(mesh), **kwargs)
                     
    #-----------------------------
    #   Standard Geometry  
    #-----------------------------    
    # Origin, xaxis, yaxis, zaxis = [0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]
    # S = trimesh.transformations.scale_matrix(20, origin)
    # xaxis = [1, 0, 0]
    # Rx = trimesh.transformations.rotation_matrix(math.radians(90), xaxis)    
    """def addCube(self) -> None:
        Tz = trimesh.transformations.translation_matrix([0, 0, self._shape_size*0.5])
        self._addShape("Cube",self._toMeshData(trimesh.creation.box(extents = [self._shape_size, self._shape_size, self._shape_size], transform = Tz )))
        
    def addCylinder(self) -> None:
        mesh = trimesh.creation.cylinder(radius = self._shape_size / 2, height = self._shape_size, sections=90)
        mesh.apply_transform(trimesh.transformations.translation_matrix([0, 0, self._shape_size*0.5]))
        self._addShape("Cylinder",self._toMeshData(mesh))

    def addTube(self) -> None:
        mesh = trimesh.creation.annulus(r_min = self._shape_size / 4, r_max = self._shape_size / 2, height = self._shape_size, sections = 90)
        mesh.apply_transform(trimesh.transformations.translation_matrix([0, 0, self._shape_size*0.5]))
        self._addShape("Tube",self._toMeshData(mesh))
        
    # Sphere are not very usefull but I leave it for the moment    
    def addSphere(self) -> None:
        # subdivisions (int) – How many times to subdivide the mesh. Note that the number of faces will grow as function of 4 ** subdivisions, so you probably want to keep this under ~5
        mesh = trimesh.creation.icosphere(subdivisions=4,radius = self._shape_size / 2,)
        mesh.apply_transform(trimesh.transformations.translation_matrix([0, 0, self._shape_size*0.5]))
        self._addShape("Sphere",self._toMeshData(mesh))"""


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

        # 3 - Get the size of the largest dimension
        max_bound: Any = numpy.max(dimensions)

        # 4 - Calculate the scaling factor based on the largest dimension and the target size
        if max_bound > 0:  # Make sure we handle a degenerate mesh gracefully
            scale_factor = target_size / max_bound
        else:
            scale_factor = 1

        # 5 - Scale your mesh by that much
        tri_node.apply_scale(scale_factor)

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

        node.setSetting(SceneNodeSettings.AutoDropDown, True)
            
        active_build_plate = application.getMultiBuildPlateModel().activeBuildPlate
        node.addDecorator(BuildPlateDecorator(active_build_plate))

        node.addDecorator(SliceableObjectDecorator())

        application.getController().getScene().sceneChanged.emit(node)