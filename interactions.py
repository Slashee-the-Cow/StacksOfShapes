class MainInteraction():
    def createShape(self, shape_type: str):
        raise NotImplementedError

class UIInteraction():
    def showListPopup(self):
        raise NotImplementedError

    def set_model_data(self, data: dict):
        raise NotImplementedError

    def set_main_instance(self, main_instance: MainInteraction):
        raise NotImplementedError