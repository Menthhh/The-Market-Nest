import sys
from PySide6.QtWidgets import QApplication, QDialog
from obj.LoginDialog import LoginDialog
from obj.adminPage import AdminPage
from obj.mainPage import MainWindow
import traceback

active_window = None  # Maintain a reference to the active window

def show_login():
    global active_window  # Refer to the global active_window

    if active_window:
        active_window.close()
        active_window = None

    login_dialog = LoginDialog()
    result = login_dialog.exec()
    if result == QDialog.Accepted:
        if login_dialog.username == "admin":
            admin_page = AdminPage()
            admin_page.logout_requested.connect(show_login)
            active_window = admin_page
            admin_page.show()
        else:
            main_window = MainWindow()
            main_window.logout_requested.connect(show_login)
            active_window = main_window
            main_window.show()
    else:
        if not active_window:
            app.quit()

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        show_login()
        sys.exit(app.exec())
    except Exception as e:
        print("An error occurred.")
        print(e)
        print(traceback.format_exc())
