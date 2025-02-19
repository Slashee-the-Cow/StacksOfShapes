# The Stacks of Shapes plugin is released under the terms of the AGPLv3 or higher.

from .StacksOfShapes import StacksOfShapes
from .shapelistui import ShapeListUI

shapes_ui_instance = ShapeListUI()
main_instance = StacksOfShapes(shapes_ui_instance)
shapes_ui_instance.set_main_instance(main_instance)

def getMetaData():
    return {}

def register(app):
    return {"extension": main_instance}
