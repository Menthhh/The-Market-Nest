from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

class ClickableWidget(QWidget):
    clicked = Signal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)
