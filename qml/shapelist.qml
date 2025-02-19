import QtQuick 6.0
import QtQuick.Controls 6.0
import QtQuick.Layouts 6.0

import UM 1.6 as UM

UM.Dialog {
    id: shapeDialog
    width: 400
    height: 300
    title: "Shape Selection"

    ColumnLayout {
        anchors.fill: parent

        ListView {  // Categories
            width: shapeDialog.width / 2
            height: 200
            model: categories
            delegate: Rectangle {
                width: parent.width
                height: 40
                color: "lightblue"
                Text {
                    text: modelData
                    anchors.centerIn: parent
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        shapeListUI.selectedCategoryIndex = categoryList.currentIndex
                    }
                }
            }
        }

        ListView {  // Shapes (filtered)
            width: shapeDialog.width / 2
            height: 200
            model: shapesListUI.selectedCategoryIndex >= 0 ? shapesList[shapesListUI.selectedCategoryIndex] : []
            delegate: Rectangle {
                width: parent.width
                height: 40
                color: "lightgray"
                Text {
                    text: modelData.name
                    anchors.centerIn: parent
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        shapeListUI.create_shape(modelData.path); // Call Python function
                    }
                }
            }
        }
    }
}