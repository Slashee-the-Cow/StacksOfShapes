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

        Timer {
        id: updateTimer
        interval: 100 // Small delay (milliseconds)
        repeat: false
            onTriggered: {
                rootObject.forceLayoutUpdate();
            }
        }

        Component.onCompleted: {
            updateTimer.start();
        }

        ListView {
            id: categoryListView
            width: parent.width
            height: 150
            model: shapeListModel
            delegate: Rectangle {
                width: categoryListView.width
                height: 40
                color: "lightblue"
                Text {
                    text: modelData ? modelData.category : "BlankCategory"
                    anchors.centerIn: parent
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        shapeListModel.select_category(modelData.category)
                    }
                }
            }
        }

        ListView {
            id: shapeListView
            width: parent.width
            height: parent.height - categoryListView.height
            model: shapeListModel  // Use the same model
            delegate: Rectangle {
                width: shapeListView.width
                height: 40
                color: "lightgray"
                Text {
                    text: modelData ? modelData.shapeName : "BlankShapeName"
                    anchors.centerIn: parent
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        shapeListUI._handleShapeSelection(modelData.shapeName) // And here!
                    }
                }
            }
        }
    }
}