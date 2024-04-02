from PySide6.QtWidgets import QMainWindow, QGridLayout, QWidget, QVBoxLayout, QLabel, QSizePolicy, QHBoxLayout, QApplication, QDialog, QPushButton, QMessageBox
from PySide6.QtCore import Signal, QSize, Qt
from PySide6.QtGui import QPixmap
from obj.FavouriteWidget import FavouriteWidget
from obj.ProductWidget import ProductWidget
from config import products, favourites, item_categories
from mainAppUi import Ui_MainWindow
import tkinter as tk
from tkinter import filedialog


from pathlib import Path
module_dir = Path(r"c:/Users/Tonkla/Desktop/The-Market-Nest/utils/")
import sys
sys.path.append(str(module_dir))
from token_retrieve import *
from fetch import APIClient

TOKEN = get_token()

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

        # set none
        self.tempImage = None 

    # ------------------ Handle adding item in the db to the widget ------------------
    def insert_product(self, products):
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

    
    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

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
        self.insert_product(self.products)

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

    # ------------------ Handle adding item for sell ------------------

    def addItem(self):
        # get the text from the input field
        self.productTitle = self.ui.productTitle.text()
        self.productCategory = self.ui.productCategory.currentText()
        self.productPrice = self.ui.productPrice.text()
        # AttributeError: 'PySide6.QtWidgets.QPlainTextEdit' object has no attribute 'text'
        self.productDesc = self.ui.productDesc.toPlainText()
        # self.productImage = self.ui.productImage.text()
        self.productLocation = self.ui.productLocation.text()

        # create a dictionary of the input
        product = {
            "title": self.productTitle,
            "category": self.productCategory,
            "description": self.productDesc,
            "price": int(self.productPrice),
            "amount": 1, 
            "address": self.productLocation,
            "user_id": TOKEN,
            "image_path": self.tempImage
        }

        for value in product.values():
            print(value)

        # add to db
        self.post_new_product(self, product)

        #clear the input fields
        self.ui.productTitle.clear()
        self.ui.productCategory.setCurrentIndex(0)
        self.ui.productPrice.clear()
        self.ui.productDesc.clear()
        self.ui.productLocation.clear()

        QMessageBox.information(self, "Success", "Product added successfully")

    def post_new_product(self, product):
        api_client = APIClient("http://localhost:9000/api")
        response = api_client.create_product_with_image("products", product["title"], product["category"], product["description"], product["price"], product["amount"], product["address"], product["user_id"], product["image_path"])
        print(response)

    def showRemoveButton(self, event):
        self.removeButton.move(self.imageLabel.width() - self.removeButton.width(), 0)  # Position button at the top-right
        self.removeButton.show()  # Show the button when the image is clicked

    def clearImage(self):
        self.imageLabel.clear()  # Clear the image
        self.tempImage = None  # Clear the stored image path
        self.removeButton.hide()  # Hide the remove button

    # clear all input fields when switching pages
    def clearInputs(self):
        # Clear the uploaded image
        if hasattr(self, 'imageLabel') and isinstance(self.imageLabel, QLabel):
            self.imageLabel.clear()
            self.tempImage = None  # Clear the stored image path
            if hasattr(self, 'removeButton') and isinstance(self.removeButton, QPushButton):
                self.removeButton.hide()  # Hide the remove button

        # Clear other input fields as needed
        # Example: self.ui.someInputField.clear()

    def switchPage(self):
        # This method should be called when changing pages
        self.clearInputs()
        # Add your code here to switch pages


    def uploadPhoto(self):
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        # Open a file dialog to select an image file
        image_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])

        if image_path:  # Check if a file was selected
            self.tempImage = image_path  # Store the image path if you need to use it later

            # Initialize QLabel for image if it doesn't exist
            if not hasattr(self, 'imageLabel') or not isinstance(self.imageLabel, QLabel):
                self.imageLabel = QLabel(self.ui.uploadedPic)
                self.imageLabel.setFixedSize(100, 100)

            # Initialize the button to remove the image
            if not hasattr(self, 'removeButton') or not isinstance(self.removeButton, QPushButton):
                self.removeButton = QPushButton('X', self.imageLabel)
                self.removeButton.clicked.connect(self.clearImage)
                self.removeButton.setFixedSize(20, 20)  # Small button size
                self.removeButton.hide()  # Hide the button initially

            pixmap = QPixmap(image_path)
            resized_pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.imageLabel.setPixmap(resized_pixmap)
            self.imageLabel.setAlignment(Qt.AlignCenter)
            
            # Show the remove button when the label is clicked
            self.imageLabel.mousePressEvent = self.showRemoveButton
            self.imageLabel.show()
 



            