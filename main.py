import sys, os
from turtle import right
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6 import *
from pathlib import *
from PySide6.QtQuick import *
# import file in ui folder
from mainAppUi import Ui_MainWindow
from loginUi import Ui_Dialog  # Import the login UI
from obj.LoginDialog import LoginDialog
from config import account
class ProductWidget(QWidget):

    clicked = Signal()
    def __init__(self, name, price, image_path, index_to_show, main_window):
        super(ProductWidget, self).__init__()

        self.main_window = main_window

        # Container widget
        container_widget = QWidget(self)
        container_widget.setStyleSheet(
            "border-radius: 5px;"
            "padding-top: 1px;"
        )
        container_widget.setObjectName("ContainerWidget")
        container_widget.setContentsMargins(0, 0, 0, 0)

        # Container layout
        container_layout = QVBoxLayout(container_widget)
        container_layout.setContentsMargins(0, 0, 0, 0)

        # Image container
        image_container = QWidget()
        image_container.setObjectName("ImageContainer")
        image_container_layout = QVBoxLayout(image_container)
        image_container_layout.setContentsMargins(0, 0, 0, 0)
        image_container.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))
        image_container.setMinimumSize(QSize(0, 200))

        # QLabel for product image
        image_label = QLabel()
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaledToWidth(200, Qt.SmoothTransformation)
        pixmap = pixmap.scaledToHeight(200, Qt.SmoothTransformation)
        image_label.setPixmap(pixmap)
        image_container_layout.addWidget(image_label)
        self.image_label = image_label
        container_layout.addWidget(image_container)

        # Name and price container
        name_price_container = QWidget()
        name_price_container_layout = QVBoxLayout(name_price_container)
        name_price_container_layout.setContentsMargins(0, 0, 0, 0)
        name_price_container.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))
        name_price_container.setMinimumSize(QSize(0, 100))

        # QLabel for product name
        self.name_label = QLabel(f"{name}")
        self.name_label.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))
        self.name_label.setContentsMargins(7, 0, 7, 0)
        name_price_container_layout.addWidget(self.name_label)

        # QLabel for product price
        self.price_label = QLabel(f"{price}")
        self.price_label.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))
        self.price_label.setContentsMargins(7, 0, 7, 0)
        name_price_container_layout.addWidget(self.price_label)

        container_layout.addWidget(name_price_container)

        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(container_widget)

        container_widget.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred))

        # Connect the click event to the function that changes the stackedWidget index
        self.index_to_show = index_to_show
        self.clicked.connect(self.on_clicked)

        self.setLayout(layout)

        # Set stylesheet for ProductWidget and ContainerWidget
        self.setStyleSheet("""
            #ContainerWidget {
                background-color: #ffffff;
                border: 1px solid #d4d4d4;
                border-radius: 5px;
                padding: 0px;
                margin: 0px;
            }              
        """)

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

