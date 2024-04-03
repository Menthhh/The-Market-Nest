from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap, Qt


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