import QtQuick 
import QtQuick.Controls 
import QtQuick.Layouts

ListView {
    anchors.fill: parent
    model: productModel.model

    delegate: Item {
        width: parent.width

        Rectangle {
            width: parent.width
            height: 80
            color: index % 2 === 0 ? "lightblue" : "lightgray"

            property int currentIndex: index // Assign the index to a property

            RowLayout {
                spacing: 10

                Image {
                    width: 60
                    height: 60
                    source: productModel.productDetails[currentIndex].image_path
                }

                ColumnLayout {
                    Text {
                        text: productModel.productDetails[currentIndex].name
                        font.bold: true
                    }
                    Text {
                        text: productModel.productDetails[currentIndex].price
                    }
                }
            }
        }
    }
}
