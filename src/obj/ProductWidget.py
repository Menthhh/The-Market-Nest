from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy
from config import products
from utils.fetch import APIClient
from utils.token_retrieve import *


class ProductWidget(QWidget):
    clicked = Signal()
    def __init__(self, name, price, image_path, address, amount, _id, index_to_show, main_window):
        super(ProductWidget, self).__init__()
    
        self.id = _id

        self.main_window = main_window

        # Container widget
        container_widget = QWidget(self)

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

    def mousePressEvent(self, event):
        self.clicked.emit()

    def on_clicked(self):
        self.main_window.ui.stackedWidget.setCurrentIndex(self.index_to_show)

        # Update the label in index 5 based on the clicked product
        name = self.main_window.ui.product_name
        name.setText(self.name_label.text())
        price = self.main_window.ui.product_price
        price.setText(self.price_label.text() + "   THB")

        api_client = APIClient("http://localhost:9000/api")
        response = api_client.get_request(f"users/getUserFromProduct/{self.id}")
        print(response)
        sellername = response['username']

        response_product = api_client.get_request(f"products/find/{self.id}")
        print(response_product)

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
        # add image to the label with adjust size
        pixmap = QPixmap(self.image_label.pixmap())
        pixmap = pixmap.scaledToWidth(200, Qt.SmoothTransformation)
        pixmap = pixmap.scaledToHeight(200, Qt.SmoothTransformation)
        product_image.setPixmap(pixmap)

