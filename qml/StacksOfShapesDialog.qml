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

    property bool showShapeAddedBanner: false
    property bool shapeAddedBannerFading: false

    Rectangle {
        id: shapeAddedBanner
        visible: showShapeAddedBanner || shapeAddedBannerFading
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right
        height: 50
        color: UM.Theme.getColor("background_2")
        opacity: 1.0
        z: 1

        UM.Label {
            anchors.centerIn: parent
            text: catalog.i18nc("@shapelist:added_banner", "Shape added!")
            font.bold: true
            font.pointSize: 16
        }

        Timer {
            id: shapeAddedBannerTimer
            interval: 1000
            running: showShapeAddedBanner
            repeat: false
            onTriggered: {
                showShapeAddedBanner = false
                shapeAddedBannerFading = true
            }
        }

        NumberAnimation {
            target: shapeAddedBanner
            property: "opacity"
            from: 1.0
            to: 0.0
            duration: 500
            running: shapeAddedBannerFading
            onStopped: {
                shapeAddedBannerFading = false
                shapeAddedBanner.opacity = 1.0
            }
        }

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

            // In case Cura crashes or something the main plugin will use this to restore auto slicing at next startup
            UM.Preferences.setValue("stacksofshapes/restore_auto_slice", true)
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
            UM.Preferences.setValue("stacksofshapes/restore_auto_slice", false)
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


                ListView {
                    id: categoryListView
                    clip: true  // Overflowing the UI below sucks.
                    Layout.preferredWidth: 200
                    Layout.fillHeight: true
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
                        delegateClickedFunction: function(shapeName) {shapeDialog.showShapeAddedBanner = true; manager.loadModel(shapeName)}
                        defaultTooltipText: {
                            return modelData.shapeData[shapeDialog.tooltipKey];
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