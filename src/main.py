import sys
from PySide6.QtWidgets import QApplication, QDialog
from obj.LoginDialog import LoginDialog
from obj.adminPage import AdminPage
from obj.mainPage import MainWindow
import traceback
from PySide6.QtCore import QTimer
active_window = None  # Maintain a reference to the active window

from PySide6.QtCore import QTimer

def delayed_quit():
    if not active_window:
        print("No active window after delay, exiting application")
        app.quit()

def show_login():
    global active_window
    print("show_login called, active_window:", active_window)

    if active_window:
        print("Closing active window:", active_window)
        active_window.close()
        active_window = None

    login_dialog = LoginDialog()
    result = login_dialog.exec()
    print(f"Login dialog result: {result}, Logged in as: {login_dialog.username}")

    if result == QDialog.Accepted:
        print("Creating new window for user:", login_dialog.username)
        if login_dialog.username == "admin":
            admin_page = AdminPage()
            admin_page.logout_requested.connect(show_login)
            active_window = admin_page
            admin_page.show()
            print("AdminPage shown")
        else:
            main_window = MainWindow()
            main_window.logout_requested.connect(show_login)
            active_window = main_window
            main_window.show()
            print("MainWindow shown")
    else:
        print("Login dialog closed or canceled, checking active_window:", active_window)
        if not active_window:
            print("No active window, application will exit")
            QTimer.singleShot(100, app.quit)



if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        show_login()
        sys.exit(app.exec())
    except Exception as e:
        print("An error occurred.")
        print(e)
        print(traceback.format_exc())
