from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy, QGridLayout
from config import products
from utils.fetch import APIClient
from utils.token_retrieve import *


class ProductWidget(QWidget):
    clicked = Signal()

    def __init__(self, name, price, image_path, address, amount, _id, index_to_show, main_window):
        super(ProductWidget, self).__init__()

        self.id = _id
        self.main_window = main_window

        # Set a fixed size for the widget
        self.setFixedSize(240, 310)

        # Container widget
        container_widget = QWidget()
        container_widget.setStyleSheet("""
            QWidget {
                background-color: #F0F0F0;
                border-radius: 10px;
            }
        """)
        container_layout = QGridLayout(container_widget)
        container_widget.setLayout(container_layout)

        # set margin for the container layout
        container_layout.setContentsMargins(20, 0, 0, 0) # (left, top, right, bottom)
        
        # QLabel for product image
        image_label = QLabel()
        image_label.setScaledContents(True)
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(180, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Adjusted for padding
        # set label fixed size
        image_label.setFixedSize(QSize(180, 150)) #(width, height)
        image_label.setPixmap(pixmap)
        image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        container_layout.addWidget(image_label, 0, 0, 1, 1)  # Row 0, Column 0

        # QLabel for product name
        name_label = QLabel(f"{name}")
        # set font size
        name_label.setStyleSheet("font: 500 12pt 'Josefin Sans Medium';")
        
        name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        container_layout.addWidget(name_label, 1, 0, 1, 1)  # Row 1, Column 0

        # QLabel for product price
        price_label = QLabel(f"{price} THB")
        price_label.setStyleSheet("font: 500 10pt 'Josefin Sans Medium';")
        price_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        container_layout.addWidget(price_label, 2, 0, 1, 1)  # Row 2, Column 0

        # Main layout for the widget
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(container_widget)
        self.setLayout(main_layout)

        # Connect the click event to the function that changes the stackedWidget index
        self.index_to_show = index_to_show
        self.clicked.connect(self.on_clicked)

    def mousePressEvent(self, event):
        self.clicked.emit()

    def on_clicked(self):
        self.main_window.ui.stackedWidget.setCurrentIndex(self.index_to_show)

        # Update the label in index 5 based on the clicked product
        # name = self.main_window.ui.product_name
        # name.setText(self.name_label.text())
        # price = self.main_window.ui.product_price
        # price.setText(self.price_label.text() + "   THB")

        api_client = APIClient("http://localhost:9000/api")
        response = api_client.get_request(f"users/getUserFromProduct/{self.id}")
        print(response)
        sellername = response['username']

        response_product = api_client.get_request(f"products/find/{self.id}")
        print(response_product)

        # set product name
        productName = self.main_window.ui.product_name
        productName.setText(response_product['title'])

        # set product price
        productPrice = self.main_window.ui.product_price
        productPrice.setText(str(response_product['price']) + " THB")

        #set emailLabel
        emailLabel = self.main_window.ui.emailLabel
        emailLabel.setText(response['email'])
        
        # set sellername to sellerNameLabel
        sellerNameLabel = self.main_window.ui.sellerNameLabel
        sellerNameLabel.setText(sellername)

        # set categoryLabel
        categoryLabel = self.main_window.ui.categoryLabel
        categoryLabel.setText(response_product['category'])

        # set addressLabel
        addressLabel = self.main_window.ui.addressLabel
        addressLabel.setText(response_product['address'])

        # set productDescLabel
        productDescLabel = self.main_window.ui.productDescLabel
        productDescLabel.setText(response_product['description'])

        # set phoneLabel
        phoneLabel = self.main_window.ui.phoneLabel
        phoneLabel.setText(str(response['phoneNumber']))
        
        product_image = self.main_window.ui.product_img
        # set label fixed size
        product_image.setFixedSize(QSize(150, 150)) #(width, height)
        # add image to the label with adjust size  
        pixmap = QPixmap(response_product['photos'][0])
 
        # set maximum width and height
        product_image.setPixmap(pixmap)
        product_image.setScaledContents(True)
        product_image.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        product_image.show()


