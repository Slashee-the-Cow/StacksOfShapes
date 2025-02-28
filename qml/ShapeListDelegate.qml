import QtQuick 6.0
import QtQuick.Controls 6.0

import UM 1.6 as UM

Rectangle {  // Base element
    Component.onCompleted: {
        manager.logMessage("ShapeListDelegate Component.onCompleted: modelData =" + modelData);
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
    property string delegateTooltipText: ""
    property bool delegateTooltipReposition: false


    MouseArea {
        id: shapeDelegateMouseArea
        anchors.fill: parent
        hoverEnabled: true

        onClicked: {
            // TBA
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

        UM.ToolTip {
           id: delegateTooltip
            text: delegateTooltipText
            visible: delegateTooltipText != "" && shapeDelegateMouseArea.containsMouse
        }
    }

    Binding {
        target: delegateTooltip
        property: "x"
        value: x + width
        when: delegateTooltipReposition
    }
    Binding {
        target: delegateTooltip
        property: "y"
        value: parent.y
        when: delegateTooltipReposition
    }

    Image {
        id: shapeImage
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

    UM.Label {
        id: textItem
        anchors.verticalCenter: parent.verticalCenter
        anchors.left: shapeImage.right
        anchors.leftMargin: 10  // Adjust as required
        anchors.right: parent.right
        font.pixelSize: 16  // ^
        text: "I'm a delegate!"
        wrapMode: Text.WordWrap
    }


    Rectangle {  // Pretty separator
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 3
        width: parent.width * 0.4
        height: 2
        color: UM.Theme.getColor("icon")
    }
}