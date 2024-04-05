from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
 
 # what is parent=NOne in the constructor? : 
class ProductWidget(QWidget):
    def __init__(self, name, price, image_path, index_to_show, main_window):
        super(ProductWidget, self).__init__()
 
       
        