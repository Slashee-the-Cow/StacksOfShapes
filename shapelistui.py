from __future__ import annotations

import os

from PyQt6.QtCore import QObject, pyqtSignal, pyqtProperty
from PyQt6.QtQml import QQmlContext
from PyQt6.QtQuick import QQuickItem

from typing import TYPE_CHECKING

from cura.CuraApplication import CuraApplication
from UM.Logger import Logger

if TYPE_CHECKING:
    from PyQt6.QtQuick import QQuickWindow


from .interactions import UIInteraction, MainInteraction

# from typing import TYPE_CHECKING

#if TYPE_CHECKING:
#    from .StacksOfShapes import StacksOfShapes

class ShapeListUI(QObject, UIInteraction):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self._list_popup = None
        self._qml_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "qml", "shapelist.qml"))

        self._shapes = {}
        self._main_instance = None

        self._selected_category_index = -1

    def set_main_instance(self, instance: MainInteraction):
        self._main_instance = instance

    def set_shape_data(self, data):
        self._shapes = data

    def create_shape(self, path):
        self._main_instance.createShape(path)
    
    def showListPopup(self) -> None:
        if self._list_popup is None:
            self._createListPopup()

        if self._list_popup:
            self._list_popup.show()

    def _createListPopup(self):

        categories = list(self._shapes.keys())
        shape_list = []
        for category in categories:
            shape_list.append([{"name": shape_name, "path": shape_path} for shape_name, shape_path in self._shapes[category].items()])

        context = {
            "categories": categories,
            "shapesList": shape_list,
            "shapeListUI": self,
        }
        
        self._list_popup = CuraApplication.getInstance().createQmlComponent(
            self._qml_path,
            context
        )

        if not self._list_popup:
            Logger.log("e", "StacksOfShapes.ShapeList could not create QML component.")
            return
   
    selectedCategoryIndexChanged = pyqtSignal(int)

    @pyqtProperty(int, notify=selectedCategoryIndexChanged)
    def selectedCategoryIndex(self) -> int:
        return self._selected_category_index
    
    @selectedCategoryIndex.setter
    def selectedCategoryIndex(self, index: int):
        if self.selectedCategoryIndex != index:
            self._selected_category_index = index
            self.selectedCategoryIndexChanged.emit(index)