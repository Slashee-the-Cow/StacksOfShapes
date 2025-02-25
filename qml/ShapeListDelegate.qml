import QtQuick 6.0
import QtQuick.Controls 6.0

import UM 1.6 as UM

Rectangle {  // Base element
    // Background colours so I don't have to grab them from UM more than once.
    readonly property var normalBackground: UM.Theme.getColor("main_background")
    readonly property var hoverBackground: UM.Theme.getColor("expandable_hover")

    id: shapeDelegateRoot
    width: ListView.view.width
    height: 60  // Technically a magic number; I don't care
    color: normalBackground

    property var delegateClickedFunction: function(text){}
    property alias delegateText: textItem.text
    property string delegateImageSource: ""

    MouseArea {
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
    }

    UM.Label {
        id: textItem
        anchors.verticalCenter: parent.verticalCenter
        anchors.left: parent.left
        anchors.leftMargin: 10  // Adjust as required
        anchors.right: shapeImage.left
        font.pixelSize: 16  // ^
        text: "I'm a delegate!"
        wrapMode: Text.WordWrap
    }

    Image {
        id: shapeImage
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.right: parent.right
        anchors.bottomMargin: 5
        anchors.topMargin: 2
        anchors.rightMargin: 5
        width: height
        source: delegateImageSource != "" ? Qt.resolvedUrl(delegateImageSource) : ""
        visible: delegateImageSource != ""
        fillMode: Image.PreserveAspectFit
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