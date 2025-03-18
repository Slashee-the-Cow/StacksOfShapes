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

    function stripNonAlphanumeric(str) {
        return str.replace(/[^a-zA-Z0-9]/g, '');
    }

    function toggleAltMode(){
        if (!altMode){
            shapeTypeTabShape.text = shapeTypeTabShape.text + "🤣"
        } else {
            shapeTypeTabShape.text = stripNonAlphanumeric(shapeTypeTabShape.text)
        }
        altMode = !altMode
    }

    readonly property string shapeTypeShape: "SHAPE"  // Would the equivalent of an enum be a regular object? Eh, this is easier
    readonly property string shapeTypeSymbol: "SYMBOL"
    readonly property string tooltipKey: "tooltip"

    property bool race_condition_workaround: false
    property bool display_tip: manager.displayTip

    property int baseDialogHeight: 480
    property int extraDialogHeight: (race_condition_workaround ? 0 : 0) + (display_tip ? tipLayout.implicitHeight : 0)

    property string currentShapeType: shapeTypeShape  // Default at startup
    
    property bool altMode: false

    property variant catalog: UM.I18nCatalog { name: "stacksofshapes" }

    id: shapeDialog
    title: catalog.i18nc("dialog:title", "Stacks of Shapes")
    width: 600
    height: baseDialogHeight + extraDialogHeight
    x: 200
    y: 200


    onClosing: (close) => {
        close.accepted = false
        manager.logMessage("shapeDialog.onClosing{} running: explicitly destroying Dialog")
        Qt.callLater(function(){
            manager.justDestroyShapeList()
        })
    }


    modality: Qt.NonModal
    flags: (Qt.platform.os == "windows" ? Qt.Dialog : Qt.Window)  // <-- Ugly workaround for a bug in Windows, where the close-button doesn't show up unless we have a Dialog (but _not_ a Window).
        | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowStaysOnTopHint

    Component.onCompleted: { // Root Component.onCompleted - keep this for logging
        //manager.logMessage("root Component.onCompleted: categoryList = " + manager.categoryList); // Keep root log
        manager.logMessage("Component.onCompleted: Triggering categoryList access...");
        manager.categoryList; // Keep for potential initial category list refresh
        manager.logMessage("Component.onCompleted: categoryList = " + manager.categoryList);
        manager.logMessage("Component.onCompleted: manager.CurrentType = " + manager.CurrentType)
        manager.logMessage("Component.onCompleted: race_version = " + race_version)
        manager.logMessage("Component.onCompleted: UM.Preferences.getValue(general/auto_slice) = " + UM.Preferences.getValue("general/auto_slice"))
        if (race_version && UM.Preferences.getValue("general/auto_slice")){
            // This is required due to a race condition in Cura <= 5.9 which causes crashing when trying to automatically slice simple geometry.
            race_condition_workaround = true // Only enable force false if it's true to begin with
            UM.Preferences.setValue("general/auto_slice", false)
        }
        currentShapeType = manager.CurrentType
        if(currentShapeType == shapeTypeSymbol){
            shapeTypeTabShape.checked = false;
            shapeTypeTabSymbol.checked = true;
        }
        manager.logMessage("tipLayout.implicitHeight = " + tipLayout.implicitHeight)
        manager.logMessage("shapeDialog.height = " + shapeDialog.height)
    }


    Component.onDestruction: {
        manager.logMessage("shapeDialog.onDestruction{} running")
        if (race_condition_workaround){
            manager.logMessage("shapeDialog.onDestruction{} should be setting general/auto_slice back to true")
            UM.Preferences.setValue("general/auto_slice", true)
            manager.logMessage("shapeDialog.onDestruction{} should have just set general/auto_slice back to true")
            // The workaround would only have been enabled if it were true when the window was opened.
        }
    }

    Item{
        id: preferenceWatcher
        Connections{
            target: UM.Preferences
            function onPreferenceChanged(preference){
                manager.logMessage("shapeDialog UM.Preferences.onPreferenceChanged connection fired with preference " + preference)
                if (!race_condition_workaround){
                    return // I'm not doing a workaround
                }
                if (preference === "general/auto_slice"){
                    UM.Preferences.setValue("general/auto_slice", false) // If someone tries to change it, we don't want to let them
                }
            }
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

                property int clickCount: 0
                property Timer clickTimer: Timer {
                    interval: 300 // Adjust this value (in milliseconds)
                    running: false
                    repeat: false
                    onTriggered: {
                        shapeTypeTabShape.clickCount = 0
                    }
                }

                onClicked: {
                    if (currentShapeType !== shapeTypeShape){
                        manager.selectType(shapeTypeShape)
                        currentShapeType = shapeTypeShape
                    }
                    
                    clickCount++;
                    clickTimer.restart();
                    if (clickCount === 3){
                        manager.logMessage("Triple click!")
                        shapeDialog.toggleAltMode()
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

            UM.Label{
                id: autoSliceWarning
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                Layout.preferredHeight: implicitHeight
                Layout.row: 2
                Layout.column: 1
                Layout.columnSpan: 2
                Layout.fillWidth: true
                text: catalog.i18nc("dialog:workaround_warning", "<b>Automatic slicing has been disabled while this window is open to prevent Cura crashing due to a bug.</b>")
                visible: race_condition_workaround
                wrapMode: Text.WordWrap
                color: UM.Theme.getColor("error")
                horizontalAlignment: Text.AlignHCenter
                Layout.leftMargin: UM.Theme.getSize("default_margin").width
                Layout.rightMargin: UM.Theme.getSize("default_margin").width
                font.pointSize: 10
            }
        }

        ColumnLayout {
            id: tipLayout
            Layout.fillWidth: true
            visible: display_tip
            Layout.preferredHeight: implicitHeight
            
            UM.Label {
                id: transformTipText
                Layout.fillWidth: true
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                Layout.preferredHeight: implicitHeight
                wrapMode: Text.WordWrap
                color: UM.Theme.getColor("text")
                horizontalAlignment: Text.AlignHCenter
                Layout.leftMargin: UM.Theme.getSize("default_margin").width
                Layout.rightMargin: UM.Theme.getSize("default_margin").width
                font.pointSize: 12
                text: catalog.i18nc("dialog:transform_tip", "Don't forget that after you've created a shape you can move, scale, rotate and mirror it using Cura's own tools!")
            }
            RowLayout{
                Layout.fillWidth: true
                Layout.preferredHeight: implicitHeight

                Cura.TertiaryButton{
                    id: disableTipButton
                    Layout.alignment: Qt.AlignLeft | Qt.AlignVCenter
                    Layout.preferredHeight: implicitHeight
                    text: catalog.i18nc("dialog:disable_transform_tip", "Okay, don't tell me again.")
                    anchors.left: parent.left

                    onClicked: {manager.disableDisplayTip()}
                }

                Item {
                    Layout.fillWidth: true
                }
                Cura.TertiaryButton{
                    id: hideTipButton
                    Layout.alignment: Qt.AlignRight | Qt.AlignVCenter
                    Layout.preferredHeight: implicitHeight
                    text: catalog.i18nc("dialog:hide_transform_tip", "Cool, thanks!")
                    anchors.right: parent.right

                    onClicked: {manager.displayTip = false}
                }

            }
        }
    }
}