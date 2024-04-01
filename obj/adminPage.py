from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from adminUi import Ui_AdminWindow
from obj.LoginDialog import LoginDialog
from PySide6.QtCore import Signal

# AdminPage class as you defined, for admin-specific functionalities
class AdminPage(QMainWindow):
    logout_requested = Signal()  # Signal to indicate logout request
    def __init__(self):
        super(AdminPage, self).__init__()
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self)
        self.pageIndex = {
            0 : "dashboard",
            1 : "maintenance",
            2 : "administration",
        }
        self.ui.fullWid.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.dashBtn_2.setChecked(True)
        

        self.ui.dashBtn_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.dashBtn_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.mtnBtn_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.mtnBtn_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.admiBtn_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.admiBtn_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.logoutBtn_1.clicked.connect(self.logout)
        self.ui.logoutBtn_2.clicked.connect(self.logout)

    # logout and show login dialog
    def logout(self):
        self.close()  # Close the admin page
        self.logout_requested.emit()  # Emit the logout signal

