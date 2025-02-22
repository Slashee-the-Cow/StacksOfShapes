# The Stacks of Shapes plugin is released under the terms of the AGPLv3 or higher.

from .StacksOfShapes import StacksOfShapes

def getMetaData():
    return {}

def register(app):
    return {"extension": StacksOfShapes()}
