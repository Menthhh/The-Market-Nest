from PySide6.QtWidgets import QMainWindow, QGridLayout, QWidget, QVBoxLayout, QLabel, QSizePolicy, QHBoxLayout, QApplication, QDialog
from PySide6.QtCore import Signal, QSize, Qt
from PySide6.QtGui import QPixmap
from obj.FavouriteWidget import FavouriteWidget
from obj.ProductWidget import ProductWidget
from config import products, favourites, item_categories
from mainAppUi import Ui_MainWindow
import tkinter as tk
from tkinter import filedialog



class MainWindow(QMainWindow):
    logout_requested = Signal()  # Add a logout signal

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
        self.products = products

        # Initial setup
        self.last_column_count = self.calculate_columns()
        self.adjust_columns()

                # Favourite list sample
        self.favourites = favourites

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
        self.ui.doneAddBtn_1.clicked.connect(self.addItem)
        self.ui.uploadPhotoBtn.clicked.connect(self.uploadPhoto)
        self.ui.productCategory.addItems(item_categories.keys())


    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

    def add_products(self, products):
        row = 0
        col = 0
        for i, product_data in enumerate(products):
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

    def add_favourites(self, favourites):
        for i, product_data in enumerate(favourites):
            product_widget = FavouriteWidget(product_data["name"], product_data["price"], product_data["image_path"], index_to_show=1, main_window=self)
            self.favourite_list_layout.addWidget(product_widget)

    def logout(self):
        # Perform necessary cleanup
        self.clear_layout(self.productlist_layout)
        self.clear_layout(self.favourite_list_layout)
        # Other cleanup operations...
        self.hide()  # Hide the main window
        self.logout_requested.emit()  # Emit the logout signal
    
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

        # Add products to the product list grid with the updated number of columns
        self.add_products(self.products)

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
        self.clear_layout(self.productlist_layout)

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
        self.clear_layout(self.favourite_list_layout)
        self.add_favourites(self.favourites)

    def on_editAccount_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)
        self.ui.stackedWidget_2.setCurrentIndex(0)

    def on_myProfile_btn_clicked(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)

    def on_manageAcc_btn_clicked(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)


    def addItem(self):
        # get the text from the input field
        self.ui.productTitle = self.ui.productTitleInput.text()
        self.ui.productCategory = self.ui.productCategoryInput.text()
        self.ui.productPrice = self.ui.productPriceInput.text()
        self.ui.productDesc = self.ui.productDescInput.text()
        # self.ui.productImage = self.ui.productImageInput.text()
        self.ui.productLocation = self.ui.productLocationInput.text()

        # create a dictionary of the input
        product = {
            "name": self.ui.productTitle,
            "price": self.ui.productPrice,
            "image_path": "images/placeholder.png",
            "category": self.ui.productCategory,
            "description": self.ui.product,
            "location": self.ui.productLocation
        }

        # add to db

        #clear the input fields
        self.ui.productTitleInput.clear()
        self.ui.productCategoryInput.clear()
        self.ui.productPriceInput.clear()
        self.ui.productDescInput.clear()
        self.ui.productLocationInput.clear()

        print("Item added successfully!")


    def uploadPhoto(self):
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        # Open a file dialog to select an image file
        image_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])

        