class FavouriteWidget(QWidget):
    clicked = Signal()

    def __init__(self, name, price, image_path, index_to_show, main_window):
        
        super(FavouriteWidget, self).__init__()

        self.main_window = main_window

        layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        # Add QLabel for product image
        image_label = QLabel()
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaledToWidth(80, Qt.SmoothTransformation)
        pixmap = pixmap.scaledToHeight(80, Qt.SmoothTransformation)
        image_label.setPixmap(pixmap)
        left_layout.addWidget(image_label)
        self.image_label = image_label
        # print(f"Image Label: {self.image_label}")            

        # Add QLabel for product name
        self.name_label = QLabel(f"{name}")
        right_layout.addWidget(self.name_label)

        # Add QLabel for product price
        self.price_label = QLabel(f"{price}")
        right_layout.addWidget(self.price_label)

        # add left and right layout to main layout
        layout.addLayout(left_layout)
        layout.addLayout(right_layout)

        # Connect the click event to the function that changes the stackedWidget index
        self.index_to_show = index_to_show
        self.clicked.connect(self.on_clicked)

        # Check if the widget already has a layout
        if self.layout() is not None:
            # Remove the existing layout
            old_layout = self.layout()
            while old_layout.count():
                item = old_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

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
        self.ui.stackedWidget.setCurrentIndex(3)

        self.productlist_layout = QGridLayout(self.ui.productlist)
        self.favourite_list_layout = QGridLayout(self.ui.favoriteList)
        self.ui.stackedWidget.resizeEvent = self.resizeEvent

        # Example product data (replace with your actual product data)
        self.products = [
            {"name": "Product 1", "price": "$10.00", "image_path": "pics/spagetti.png"},
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

        # Initial setup
        self.last_column_count = self.calculate_columns()
        self.adjust_columns()

        row = 0
        col = 0
        for i, product_data in enumerate(self.products):
            product_widget = ProductWidget(product_data["name"], product_data["price"], product_data["image_path"], index_to_show=1, main_window=self)
            self.productlist_layout.addWidget(product_widget, row, col)
            col += 1
            if col == 4:
                col = 0
                row += 1

                # Favourite list sample
        self.favourites = [
            {"name": "Product 1", "price": "$10.00", "image_path": "pics/spagetti.png"},
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

        self.ui.homeBtn_1.setChecked(True)
        self.ui.searchBtn_1.clicked.connect(self.on_search_btn_clicked)
        self.ui.homeBtn_1.clicked.connect(self.on_home_btn_clicked)
        self.ui.homeBtn_2.clicked.connect(self.on_home_btn_clicked)
        self.ui.sellBtn_1.clicked.connect(self.sell_btn_clicked)
        self.ui.favBtn_1.clicked.connect(self.on_fav_btn_clicked)
        self.ui.favBtn_2.clicked.connect(self.on_fav_btn_clicked)
        self.ui.profileBtn_1.clicked.connect(self.on_profile_btn_clicked)
        self.ui.profileBtn_2.clicked.connect(self.on_profile_btn_clicked)
        self.ui.accountBtn_1.clicked.connect(self.on_editAccount_btn_clicked)
        self.ui.accountBtn_2.clicked.connect(self.on_editAccount_btn_clicked)
        self.ui.manageAccBtn_1.clicked.connect(self.on_manageAcc_btn_clicked)
        self.ui.myProfileBtn_1.clicked.connect(self.on_myProfile_btn_clicked)
        self.ui.exitBtn_1.clicked.connect(self.logout)
        self.ui.exitBtn_2.clicked.connect(self.logout)

    #logout and open login dialog
    def logout(self):
        self.hide()  # Hide the main window
        login_dialog = LoginDialog()
        if login_dialog.exec() == QDialog.Accepted:
            self.show()  # Show the main window again if login is successful
        else:
            QApplication.instance().quit()  # Exit the application if login is not successful

    
    #function for searching
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        search_text = self.ui.searchInput_1.text().strip()
        if search_text:
            self.ui.label_7.setText(search_text)

    #function for changing page to user page
    def on_profile_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def on_home_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        # clear all the widgets in the productlist layout without deleting the layout
        for i in reversed(range(self.productlist_layout.count())):
            self.productlist_layout.itemAt(i).widget().setParent(None)
        # Add products to the product list grid
        row = 0
        col = 0
        for i, product_data in enumerate(self.products):
            product_widget = ProductWidget(product_data["name"], product_data["price"], product_data["image_path"], index_to_show=1, main_window=self)
            self.productlist_layout.addWidget(product_widget, row, col)
            col += 1
            # set col based on the window size
            window_width = self.ui.stackedWidget.width()
            if window_width > 1000 and window_width < 1500:
                if col == 5:
                    col = 0
                    row += 1

            elif window_width > 1500:
                if col == 6:
                    col = 0
                    row += 1

            else:
                if col == 4:
                    col = 0
                    row += 1

    def resizeEvent(self, event):
        current_column_count = self.calculate_columns()

        # Check if the number of columns has changed
        if current_column_count != self.last_column_count:
            self.adjust_columns()
            self.last_column_count = current_column_count

        event.accept()

    def calculate_columns(self):
        window_width = self.ui.stackedWidget.width()

        # Define the number of columns based on window size
        if window_width > 1500:
            return 6
        elif 1000 < window_width <= 1500:
            return 5
        else:
            return 4

    def adjust_columns(self):
        current_column_count = self.calculate_columns()

        # Clear existing widgets in the layout
        for i in reversed(range(self.productlist_layout.count())):
            self.productlist_layout.itemAt(i).widget().setParent(None)

        # Add products to the product list grid with the updated number of columns
        row = col = 0
        for i, product_data in enumerate(self.products):
            product_widget = ProductWidget(product_data["name"], product_data["price"],
                                           product_data["image_path"], index_to_show=1, main_window=self)
            self.productlist_layout.addWidget(product_widget, row, col)

            col += 1
            if col == current_column_count:
                col = 0
                row += 1

    def sell_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_fav_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        # clear all the widgets in the favouriteList layout without deleting the layout
        for i in reversed(range(self.favourite_list_layout.count())):
            self.favourite_list_layout.itemAt(i).widget().setParent(None)
        # Add products to the favourite list vertically
        for i, product_data in enumerate(self.favourites):
            product_widget = FavouriteWidget(product_data["name"], product_data["price"], product_data["image_path"], index_to_show=1, main_window=self)
            self.favourite_list_layout.addWidget(product_widget)

    def on_editAccount_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)
        self.ui.stackedWidget_2.setCurrentIndex(0)

    def on_myProfile_btn_clicked(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)

    def on_manageAcc_btn_clicked(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_dialog = LoginDialog()
    font_path = Path.joinpath(Path(__file__).parent, "fonts/JosefinSans-VariableFont_wght.ttf").as_posix()
    # print(f"Font Path: {font_path}")
    if QFontDatabase.addApplicationFont(font_path) == -1:
        print("Font not found")
    else:
        print("Font found")
    stylesheet = open("styles.qss").read()
    app.setStyleSheet(stylesheet)

    if login_dialog.exec() == QDialog.Accepted:
        main_window = MainWindow()
        main_window.show()
        sys.exit(app.exec_())
    else:
        sys.exit(0)

        # Add label to the layout of self.ui.productlist
        # label = QLabel("Hello World")
        # label.setAlignment(Qt.AlignCenter)
        # productlist_layout.addWidget(label)