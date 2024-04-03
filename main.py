import sys, os
from turtle import right
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6 import *
from pathlib import *
from PySide6.QtQuick import *
from mainAppUi import Ui_MainWindow
from loginUi import Ui_Dialog  
from obj.LoginDialog import LoginDialog
from obj.ProductWidget import ProductWidget
from obj.FavouriteWidget import FavouriteWidget
from config import account, products, favourites
from obj.adminPage import AdminPage
from obj.mainPage import MainWindow

def show_login():
    login_dialog = LoginDialog()
    if login_dialog.exec() == QDialog.Accepted:
        if login_dialog.user_role == "admin":
            admin_page = AdminPage()
            admin_page.logout_requested.connect(show_login) 
            admin_page.show()
        else:
            main_window = MainWindow()
            main_window.logout_requested.connect(show_login) 
            main_window.show()
    else:
        app.quit()

import sys
import traceback

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)

        # Font and stylesheet setup
        font_path = Path.joinpath(Path(__file__).parent, "fonts/JosefinSans-VariableFont_wght.ttf").as_posix()
        QFontDatabase.addApplicationFont(font_path)
        stylesheet = open("styles.qss").read()
        app.setStyleSheet(stylesheet)

        print("Showing login dialog...")
        show_login()  # This initiates the login process.
        sys.exit(app.exec_())  # This starts the application's event loop.

    except Exception as e:
        print(f"An exception occurred: {e}")
        traceback.print_exc()
