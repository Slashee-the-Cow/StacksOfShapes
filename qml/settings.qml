// Copyright 2025 Slashee the Cow

import QtQuick 6.0
import QtQuick.Controls 6.0
import QtQuick.Layouts 6.0

import UM 1.6 as UM
import Cura 1.7 as Cura

UM.Dialog {
    id: sosSettings

    property bool validInput: false

    function validateInput(text) {
        validInput = (text !== "" && !isNaN(text) && parseInt(text) >= 1 && parseInt(text) <= 200);
        return validInput
    }
    
    property int shapeSizeValue: 999

    property variant catalog: UM.I18nCatalog { name: "stacksofshapes" }

    Component.onCompleted: {
        shapeSizeValue = manager.ShapeSize
        shapeSizeTextField.forceActiveFocus()
    }

    title: catalog.i18nc("@title", "Stacks of Shapes Settings")

    backgroundColor: UM.Theme.getColor("main_background")
    buttonSpacing: UM.Theme.getSize("default_margin").width
    minimumWidth: Math.max((mainLayout.Layout.minimumWidth + 3 * UM.Theme.getSize("default_margin").width),
        (sizeErrorMessage.contentWidth + 50 * screenScaleFactor + 3 * UM.Theme.getSize("default_margin").width),
        (saveButton.width + cancelButton.width + 4 * UM.Theme.getSize("default_margin").width))
    maximumWidth: minimumWidth
    width: minimumWidth
    minimumHeight: mainLayout.Layout.minimumHeight + sizeErrorMessage.contentHeight + (2 * UM.Theme.getSize("default_margin").height) + saveButton.height + UM.Theme.getSize("default_lining").height
    //minimumHeight: 300 * screenScaleFactor
    maximumHeight: minimumHeight
    height: minimumHeight


// Use a Layout for the main content
    ColumnLayout {
        id: mainLayout
        anchors.fill: parent
        anchors.margins: UM.Theme.getSize("default_margin").width
        spacing: UM.Theme.getSize("default_lining").height

        // Group related elements together (e.g., using a GroupBox)
        //GroupBox {
            //id: shapeSettings
            //anchors.top: mainLayout.Layout.top
            //title: catalog.i18nc("@group_label", "Shape Size Settings") // Replace with your group label

        ColumnLayout {
            spacing: UM.Theme.getSize("default_lining").height

            RowLayout {
                spacing: UM.Theme.getSize("default_margin").width

                UM.Label {
                    text: catalog.i18nc("@label", "Shape size")
                }

                UM.TextFieldWithUnit {
                    id: shapeSizeTextField
                    Layout.minimumWidth: 75 * screenScaleFactor
                    height: UM.Theme.getSize("setting_control").height
                    unit: "mm"
                    placeholderText: shapeSizeValue.toString()
                    focus: true

                    validator: IntValidator {
                        bottom: 1
                        top: 200
                    }

                    Connections {
                        target: sosSettings
                        function onShapeSizeValueChanged() {
                            shapeSizeTextField.text = sosSettings.shapeSizeValue.toString()
                        }
                    }

                    onTextChanged: {
                        if(validateInput(shapeSizeTextField.text)){
                            shapeSizeValue = parseInt(shapeSizeTextField.text)
                        }
                    }
                }
            }

            // Add any other shape-related settings here
        }
        //}

        UM.Label {
            id: placeholder
            text: " <br> "
            width: 100 * screenScaleFactor
            visible: validInput
        }

        UM.Label {
            id: sizeErrorMessage
            color: "red"
            text: catalog.i18nc("@warning_text", "Please enter a valid number<br>Between 1 and 200")
            visible: !validInput
            width: 100 * screenScaleFactor
            wrapMode: Text.WordWrap
            elide: Text.ElideNone
        }
    }

    // Buttons
    rightButtons: [
        Cura.SecondaryButton {
            id: cancelButton
            text: catalog.i18nc("@cancel", "Cancel")
            
            onClicked: {
                sosSettings.reject()
            } 
        },
        Cura.PrimaryButton {
            id: saveButton
            text: catalog.i18nc("@save", "Save")
            enabled: validInput // Disable the button if input is invalid
            onClicked: {
                if(validInput){
                    sosSettings.accept()
                } else {
                    shapeSizeTextField.forceActiveFocus()        
                }
            }
        }
    ]

    onAccepted: {
        if (validInput){
            manager.SetShapeSize(shapeSizeValue)
        } else {
            reject()
        }
    }

    onRejected: {
        shapeSizeTextField.text = manager.ShapeSize.toString()
    }
}