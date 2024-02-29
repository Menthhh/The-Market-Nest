import sys, os
from PySide6.QtWidgets import QMainWindow, QApplication, QStackedWidget
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6 import QtGui
from pathlib import Path
#import file lib



# import file in ui folder
from mainApp import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.homeBtn_1.setChecked(True)

        self.ui.searchBtn_1.clicked.connect(self.on_search_btn_clicked)
        self.ui.profileBtn_1.clicked.connect(self.on_user_btn_clicked)

    #function for searching
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        search_text = self.ui.searchInput_1.text().strip()
        if search_text:
            self.ui.label_7.setText(search_text)

    #function for changing page to user page
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(4)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # font_path_medium = os.path.abspath("fonts/JosefinSans-Medium.ttf")
     # font_path_weight = os.path.abspath("fonts/JosefinSans-VariableFont_wght")
    # font_path_regular = Path.joinpath(Path(__file__).parent, "fonts/JosefinSans-Regular.ttf")

    # font_id = QtGui.QFontDatabase.addApplicationFont(str(font_path_regular))

    # if font_id != -1:
    #     font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]
    #     app.setFont(QFont(font_family))
    #     print("Font found")
    # else:
    #     print("Font not found")

    font_path = Path.joinpath(Path(__file__).parent, "fonts/JosefinSans-VariableFont_wght.ttf").as_posix()
    print(f"Font Path: {font_path}")
    if QFontDatabase.addApplicationFont(font_path) == -1:
        print("Font not found")
    else:
        print("Font found")
    stylesheet = open("styles.qss").read()
    app.setStyleSheet(stylesheet)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())