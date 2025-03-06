import QtQuick 6.0
import QtQuick.Controls 6.0

import UM 1.6 as UM

Rectangle {  // Base element
    Component.onCompleted: {
        manager.logMessage("ShapeListDelegate Component.onCompleted: modelData = " + modelData);
        defaultTooltipText = modelData.shapeData.tooltip;
        alternateTooltipText = modelData.shapeData.jokeTooltip;
        manager.logMessage("ShapeListDelegate Component.onCompleted: modelData.shapeData = " + modelData.shapeData);
        manager.logMessage("ShapeListDelegate Component.onCompleted: modelData.shapeData.tooltip = " + modelData.shapeData.tooltip);
        manager.logMessage("ShapeListDelegate Component.onCompleted: modelData.shapeData.jokeTooltip = " + modelData.shapeData.jokeTooltip);
    }

    // Background colours so I don't have to grab them from UM more than once.
    readonly property var normalBackground: UM.Theme.getColor("main_background")
    readonly property var hoverBackground: UM.Theme.getColor("expandable_hover")
    readonly property string tooltipKey: "tooltip"

    id: shapeDelegateRoot
    width: ListView.view.width
    height: 60  // Technically a magic number; I don't care
    color: normalBackground

    property var delegateClickedFunction: function(text){}
    property alias delegateText: textItem.text
    property string delegateImageSource: ""
    property string defaultTooltipText: modelData.shapeData.tooltip
    property string alternateTooltipText: modelData.shapeData.jokeTooltip
    //property string delegateTooltipText: alternateTooltipMode ? alternateTooltipText : defaultTooltipText

    property bool alternateTooltipMode: false

        // Listen for changes on the global property.
    Connections {
        target: shapeDialog
        function onGlobalAltShiftPressedChanged() {
            shapeDelegateRoot.alternateTooltipMode = shapeDialog.globalAltShiftPressed
            manager.logMessage("Delegate updated: alternateTooltipMode = " + shapeDelegateRoot.alternateTooltipMode)
        }
    }

    Image {
        id: shapeImage
        enabled: false
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.bottomMargin: 5
        anchors.topMargin: 2
        width: height
        source: delegateImageSource != "" ? Qt.resolvedUrl(delegateImageSource) : ""
        visible: delegateImageSource != ""
        fillMode: Image.PreserveAspectFit
        
    }

    /*UM.ToolTip {
        id: delegateTooltip
        text: delegateTooltipText
        visible: shapeDelegateMouseArea.containsMouse
        parent:delegateSeparator
        contentAlignment: UM.Enums.ContentAlignment.AlignRight
        //targetPoint: Qt.point(shapeDelegateRoot.x, shapeDelegateRoot.y + Math.round(shapeDelegateRoot.height * 1.25))
        enabled: false
    }*/

    UM.Label {
        id: textItem
        enabled: false
        anchors.verticalCenter: parent.verticalCenter
        anchors.left: shapeImage.right
        anchors.leftMargin: 10  // Adjust as required
        anchors.right: parent.right
        font.pixelSize: 16  // ^
        text: "I'm a delegate!"
        wrapMode: Text.WordWrap
    }


    Rectangle {  // Pretty separator
        id: delegateSeparator
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 3
        width: parent.width * 0.4
        height: 2
        color: UM.Theme.getColor("icon")
    }

    MouseArea {
        id: shapeDelegateMouseArea
        anchors.fill: parent
        hoverEnabled: true

        onClicked: {
            manager.logMessage("Current value of alternateTooltipMode: " + alternateTooltipMode)
            manager.logMessage("Delegate clicked: " + delegateText + " and delegateImageSource is " + delegateImageSource + " and shapeImage.source is " + shapeImage.source)
            manager.logMessage("On delegate click for " + delegateText + " ListView.view is currently: " + shapeDelegateRoot.ListView.view)
            shapeDelegateRoot.ListView.view.currentIndex = index
            delegateClickedFunction(delegateText)
        }

        onEntered: {
            shapeDelegateRoot.color = hoverBackground
        }

        onExited: {
            shapeDelegateRoot.color = normalBackground
        }

        ToolTip.text: alternateTooltipMode ? alternateTooltipText : defaultTooltipText
        ToolTip.visible: containsMouse && ToolTip.text !== ""
        ToolTip.delay: 500
    }
    

    /*ToolTip {
        id: delegateTooltip // Keep the same ID for consistency
        text: delegateTooltipText
        visible: text !== "" && shapeDelegateMouseArea.containsMouse // Visible property - reuse your condition
        parent: shapeDelegateMouseArea // Anchor it to the MouseArea
        x: shapeDelegateMouseArea.width // Adjust positioning as needed (start with right edge of MouseArea)
        y: 0 // Adjust vertical positioning as needed
        // background:  // Standard ToolTip might have default background, or you can customize if needed
        // contentItem: // Standard ToolTip usually uses a Text element internally
        // ... You can further customize font, color, etc., if needed, but let's start basic.
    }*/
}