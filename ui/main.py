import sys, os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6 import *
from pathlib import *
from PySide6.QtQuick import *
#import file lib

# import file in ui folder
from mainApp import Ui_MainWindow

class ProductWidget(QWidget):
    clicked = Signal()

    def __init__(self, name, price, image_path, index_to_show, main_window):
        super(ProductWidget, self).__init__()

        self.main_window = main_window

        layout = QVBoxLayout()

        # Add QLabel for product image
        image_label = QLabel()
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaledToWidth(80, Qt.SmoothTransformation)
        pixmap = pixmap.scaledToHeight(80, Qt.SmoothTransformation)
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)
        self.image_label = image_label
        # print(f"Image Label: {self.image_label}")            

        # Add QLabel for product name
        self.name_label = QLabel(f"{name}")
        layout.addWidget(self.name_label)

        # Add QLabel for product price
        self.price_label = QLabel(f"{price}")
        layout.addWidget(self.price_label)

        # Connect the click event to the function that changes the stackedWidget index
        self.index_to_show = index_to_show
        self.clicked.connect(self.on_clicked)

        self.setLayout(layout)

    def mousePressEvent(self, event):
        self.clicked.emit()

    def on_clicked(self):
        self.main_window.ui.stackedWidget.setCurrentIndex(self.index_to_show)

        # Update the label in index 5 based on the clicked product
        name = self.main_window.ui.product_name
        name.setText(self.name_label.text())
        price = self.main_window.ui.product_price
        price.setText(self.price_label.text())
        product_image = self.main_window.ui.product_img
        # add image to the label with adjust size
        pixmap = QPixmap(self.image_label.pixmap())
        pixmap = pixmap.scaledToWidth(200, Qt.SmoothTransformation)
        pixmap = pixmap.scaledToHeight(200, Qt.SmoothTransformation)
        product_image.setPixmap(pixmap)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)

        productlist_layout = QGridLayout(self.ui.productlist)

        # Example product data (replace with your actual product data)
        products = [
            {"name": "Product 1", "price": "$10.00", "image_path": "pics/product1.png"},
            {"name": "Product 2", "price": "$20.00", "image_path": "pics/spagetti.png"},
            {"name": "Product 3", "price": "$30.00", "image_path": "pics/spagetti.png"},
            {"name": "Product 4", "price": "$40.00", "image_path": "pics/spagetti.png"},
            {"name": "Product 5", "price": "$50.00", "image_path": "pics/spagetti.png"},
            {"name": "Product 6", "price": "$60.00", "image_path": "pics/spagetti.png"},
            {"name": "Product 7", "price": "$70.00", "image_path": "pics/spagetti.png"},
            {"name": "Product 8", "price": "$80.00", "image_path": "pics/spagetti.png"},
            {"name": "Product 9", "price": "$90.00", "image_path": "pics/spagetti.png"},
            {"name": "Product 10", "price": "$100.00", "image_path": "pics/spagetti.png"},
            {"name": "Product 11", "price": "$110.00", "image_path": "pics/spagetti.png"},
            {"name": "Product 12", "price": "$120.00", "image_path": "pics/spagetti.png"},
            {"name": "Product 13", "price": "$130.00", "image_path": "pics/spagetti.png"},
            # Add more products as needed
        ]
        row = 0
        col = 0
        for i, product_data in enumerate(products):
            product_widget = ProductWidget(product_data["name"], product_data["price"], product_data["image_path"], index_to_show=5, main_window=self)
            productlist_layout.addWidget(product_widget, row, col)
            col += 1
            if col == 4:
                col = 0
                row += 1

        self.ui.homeBtn_1.setChecked(True)

        self.ui.searchBtn_1.clicked.connect(self.on_search_btn_clicked)
        self.ui.profileBtn_1.clicked.connect(self.on_user_btn_clicked)
        self.ui.homeBtn_1.clicked.connect(self.on_home_btn_clicked)
        self.ui.homeBtn_2.clicked.connect(self.on_home_btn_clicked)
        self.ui.sellBtn_1.clicked.connect(self.sell_btn_clicked)

    #function for searching
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        search_text = self.ui.searchInput_1.text().strip()
        if search_text:
            self.ui.label_7.setText(search_text)

    #function for changing page to user page
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_home_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def sell_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    font_path = Path.joinpath(Path(__file__).parent, "fonts/JosefinSans-VariableFont_wght.ttf").as_posix()
    print(f"Font Path: {font_path}")
    if QFontDatabase.addApplicationFont(font_path) == -1:
        print("Font not found")
    else:
        print("Font found")
    stylesheet = open("styles.qss").read()
    app.setStyleSheet(stylesheet)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



        # Add label to the layout of self.ui.productlist
        # label = QLabel("Hello World")
        # label.setAlignment(Qt.AlignCenter)
        # productlist_layout.addWidget(label)