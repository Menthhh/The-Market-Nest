from PySide6.QtWidgets import QMainWindow, QVBoxLayout
from PySide6.QtCore import Qt
from adminUi import Ui_AdminWindow
from obj.LoginDialog import LoginDialog
from PySide6.QtCore import Signal
from utils.token_retrieve import UserManager
from obj.roundProgressBar import RoundProgressBar
from obj.categoryProgressBar import CategoryProgressBar

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
        self.user_manager = UserManager()
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

        #set up total acc
        self.ui.showTotalAcc.setText(str(self.user_manager.get_all_users()))

        # set up the progress bar into showBuySell frame
        self.progress_bar = RoundProgressBar(self)
        self.progress_bar.value = self.user_manager.get_user_with_product()
        self.progress_bar.text_format = "{value}% of the total account"
        self.progress_bar.progress_color = "#FFA500"
        self.progress_bar.enable_shadow = True
        self.progress_bar.show()
        self.ui.showBuySell.setLayout(QVBoxLayout())
        self.ui.showBuySell.layout().addWidget(self.progress_bar)

        # set up the progress bar into showAvg frame
        self.progress_bar = RoundProgressBar(self)
        self.progress_bar.value = self.user_manager.avg_product_per_user()
        self.progress_bar.text_format = "{value} products per user"
        self.progress_bar.progress_color = "#FFA500"
        self.progress_bar.enable_shadow = True
        self.progress_bar.show()
        self.ui.showAvgProduct.setLayout(QVBoxLayout())
        self.ui.showAvgProduct.layout().addWidget(self.progress_bar)

        # set up the progress bar into showCategory frame
        self.category_progress_bar = CategoryProgressBar(self)
        self.category_progress_bar_percentage = self.user_manager.get_product_category_percentage()
        self.category_progress_bar.set_categories(self.category_progress_bar_percentage)
        self.category_progress_bar.show()

        self.ui.categoryBar.setLayout(QVBoxLayout())
        self.ui.categoryBar.layout().addWidget(self.category_progress_bar)
        
        print(f'User count: {self.user_manager.get_all_users()}')
        print(f'Users with products: {self.user_manager.get_user_with_product()}')
        print(f'Avg. product count: {self.user_manager.avg_product_per_user()}')
        print(f'Product categories: {self.user_manager.get_product_category_percentage()}')

    # logout and show login dialog
    def logout(self):
        self.close()  # Close the admin page
        self.logout_requested.emit()  # Emit the logout signal

