import os

from PyQt6.QtCore import QObject, QMetaObject, Qt

from cura.CuraApplication import CuraApplication
from UM.Logger import Logger

from .shapelistmodel import ShapeListModel
from .interactions import UIInteraction, MainInteraction

# from typing import TYPE_CHECKING

#if TYPE_CHECKING:
#    from .StacksOfShapes import StacksOfShapes

class ShapeListUI(QObject, UIInteraction):
    
    def __init__(self, model: ShapeListModel, parent = None):
        super().__init__(parent)
        
        self._list_popup = None
        self._qml_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "qml", "shapelist.qml"))

        self._model = model
        self._main_instance = None

    def set_main_instance(self, instance: MainInteraction):
        self._main_instance = instance

    def set_model_data(self, data):
        self._model.set_data(data)

    def _handle_shape_selected(self, shape_type):
        self._main_instance.createShape(shape_type)
    
    def showListPopup(self) -> None:
        if self._list_popup is None:
            self._createListPopup()

        if self._list_popup:
            self._list_popup.show()

    def _createListPopup(self):
        context = {
            "shapeListModel": self._model,
            "shapeListUI": self,
            "rootObject": None
        }
        
        self._list_popup = CuraApplication.getInstance().createQmlComponent(
            self._qml_path,
            context
        )

        if not self._list_popup:
            Logger.log("e", "StacksOfShapes.ShapeList could not create QML component.")
            return
        
        root_object = self._list_popup.rootObject()
        context["rootObject"] = root_object  # Add to the context