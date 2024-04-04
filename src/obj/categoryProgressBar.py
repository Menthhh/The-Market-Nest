from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QColor, QFont, QPainterPath
from PySide6.QtCore import QRect, QPoint, Qt

class CategoryProgressBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.categories = {}
        self.colors = [
            'blue', 'green', 'red', 'yellow', 'purple', 'orange',
            'pink', 'brown', 'grey', 'violet', 'magenta', 'cyan',
            'olive', 'maroon', 'navy', 'lime', 'coral', 'beige',
            'mint', 'lavender'
        ]
        self.width = 300
        self.height = 350  # Increased height to accommodate labels
        self.setFixedSize(self.width, self.height)

    def set_categories(self, categories):
        self.categories = categories
        self.repaint()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        total_value = sum(self.categories.values())
        start_angle = 0
        rect = QRect(10, 10, self.width - 20, self.width - 20)  # Adjust for padding

        # Draw the pie chart
        for i, (category, value) in enumerate(self.categories.items()):
            proportion = (value / total_value) * 360
            color = QColor(self.colors[i % len(self.colors)])
            painter.setBrush(color)
            painter.drawPie(rect, int(start_angle * 16), int(proportion * 16))
            start_angle += proportion

        # Draw labels at the bottom
        painter.setFont(QFont('Arial', 10))
        y_position = self.width + 5  # Starting position for labels
        x_position = 10
        label_height = 15
        label_width = self.width // 4  # Four labels per row
        row_counter = 0

        for i, category in enumerate(self.categories.keys()):
            color = QColor(self.colors[i % len(self.colors)])
            painter.setBrush(color)
            painter.drawRect(x_position, y_position + (row_counter * label_height), 10, 10)  # Draw color box
            painter.setPen(QColor('black'))
            painter.drawText(x_position + 15, y_position + 10 + (row_counter * label_height), category)  # Draw text
            x_position += label_width
            if (i + 1) % 4 == 0:  # Move to the next row after every 4 labels
                x_position = 10
                row_counter += 1

