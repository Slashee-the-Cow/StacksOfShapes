import QtQuick 6.0
import QtQuick.Controls 6.0
import QtQuick.Layouts 6.0


import UM 1.6 as UM
import Cura 1.7 as Cura

UM.Dialog {
    property variant catalog: UM.I18nCatalog { name: "stacksofshapes" }

    id: shapeDialog
    title: catalog.i18nc("dialog:title", "Stacks of Shapes")
    width: 600
    height: 400

    modality: Qt.NonModal
    flags: (Qt.platform.os == "windows" ? Qt.Dialog : Qt.Window)  // <-- Ugly workaround for a bug in Windows, where the close-button doesn't show up unless we have a Dialog (but _not_ a Window).
        | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowStaysOnTopHint
    /*Connections {
        target: manager
        onShapeListChanged:{
            manager.logMessage("onShapeListChanged signal received. shapeList = " + shapeList + " typeof shapeList = " + typeof shapeList)
            shapeModel.clear()
            manager.logMessage("shapeModel has been cleared")
            for (let i = 0; i < shapeList.length; i++){
                let shapeName = shapeList[i]
                shapeModel.append({"shapeName": shapeName})
                manager.logMessage("Appended to shapeModel, shapeName = " + shapeName)
            }
            manager.logMessage("shapeModel population completed.")
        }
    }*/

    Component.onCompleted: { // Root Component.onCompleted - keep this for logging
        //manager.logMessage("root Component.onCompleted: categoryList = " + categoryList); // Keep root log
        manager.logMessage("Component.onCompleted: Triggering categoryList access...");
        categoryList; // Keep for potential initial category list refresh
        manager.logMessage("Component.onCompleted: categoryList = " + categoryList);
    }

    ColumnLayout{
        id: baseColumn
        anchors.fill: parent
        spacing: 0

        UM.TabRow {
            id: shapeSymbolTabRow
            Layout.fillWidth: true

            UM.TabRowButton {
                text: catalog.i18nc("dialog:shape_tab", "Shapes")
            }

            UM.TabRowButton {
                text: catalog.i18nc("dialog:symbol_tab", "Symbols")
            }
        }

        RowLayout {
            id: shapePickerRow
            Layout.fillWidth: true
            Layout.fillHeight: true

            // Category Column (Left)
            ColumnLayout {
                Layout.fillWidth: true
                Layout.fillHeight: true
                //Layout.preferredWidth: 200

                UM.Label{
                    text: "Categories"
                } // Category label

                ListView {
                    id: categoryListView
                    Layout.fillWidth: true
                    Layout.fillHeight: true // Make listview fill column height
                    model: categoryList  // Pulling a list straight from the Python file. Hey, if it works, right?
                    delegate: UM.Label {
                        text: modelData // Display category name
                        height: 50
                        MouseArea{
                            anchors.fill: parent
                            onClicked: {
                                manager.logMessage(modelData + " has been clicked, and before change the current manager.shapeList = " + manager.shapeList)
                                manager.selectCategory(modelData)
                            }
                        }
                        // ... (Styling, mouse click handling for category selection) ...
                        Component.onCompleted: { // Delegate onCompleted - for debugging!
                            //manager.logMessage("Delegate Component.onCompleted: modelData = " + modelData + ", typeof modelData = " + typeof modelData); // DELEGATE LOG!
                        }
                    }
                    Component.onCompleted: { // Delegate onCompleted - for debugging!
                        //manager.logMessage("ListView Component.onCompleted: categoryList = " + categoryList + ", typeof categoryList = " + typeof categoryList); // LIST LOG!
                    }
                }
            }

            // Shape Column (Right)
            ColumnLayout {
                Layout.fillWidth: true
                Layout.fillHeight: true
                UM.Label { text: "Shapes" } // Shape label

                ListModel {
                    id: shapeModel
                }

                ListView {
                    id: shapeListView

                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    model: manager.shapeList
                    delegate: UM.Label {
                        text: modelData // Display shape name
                        height: 50
                        MouseArea{
                            anchors.fill: parent
                            onClicked: {
                                manager.logMessage(modelData + " has been clicked, and before change the current manager.shapeList = " + manager.shapeList)
                                manager.loadModel(modelData)
                            }
                        }
                        Component.onCompleted: { // Delegate onCompleted - for debugging!
                            manager.logMessage("shapeModel Delegate Component.onCompleted: modelData = " + modelData + ", typeof modelData = " + typeof modelData); // DELEGATE LOG!
                        }
                        // ... (Styling, mouse click handling for shape selection) ...
                    }
                    Component.onCompleted: {
                        manager.logMessage("shapeListView onCompleted{}: Current model is" + model)
                    }
                }
            }
        }

        GridLayout {
            id: controlRow
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignBottom

            Rectangle {
                Layout.row: 0
                Layout.column: 0
                Layout.preferredWidth: 120
                height: 1
                color: "transparent"
            }
            Rectangle {
                Layout.row: 0
                Layout.column: 1
                Layout.fillWidth: true
                height: 1
                color: "transparent"
            }
            Rectangle {
                Layout.row: 0
                Layout.column: 2
                Layout.preferredWidth: 120
                height: 1
                color: "transparent"
            }

            RowLayout{
                id: shapeSizeHolder
                Layout.alignment: Qt.AlignLeft | Qt.AlignVCenter
                Layout.preferredHeight: implicitHeight
                Layout.row: 1
                Layout.column: 0
                UM.Label{
                    id: shapeSizeText
                    text: catalog.i18nc("dialog:shapeSize", "Shape size: ")
                    //Layout.preferredWidth: 40
                    //width: 60
                    //background: Rectangle { color: "pink"}
                }

                UM.TextFieldWithUnit{
                    id: shapeSizeTextField
                    unit: "mm"
                    Layout.preferredWidth: 80
                    validator: IntValidator{
                        bottom: 1
                    }
                    text: "20"
                    //background: Rectangle { color: "red"}
                }
            }

            UM.CheckBox{
                id: alwaysOnTopCheckBox
                Layout.row: 1
                Layout.column: 1
                Layout.alignment: Qt.AlignHCenter | Qt.AlignBottom
                //anchors.horizontalCenter: parent.horizontalCenter
                //anchors.verticalCenter: parent.verticalCenter
                text: catalog.i18nc("dialog:alwaysOnTop", "Always on top")
                checked: true  // Always on top by default

                onCheckedChanged: {
                    if(checked){
                        shapeDialog.flags = shapeDialog.flags | Qt.WindowStaysOnTopHint
                    } else {
                        shapeDialog.flags = shapeDialog.flags & ~Qt.WindowStaysOnTopHint
                    }
                }
                //background: Rectangle { color: "blue"}
            }

            Cura.TertiaryButton{
                id: closeButton
                Layout.alignment: Qt.AlignRight | Qt.AlignBottom
                Layout.preferredHeight: implicitHeight
                Layout.row: 1
                Layout.column: 2
                text: catalog.i18nc("dialog:close", "Close")

                onClicked: {shapeDialog.close()}
                //background: Rectangle { color: "green"}
            }
        }
    }
}