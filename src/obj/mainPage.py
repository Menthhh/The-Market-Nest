from PySide6.QtWidgets import QMainWindow, QGridLayout, QWidget, QVBoxLayout, QLabel, QSizePolicy, QHBoxLayout, QApplication, QDialog, QPushButton, QMessageBox, QFileDialog, QTableWidgetItem
from PySide6.QtCore import Signal, QSize, Qt
from PySide6.QtGui import QPixmap
from obj.FavouriteWidget import FavouriteWidget
from obj.ProductWidget import ProductWidget
from config import item_categories
from mainAppUi import Ui_MainWindow
from utils.fetch import APIClient
from utils.token_retrieve import *
from PySide6.QtWidgets import QLineEdit
from functools import partial
from obj.clickablewidget import ClickableWidget

from dotenv import load_dotenv
import os
load_dotenv()
UTILS = os.getenv("utils")
from pathlib import Path
module_dir = Path(UTILS)
import sys
sys.path.append(str(module_dir))

# Get the token
user_manager = UserManager()
api_client = APIClient("http://localhost:9000/api")
# TOKEN = user_manager.get_token()

class MainWindow(QMainWindow):
    logout_requested = Signal()  # Add a logout signal

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(3)


        self.productlist_layout = QGridLayout(self.ui.productlist)
        self.searchitemlist_layout = QGridLayout(self.ui.searchItemList)
        self.categoryproductlist_layout = QGridLayout(self.ui.categoryProductList)

        self.insert_product()

        self.ui.homeBtn_1.setChecked(True)
        self.ui.searchBtn_1.clicked.connect(self.on_search_btn_clicked)
        self.ui.homeBtn_1.clicked.connect(self.on_home_btn_clicked)
        self.ui.homeBtn_2.clicked.connect(self.on_home_btn_clicked)
        self.ui.sellBtn_1.clicked.connect(self.sell_btn_clicked)
        # self.ui.favBtn_1.clicked.connect(self.on_fav_btn_clicked)
        # self.ui.favBtn_2.clicked.connect(self.on_fav_btn_clicked)
        self.ui.profileBtn_1.clicked.connect(self.on_profile_btn_clicked)
        self.ui.profileBtn_2.clicked.connect(self.on_profile_btn_clicked)
        self.ui.accountBtn_1.clicked.connect(self.on_editAccount_btn_clicked)
        self.ui.accountBtn_2.clicked.connect(self.on_editAccount_btn_clicked)
        # self.ui.manageAccBtn_1.clicked.connect(self.on_manageAcc_btn_clicked)
        # self.ui.myProfileBtn_1.clicked.connect(self.on_myProfile_btn_clicked)
        self.ui.exitBtn_1.clicked.connect(self.logout)
        self.ui.exitBtn_2.clicked.connect(self.logout)
        self.ui.doneAddBtn_1.clicked.connect(self.addItem)
        self.ui.uploadPhotoBtn.clicked.connect(self.uploadPhoto)
        self.ui.productCategory.addItems(item_categories.keys())
        self.ui.cateProEdit.addItems(item_categories.keys())
        self.ui.cancelProEdit.clicked.connect(self.cancelEditProduct)
        self.ui.doneProEdit.clicked.connect(self.doneEditProduct)
        # self.ui.uploadEditImg.clicked.connect(self.uploadEditProduct)
        self.tempImageEdit = None

        #set banner

        # set the user info
        self.update_user_info()

        #my profile utils
        self.ui.changePassBtn.clicked.connect(self.changingPasswordPage)
        self.ui.cancelChangePass.clicked.connect(self.cancelChangePass)
        self.ui.confirmChangePass.clicked.connect(self.changePassword)
        self.ui.profileEditBtn.clicked.connect(self.editInfo)
        self.ui.cancelEdit.clicked.connect(self.cancelEdit)
        self.ui.confirmEdit.clicked.connect(self.confirmEdit)

        # add onclick to categories
        # QWidget electronics
        
        # self.ui.electronics.clicked.connect(self.electronics_clicked)
        self.ui.electronics = ClickableWidget(self.ui.electronics)
        self.ui.electronics.clicked.connect(self.electronics_clicked)
        self.ui.fashions = ClickableWidget(self.ui.fashions)
        self.ui.fashions.clicked.connect(self.fashion_clicked)
        self.ui.homeNgarden = ClickableWidget(self.ui.homeNgarden)
        self.ui.homeNgarden.clicked.connect(self.homeNgarden_clicked)
        self.ui.beautyNhealth = ClickableWidget(self.ui.beautyNhealth)
        self.ui.beautyNhealth.clicked.connect(self.beautyNhealth_clicked)
        self.ui.sports = ClickableWidget(self.ui.sports)
        self.ui.sports.clicked.connect(self.sports_clicked)
        self.ui.toysNgame = ClickableWidget(self.ui.toysNgame)
        self.ui.toysNgame.clicked.connect(self.toysNgames_clicked)
        self.ui.entertainment = ClickableWidget(self.ui.entertainment)
        self.ui.entertainment.clicked.connect(self.entertainment_clicked)
        self.ui.automative = ClickableWidget(self.ui.automative)
        self.ui.automative.clicked.connect(self.automative_clicked)
        self.ui.pet = ClickableWidget(self.ui.pet)
        self.ui.pet.clicked.connect(self.pet_clicked)
        self.ui.officesupplies = ClickableWidget(self.ui.officesupplies)
        self.ui.officesupplies.clicked.connect(self.officesupplies_clicked)
        self.ui.groceries = ClickableWidget(self.ui.groceries)
        self.ui.groceries.clicked.connect(self.groceries_clicked)
        self.ui.babyproducts = ClickableWidget(self.ui.babyproducts)
        self.ui.babyproducts.clicked.connect(self.babyproducts_clicked)
        self.ui.arts = ClickableWidget(self.ui.arts)
        self.ui.arts.clicked.connect(self.artsNcraft_clicked)
        self.ui.travel = ClickableWidget(self.ui.travel)
        self.ui.travel.clicked.connect(self.travel_clicked)
        self.ui.gift = ClickableWidget(self.ui.gift)
        self.ui.gift.clicked.connect(self.gift_clicked)

        #update my profile(product edit)
        self.ui.accountUsername.setText(user_manager.get_username())

        #init show all products
        # self.init_show_all_products()
        
        # widget table productEditTable
        self.init_table()

    def electronics_clicked(self):
        self.init_show_based_on_category("Electronics")
        self.ui.stackedWidget.setCurrentIndex(7)

    def fashion_clicked(self):
        self.init_show_based_on_category("Fashion")
        self.ui.stackedWidget.setCurrentIndex(7)

    def homeNgarden_clicked(self):
        self.init_show_based_on_category("Home and Gargen")
        self.ui.stackedWidget.setCurrentIndex(7)

    def beautyNhealth_clicked(self):
        self.init_show_based_on_category("Beauty and Health")
        self.ui.stackedWidget.setCurrentIndex(7)

    def sports_clicked(self):
        self.init_show_based_on_category("Sports and Outdoors")
        self.ui.stackedWidget.setCurrentIndex(7)

    def toysNgames_clicked(self):
        self.init_show_based_on_category("Toys and Games")
        self.ui.stackedWidget.setCurrentIndex(7)

    def entertainment_clicked(self):
        self.init_show_based_on_category("Entertainment")
        self.ui.stackedWidget.setCurrentIndex(7)

    def automative_clicked(self):
        self.init_show_based_on_category("Automative")
        self.ui.stackedWidget.setCurrentIndex(7)

    def pet_clicked(self):
        self.init_show_based_on_category("Pet Supplies")
        self.ui.stackedWidget.setCurrentIndex(7)

    def officesupplies_clicked(self):
        self.init_show_based_on_category("Office Supplies")
        self.ui.stackedWidget.setCurrentIndex(7)

    def groceries_clicked(self):
        self.init_show_based_on_category("Groceries")
        self.ui.stackedWidget.setCurrentIndex(7)

    def babyproducts_clicked(self):
        self.init_show_based_on_category("Baby Products")
        self.ui.stackedWidget.setCurrentIndex(7)

    def artsNcraft_clicked(self):
        self.init_show_based_on_category("Arts and Crafts")
        self.ui.stackedWidget.setCurrentIndex(7)

    def travel_clicked(self):
        self.init_show_based_on_category("Travel")
        self.ui.stackedWidget.setCurrentIndex(7)

    def gift_clicked(self):
        self.init_show_based_on_category("Personalized Gifts")
        self.ui.stackedWidget.setCurrentIndex(7)

    def init_show_all_products(self):
        response = api_client.get_request("products")
        print(response)
        products = response  # Assuming this is a list of products

        self.ui.productTable.setRowCount(len(products))
        self.ui.productTable.setColumnCount(3)  # Adjust based on the data you want to display
        self.ui.productTable.setHorizontalHeaderLabels(["Image", "Title", "Price"])

        for row, product in enumerate(products):
            # Image
            cell_widget = QWidget()
            layout = QHBoxLayout(cell_widget)
            img_label = QLabel()
            pixmap = QPixmap(product['photos'][0] if product['photos'] else 'path/to/default/image')
            img_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
            img_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(img_label)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            cell_widget.setLayout(layout)
            self.ui.productTable.setCellWidget(row, 0, cell_widget)

            # Title
            self.ui.productTable.setItem(row, 1, QTableWidgetItem(product['title']))

            # Price
            self.ui.productTable.setItem(row, 2, QTableWidgetItem(f"${product['price']}"))

        self.ui.productTable.resizeColumnsToContents()
        self.ui.productTable.resizeRowsToContents()

    def init_table(self):
        # Increase column count by one to accommodate the "Edit" button
        self.ui.productEditTable.setColumnCount(9)
        self.ui.productEditTable.setHorizontalHeaderLabels(["Img","Title", "Category", "Price", "Description", "Location", "Amount","ID", "Action"])
        self.ui.productEditTable.horizontalHeader().setStretchLastSection(True)
        account = user_manager.get_user_id()
        self.populate_table(account)

    def populate_table(self, account):
        response = api_client.get_request(f"users/find/{account}")
        products_id_list = response["products"]
        product_list = []

        for product_id in products_id_list:
            product = api_client.get_request(f"products/find/{product_id}")
            product_list.append(product)

        self.ui.productEditTable.setRowCount(len(product_list))

        for i, product in enumerate(product_list):
            img_label = QLabel()

            pixmap = QPixmap()
            # Check if 'photos' is a list and has at least one image
            if isinstance(product["photos"], list) and product["photos"]:
                # Attempt to load the first image in the list
                if pixmap.load(product["photos"][0]):
                    pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio)
                else:
                    print(f"Failed to load image: {product['photos'][0]}")
                    pixmap.load("src/assets/no_image.png")
                    pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio)
            else:
                # Load a default image if no images are provided
                pixmap.load("src/assets/no_image.png")
                pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio)

            img_label.setPixmap(pixmap)
            img_label.setAlignment(Qt.AlignCenter)
            self.ui.productEditTable.setCellWidget(i, 0, img_label)

            # Set other product details in the table
            self.ui.productEditTable.setItem(i, 1, QTableWidgetItem(product["title"]))
            self.ui.productEditTable.setItem(i, 2, QTableWidgetItem(product["category"]))
            self.ui.productEditTable.setItem(i, 3, QTableWidgetItem(str(product["price"])))
            self.ui.productEditTable.setItem(i, 4, QTableWidgetItem(product["description"]))
            self.ui.productEditTable.setItem(i, 5, QTableWidgetItem(product["address"]))
            self.ui.productEditTable.setItem(i, 6, QTableWidgetItem(str(product["amount"])))
            self.ui.productEditTable.setItem(i, 7, QTableWidgetItem(product["_id"]))


            # Add "Edit" button with click event
            btn_edit = QPushButton('Edit', self.ui.productEditTable)
            btn_edit.clicked.connect(partial(self.edit_product, i))
            self.ui.productEditTable.setCellWidget(i, 8, btn_edit)


    def edit_product(self, product):
        self.ui.stackedWidget_4.setCurrentIndex(1)
        self.ui.proTitleEdit.setText(self.ui.productEditTable.item(product, 1).text())
        self.ui.cateProEdit.setCurrentText(self.ui.productEditTable.item(product, 2).text())
        self.ui.priceProEdit.setText(self.ui.productEditTable.item(product, 3).text())
        self.ui.descProEdit.setPlainText(self.ui.productEditTable.item(product, 4).text())
        self.ui.locaProEdit.setText(self.ui.productEditTable.item(product, 5).text())
        self.ui.amountProEdit.setValue(int(self.ui.productEditTable.item(product, 6).text()))
        self.ui.deleteProduct.clicked.connect(partial(self.delete_product, self.ui.productEditTable.item(product, 7).text(), user_manager.get_user_id()))
        self.ui.uploadEditImg.clicked.connect(self.uploadEditProduct)

        # Get the image path from the table
        product_id = self.ui.productEditTable.item(product, 7).text()
        
        response = api_client.get_request(f"products/find/{product_id}")
        image_path = response["photos"][0]

        # Display the product image create label
        self.tempImageEdit = image_path
        self.imageLabelEdit = QLabel(self.ui.photoHolder)
        self.imageLabelEdit.setFixedSize(100, 100)
        pixmap = QPixmap(image_path)
        resized_pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.imageLabelEdit.setPixmap(resized_pixmap)
        self.imageLabelEdit.setAlignment(Qt.AlignCenter)
        self.imageLabelEdit.show()

    # QWidget photoHolder
    def uploadEditProduct(self):
        # clear the image label
        # Open a file dialog to select an image file
        image_path, _ = QFileDialog.getOpenFileName(self, "Select Image File", "",
                                                    "Image Files (*.jpg *.jpeg *.png *.gif)")

        
        if image_path:  # Check if a file was selected
            self.tempImageEdit = image_path  # Store the image path if you need to use it later
            
            # Initialize QLabel for image if it doesn't exist
            if not hasattr(self, 'imageLabelEdit') or not isinstance(self.imageLabelEdit, QLabel):
                self.imageLabelEdit = QLabel(self.ui.photoHolder)
                self.imageLabelEdit.setFixedSize(100, 100)

            pixmap = QPixmap(image_path)
            resized_pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.imageLabelEdit.setPixmap(resized_pixmap)
            self.imageLabelEdit.setAlignment(Qt.AlignCenter)
            self.imageLabelEdit.show()


    def cancelEditProduct(self):
        self.ui.stackedWidget_4.setCurrentIndex(0)

    # update product
    def doneEditProduct(self):
        # get the text from the input field
        self.productTitle = self.ui.proTitleEdit.text()
        # combo box
        self.productCategory = self.ui.cateProEdit.currentText()
        self.productPrice = self.ui.priceProEdit.text()
        self.productDesc = self.ui.descProEdit.toPlainText()
        self.productLocation = self.ui.locaProEdit.text()
        self.productAmount = self.ui.amountProEdit.value()
        self.productImage = self.tempImageEdit
        

        # create a dictionary of the input
        product = {
            "title": self.productTitle,
            "category": self.productCategory,
            "price": self.productPrice,
            "description": self.productDesc,
            "price": int(self.productPrice),
            "amount": int(self.productAmount),
            "address": self.productLocation,
            "user_id": user_manager.get_user_id(),
            "photos": [self.productImage]
        }

        for value in product.values():
            print(value)

        # update product not create a new one
        product_id = self.ui.productEditTable.item(self.ui.productEditTable.currentRow(), 7).text()
        response = api_client.put_request(f"products/{product_id}", product)
        print(f"response: {response}")

        # update the image
        if self.tempImageEdit:
            print(self.tempImageEdit)
            # 2 params product_id and user_id and body is image
            response = api_client.update_product_photo("products/images", product_id, user_manager.get_user_id(), self.tempImageEdit)

        self.ui.stackedWidget_4.setCurrentIndex(0)

        #clear photoHolder
        self.imageLabelEdit.clear()
        self.tempImageEdit = None

        #refresh the table
        self.refresh_table()

        QMessageBox.information(self, "Success", "Product edited successfully")

    def delete_product(self, product_id, user_id):
        response = api_client.delete_request(f"products/{product_id}/{user_id}")
        print(response)
        self.refresh_table()
        self.ui.stackedWidget_4.setCurrentIndex(0)
        

    def refresh_table(self):
        account = user_manager.get_user_id()
        self.populate_table(account)


    # ------------------ Handle editing user info // details ------------------
    def editInfo(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
        self.ui.nameEdit.setText(user_manager.get_name())
        self.ui.emailEdit.setText(user_manager.get_email())
        self.ui.phoneEdit.setText(str(user_manager.get_phone_number()))
        self.ui.birthEdit.setText(user_manager.get_birthdate())


    def confirmEdit(self):
        # get the text from the input field
        self.editName = self.ui.nameEdit.text()
        self.editEmail = self.ui.emailEdit.text()
        self.editPhone = self.ui.phoneEdit.text()
        self.editBirth = self.ui.birthEdit.text()


        # create a dictionary of the input
        user = {
            "name": self.editName,
            "email": self.editEmail,
            "phoneNumber": int(self.editPhone),
            "birthDate": self.editBirth
        }

        # access the data and change the user info
        user_id = user_manager.get_user_id()
        response = api_client.put_request(f"users/{user_id}", user)
        self.update_user_info()
        self.ui.stackedWidget_2.setCurrentIndex(0)
        # pop up message
        QMessageBox.information(self, "Success", "User info changed successfully")
        print(response)

    def cancelEdit(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
        

    # ------------------ Handle editing user info // changing password ------------------

    def cancelChangePass(self):
        self.ui.stackedWidget_3.setCurrentIndex(0)


    def changingPasswordPage(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
        self.ui.passLineEdit.clear()

    def changePassword(self):
        self.changedPass = self.ui.passLineEdit.text()

        # access the user id and change the password
        user_id = user_manager.get_user_id()
        body = {
            "password": self.changedPass
        }
        response = api_client.put_request(f"users/{user_id}", body)
        self.update_user_info()
        self.ui.stackedWidget_3.setCurrentIndex(0)
        # pop up message
        QMessageBox.information(self, "Success", "Password changed successfully")
        print(response)

    

    def update_user_info(self):
        # set the user info
        self.ui.showUsername.setText(user_manager.get_username())
        self.ui.showID.setText(user_manager.get_user_id())
        self.ui.showName.setText(user_manager.get_name())
        self.ui.showEmail.setText(user_manager.get_email())
        self.ui.showBirth.setText(user_manager.get_birthdate())
        self.ui.showPhone.setText(str(user_manager.get_phone_number()))
        self.ui.showPassword.setText(len(user_manager.get_password()) * "*")
        # set none
        self.tempImage = None 


    # ------------------ Handle adding item in the db products
    def insert_product(self):
        # reqest product data from the server
        response = api_client.get_request("products")
        products = response

        row = col = 0
        for i, product_data in enumerate(products):
            product_widget = ProductWidget(product_data["title"], product_data["price"],
                                           product_data["photos"][0], product_data["address"], product_data["amount"], product_data["_id"], index_to_show=1, main_window=self)
            self.productlist_layout.addWidget(product_widget, row, col)

            #add backgroud color to the widget

            col += 1
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
        # clear cookies
        user_manager.clear_cookies()
        self.close()  # Close the main window 
        # Emit the logout signal
        self.logout_requested.emit()

    
    #function for searching
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        # check if there is layout if yes do clear
        if self.searchitemlist_layout:
            self.clear_layout(self.searchitemlist_layout)
        search_text = self.ui.searchInput_1.text().strip()
        if search_text:
            self.ui.topicSearch.setText(search_text)
            self.init_search()

    def init_search(self):
        search_text = self.ui.searchInput_1.text().strip()
        response = api_client.get_request(f"products/search/{search_text}")
        print(response)
        products = response  # Assuming this is a list of products

        #totalItemFound QLabel
        self.ui.totalItemFound.setText(f"{len(products)} items found")
        

        row = col = 0
        for i, product_data in enumerate(products):
            product_widget = ProductWidget(product_data["title"], product_data["price"],
                                           product_data["photos"][0], product_data["address"], product_data["amount"], product_data["_id"], index_to_show=1, main_window=self)
            self.searchitemlist_layout.addWidget(product_widget, row, col)

            col += 1
            if col == 4:
                col = 0
                row += 1

        # insert  product to  layout using ProductWidget
    def init_show_based_on_category(self, category):
        # clear the layout
        self.clear_layout(self.categoryproductlist_layout)

        response = api_client.get_request(f"products/getProductFromCategory/{category}")
        print(response)
        products = response

        #searchCate QLabel
        self.ui.searchCate.setText(f"{category} category")

        #cateItemFound QLabel
        self.ui.cateItemFound.setText(f"{len(products)} items found")

        row = col = 0
        for i, product_data in enumerate(products):
            product_widget = ProductWidget(product_data["title"], product_data["price"],
                                           product_data["photos"][0], product_data["address"], product_data["amount"], product_data["_id"], index_to_show=1, main_window=self)
            self.categoryproductlist_layout.addWidget(product_widget, row, col)

            col += 1
            if col == 4:
                col = 0
                row += 1
        

    #function for changing page to user page
    def on_profile_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        # refresh the table
        self.refresh_table()

    def on_home_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        # clear all the widgets in the productlist layout without deleting the layout
        for i in reversed(range(self.productlist_layout.count())):
            self.productlist_layout.itemAt(i).widget().setParent(None)

        # Add products to the product list grid with the updated number of columns
        self.insert_product()

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
        # prouductAmount is a spinbox
        self.productAmount = self.ui.productAmount.value()

        # create a dictionary of the input
        product = {
            "title": self.productTitle,
            "category": self.productCategory,
            "price": self.productPrice,
            "description": self.productDesc,
            "price": int(self.productPrice),
            "amount": int(self.productAmount), 
            "address": self.productLocation,
            "user_id": user_manager.get_user_id(),
            "image_path": self.tempImage
        }

        for value in product.values():
            print(value)

        # add to db
        self.post_new_product(product)

        #refresh the table
        self.refresh_table()

        #clear the input fields
        self.ui.productTitle.clear()
        self.ui.productCategory.setCurrentIndex(0)
        self.ui.productPrice.clear()
        self.ui.productDesc.clear()
        self.ui.productLocation.clear()
        self.ui.productAmount.setValue(0)

        QMessageBox.information(self, "Success", "Product added successfully")

    def post_new_product(self, product):
        response = api_client.create_product_with_image("products", product["title"], product["category"], product["description"], product["price"], product["amount"], product["address"], product["user_id"], product["image_path"])
        print(f"response: {response}")

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
        # Open a file dialog to select an image file
        image_path, _ = QFileDialog.getOpenFileName(self, "Select Image File", "",
                                                    "Image Files (*.jpg *.jpeg *.png *.gif)")

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



            