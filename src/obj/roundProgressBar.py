from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QColor, Qt
from PySide6.QtCore import QRect

class RoundProgressBar(QWidget):
    def __init__(self, parent=None):
        super(RoundProgressBar, self).__init__(parent)
        self.value = 0
        self.width = 150
        self.height = 150
        self.progress_width = 10
        self.max_value = 100
        self.text_color = Qt.black
        self.progress_color = "#FFA500"
        self.text_format = "{value}%"  # Default text format

        self.resize(self.width, self.height)

    def set_value(self, value):
        self.value = value
        self.repaint()

    def set_text_format(self, format_str):
        """Set the text format for the progress bar.

        Args:
            format_str (str): The format string, which can include {value} as a placeholder for the progress value.
        """
        self.text_format = format_str
        self.repaint()

    def paintEvent(self, event):
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        full_circle = 360 * 16

        paint = QPainter(self)
        paint.setRenderHint(QPainter.Antialiasing)

        rect = QRect(0, 0, self.width, self.height)

        # Background circle
        remaining_pen = QPen(QColor("darkgray"), self.progress_width, Qt.SolidLine, Qt.RoundCap)
        paint.setPen(remaining_pen)
        paint.drawArc(margin, margin, width, height, 0, full_circle)

        # Foreground circle
        progress_pen = QPen(QColor(self.progress_color), self.progress_width, Qt.SolidLine, Qt.RoundCap)
        paint.setPen(progress_pen)
        value_angle = int(self.value * full_circle / self.max_value)
        paint.drawArc(margin, margin, width, height, -90 * 16, value_angle)

        # Text
        formatted_text = self.text_format.format(value=self.value)
        paint.setPen(QColor(self.text_color))
        paint.drawText(rect, Qt.AlignCenter, formatted_text)
