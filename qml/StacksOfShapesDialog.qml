import QtQuick 6.0
import QtQuick.Controls 6.0
import QtQuick.Layouts 6.0


import UM 1.6 as UM
import Cura 1.7 as Cura

UM.Dialog {

    function isValidInt(text){
        let value = parseInt(text)  // Should be NaN on blank
        return !isNaN(value)
    }
    function isValidFloat(text){
        let value = parseFloat(text)
        return !isNaN(value)
    }

    readonly property string shapeTypeShape: "SHAPE"  // Would the equivalent of an enum be a regular object? Eh, this is easier
    readonly property string shapeTypeSymbol: "SYMBOL"
    readonly property string tooltipKey: "tooltip"

    property string currentShapeType: shapeTypeShape  // Default at startup

    property variant catalog: UM.I18nCatalog { name: "stacksofshapes" }

    id: shapeDialog
    title: catalog.i18nc("dialog:title", "Stacks of Shapes")
    width: 600
    height: 400
    x: 200
    y: 200


    modality: Qt.NonModal
    flags: (Qt.platform.os == "windows" ? Qt.Dialog : Qt.Window)  // <-- Ugly workaround for a bug in Windows, where the close-button doesn't show up unless we have a Dialog (but _not_ a Window).
        | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowStaysOnTopHint

    Component.onCompleted: { // Root Component.onCompleted - keep this for logging
        //manager.logMessage("root Component.onCompleted: categoryList = " + manager.categoryList); // Keep root log
        manager.logMessage("Component.onCompleted: Triggering categoryList access...");
        manager.categoryList; // Keep for potential initial category list refresh
        manager.logMessage("Component.onCompleted: categoryList = " + manager.categoryList);
        manager.logMessage("Component.onCompleted: manager.CurrentType = " + manager.CurrentType)
        currentShapeType = manager.CurrentType
        if(currentShapeType == shapeTypeSymbol){
            shapeTypeTabShape.checked = false
            shapeTypeTabSymbol.checked = true
        }
    }

    /*Item {
        id: keyListener
        anchors.fill: parent
        focus: true
        // Ensure it always stays focused.
        onActiveFocusChanged: {
            if (!activeFocus) keyListener.forceActiveFocus();
        }

        Keys.onPressed: {
            // Log key info for debugging.
            manager.logMessage("Key pressed: " + event.key, " modifiers: " + event.modifiers);
            // Update the global property when both Alt and Shift are held.
            shapeDialog.globalAltShiftPressed = (event.modifiers & Qt.AltModifier) && (event.modifiers & Qt.ShiftModifier);
        }
        Keys.onReleased: {
            manager.logMessage("Key released: " + event.key + " modifiers: " + event.modifiers);
            // Re-check the modifiers on key release.
            shapeDialog.globalAltShiftPressed = (event.modifiers & Qt.AltModifier) && (event.modifiers & Qt.ShiftModifier);
        }
    }*/

    ColumnLayout{
        id: baseColumn
        anchors.fill: parent
        spacing: 0

        UM.TabRow {
            id: shapeSymbolTabRow
            Layout.fillWidth: true
            Layout.preferredHeight: childrenRect.height

            UM.TabRowButton {
                id: shapeTypeTabShape
                text: catalog.i18nc("dialog:shape_tab", "Shapes")
                height: 30

                onClicked: {
                    if (currentShapeType !== shapeTypeShape){
                        manager.selectType(shapeTypeShape)
                        currentShapeType = shapeTypeShape
                    }
                }
            }

            UM.TabRowButton {
                id: shapeTypeTabSymbol
                text: catalog.i18nc("dialog:symbol_tab", "Symbols")
                height: 30

                onClicked: {
                    if (currentShapeType !== shapeTypeSymbol){
                        manager.selectType(shapeTypeSymbol)
                        currentShapeType = shapeTypeSymbol
                    }
                }
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

                /*UM.Label{
                    text: "Categories"
                } // Category label*/

                ListView {
                    id: categoryListView
                    clip: true
                    Layout.preferredWidth: 200
                    Layout.fillHeight: true // Make listview fill column height
                    model: manager.categoryList  // Pulling a list straight from the Python file. Hey, if it works, right?
                    delegate: ShapeListDelegate{
                        delegateText: modelData
                        delegateImageSource: {
                            let image_path = manager.getCategoryImage(modelData)
                            manager.logMessage("Delegate trying to get image for category " + modelData + " got " + image_path + " which is type " + typeof image_path)
                            return image_path
                        }
                        delegateClickedFunction: function(categoryName) {manager.selectCategory(categoryName)}
                        defaultTooltipText: manager.getCategoryTooltip(modelData)
                        alternateTooltipText: manager.getCategoryAltTooltip(modelData)
                        /*alternateTooltipMode: {
                            manager.logMessage("Delegate attempting to set alternateTooltipMode to " + globalAltShiftPressed)
                            return shapeDialog.globalAltShiftPressed
                        }*/
                    }
                    ScrollBar.vertical: ScrollBar{
                        policy: categoryListView.contentHeight > categoryListView.height ? ScrollBar.AlwaysOn : ScrollBar.AlwaysOff
                    }
                    Component.onCompleted: { // Delegate onCompleted - for debugging!
                        //manager.logMessage("ListView Component.onCompleted: categoryList = " + manager.categoryList + ", typeof categoryList = " + typeof manager.categoryList); // LIST LOG!
                    }
                }
            }

            // Shape Column (Right)
            ColumnLayout {
                Layout.fillWidth: true
                Layout.fillHeight: true
                /*UM.Label { text: "Shapes" } // Shape label*/

                ListView {
                    id: shapeListView
                    clip: true
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    ScrollBar.vertical: ScrollBar{
                        policy: shapeListView.contentHeight > shapeListView.height ? ScrollBar.AlwaysOn : ScrollBar.AlwaysOff
                    }
                    model: manager.shapeList
                    delegate: ShapeListDelegate{
                        delegateText: modelData.shapeName
                        delegateImageSource: manager.getShapeImage(modelData.shapeName)
                        delegateClickedFunction: function(shapeName) {manager.loadModel(shapeName)}
                        defaultTooltipText: {
                            /*manager.logMessage("ShapeDelegate (Shape): modelData =" + modelData);
                            for (var key in modelData) {
                                manager.logMessage("  Key: " + key + ", Value: " + modelData[key]);
                            }
                            manager.logMessage("ShapeDelegate (Shape): tooltipKey = " + tooltipKey);
                            manager.logMessage("ShapeDelegate (Shape): modelData.shapeData[tooltipKey] = " + modelData.shapeData[tooltipKey]);
                            manager.logMessage("ShapeDelegate (Shape): modelData.shapeData[shapeDialog.tooltipKey] = " + modelData.shapeData[shapeDialog.tooltipKey]);
                            manager.logMessage("ShapeDelegate (Shape) - DEBUGGING - Trying modelData.shapeData.tooltip Directly: " + modelData.shapeData.tooltip); // NEW! - Try direct property access!*/
                            return modelData.shapeData[shapeDialog.tooltipKey]; // Keep original dictionary access for now, but log direct access result
                        alternateTooltipMode: {
                            manager.logMessage("Delegate attempting to set alternateTooltipMode to " + shapeDialog.globalAltShiftPressed)
                            return shapeDialog.globalAltShiftPressed
                            }
                            // return modelData.tooltip; // ALTERNATIVE -  *TEMPORARILY* TRY RETURNING DIRECT ACCESS - for debugging ONLY
                        }
                    }
                    Component.onCompleted: {
                        manager.logMessage("shapeListView onCompleted{}: Current model is " + model)
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
                visible: currentShapeType == shapeTypeShape
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
                    property string displayShapeSize: ""
                    Layout.preferredWidth: 80
                    validator: IntValidator{
                        bottom: 1
                    }
                    text: displayShapeSize
                    //background: Rectangle { color: "red"}
                    onTextChanged: {
                        manager.logMessage("shapeSizeTextField text changed")
                        if (isValidInt(text)) {
                            manager.logMessage("shapeSizeTextField text change is valid int: " + text)
                            manager.ShapeSize = parseInt(text)
                        }
                    }
                    Component.onCompleted: {
                        displayShapeSize = manager.ShapeSize.toString()
                        manager.logMessage("shapeSizeTextField has been completed and its text is " + text)
                    }
                }
            }

            RowLayout{
                id: symbolSizeHolder
                visible: currentShapeType == shapeTypeSymbol
                Layout.alignment: Qt.AlignLeft | Qt.AlignVCenter
                Layout.preferredHeight: implicitHeight
                Layout.row: 1
                Layout.column: 0
                UM.Label{
                    id: symbolSizeText
                    text: catalog.i18nc("dialog:symbolSize", "Symbol size: ")
                    //Layout.preferredWidth: 40
                    //width: 60
                    //background: Rectangle { color: "pink"}
                }

                UM.TextFieldWithUnit{
                    id: symbolSizeTextField
                    unit: "mm"
                    property string displaySymbolSize: ""
                    Layout.preferredWidth: 80
                    validator: IntValidator{
                        bottom: 1
                    }
                    text: displaySymbolSize
                    onTextChanged: {
                        manager.logMessage("symbolSizeTextField text changed")
                        if (isValidInt(text)) {
                            manager.logMessage("symbolSizeTextField text change is valid int: " + text)
                            manager.SymbolSize = parseInt(text)
                        }
                    }
                    Component.onCompleted: {
                        displaySymbolSize = manager.SymbolSize.toString()
                        manager.logMessage("symbolSizeTextField has been completed and its text is " + text)
                    }
                    //background: Rectangle { color: "red"}
                }
            }

            RowLayout{
                id: symbolHeightHolder
                visible: currentShapeType == shapeTypeSymbol
                Layout.alignment: Qt.AlignLeft | Qt.AlignVTop
                Layout.preferredHeight: implicitHeight
                Layout.row: 2
                Layout.column: 0
                UM.Label{
                    id: symbolHeightText
                    text: catalog.i18nc("dialog:symbolHeight", "Symbol height: ")
                    //Layout.preferredWidth: 40
                    //width: 60
                    //background: Rectangle { color: "pink"}
                }

                UM.TextFieldWithUnit{
                    id: symbolHeightTextField
                    unit: "mm"
                    property string displaySymbolHeight: ""
                    Layout.preferredWidth: 80
                    validator: DoubleValidator{
                        bottom: 0.1
                        decimals: 2
                    }
                    text: displaySymbolHeight
                    onTextChanged: {
                        manager.logMessage("symbolHeightTextField text changed")
                        if (isValidFloat(text)) {
                            manager.logMessage("symbolHeightTextField text change is valid float: " + text)
                            manager.SymbolHeight = parseFloat(text)
                        }
                    }
                    Component.onCompleted: {
                        displaySymbolHeight = manager.SymbolHeight.toString()
                        manager.logMessage("symbolHeightTextField has been completed and its text is " + text)
                    }
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