from PyQt6.QtCore import QAbstractListModel, Qt, QModelIndex

class ShapeListModel(QAbstractListModel):
    CategoryRole = Qt.ItemDataRole.UserRole + 1
    ShapeNameRole = Qt.ItemDataRole.UserRole + 2
    ShapeFileRole = Qt.ItemDataRole.UserRole + 3

    def __init__(self, parent=None):
        super().__init__(parent)
        self._data = {}
        self._categories = []
        self._shapes = []
        self._selected_category = None

    def set_data(self, data):
        self.beginResetModel()
        self._data = data
        self._categories = list(data.keys())
        if self._categories:
            self._selected_category = self._categories[0]
            self._shapes = []
            for name, file in self._data[self._selected_category].items():
                self._shapes.append({"name": name, "file": file})
        self.endResetModel()

    def rowCount(self, parent):
        if not parent.isValid():
            return len(self._categories)
        else:
            return len(self._shapes)

    def data(self, index: QModelIndex, role):
        if not index.isValid():  # Categories
            if role == ShapeListModel.CategoryRole:
                return self._categories[index.row()]
        else:  # Shapes
            if role == ShapeListModel.ShapeNameRole:
                return self._shapes[index.row()]["name"]
            elif role == ShapeListModel.ShapeFileRole:
                return self._shapes[index.row()]["file"]
        return None

    def roleNames(self):
        roles = super().roleNames()
        roles[ShapeListModel.CategoryRole] = b'category'  # Must match QML
        roles[ShapeListModel.ShapeNameRole] = b'shapeName'  # Must match QML
        roles[ShapeListModel.ShapeFileRole] = b'shapeFile' # Must match QML
        return roles

    def select_category(self, category):
        self._selected_category = category
        self._shapes = []
        if category in self._data:
            for name, file in self._data[category].items():
                self._shapes.append({"name": name, "file": file})
        self.layoutChanged.emit()