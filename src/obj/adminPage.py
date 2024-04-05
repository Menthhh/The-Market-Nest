from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QTableWidgetItem
from PySide6.QtCore import Qt
from adminUi import Ui_AdminWindow
from obj.LoginDialog import LoginDialog
from PySide6.QtCore import Signal
from utils.token_retrieve import UserManager
from obj.roundProgressBar import RoundProgressBar
from obj.categoryProgressBar import CategoryProgressBar
from functools import partial

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
        
        #initializa_acc_table
        self.initializa_acc_table()

        self.ui.dashBtn_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.dashBtn_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.mtnBtn_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.mtnBtn_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.admiBtn_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.admiBtn_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.logoutBtn_1.clicked.connect(self.logout)
        self.ui.logoutBtn_2.clicked.connect(self.logout)

        #set up total acc
        self.ui.showTotalAcc.setText(str(len(self.user_manager.get_all_users())))

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
        
        print(f'User count: {len(self.user_manager.get_all_users())}')
        print(f'Users with products: {self.user_manager.get_user_with_product()}')
        print(f'Avg. product count: {self.user_manager.avg_product_per_user()}')
        print(f'Product categories: {self.user_manager.get_product_category_percentage()}')

        #tableWidget
        # self.ui.accTableWid

    def initializa_acc_table(self):
        # Set column count and headers
        self.ui.accTableWid.setColumnCount(4)  # Adjust the number based on your data
        headers = ["Account ID", "Username", "Email", "Actions"]
        self.ui.accTableWid.setHorizontalHeaderLabels(headers)

        # Sample data retrieval - replace this with actual data fetching
        accounts = self.user_manager.get_all_users()

        # Populate the table with data
        self.populate_acc_table(accounts)

    def populate_acc_table(self, accounts):
        self.ui.accTableWid.setRowCount(len(accounts))

        for i, account in enumerate(accounts):
            self.ui.accTableWid.setItem(i, 0, QTableWidgetItem(account['_id']))
            self.ui.accTableWid.setItem(i, 1, QTableWidgetItem(account.get('username', '')))
            self.ui.accTableWid.setItem(i, 2, QTableWidgetItem(account.get('email', '')))

            delete_btn = QPushButton("Delete", self.ui.accTableWid)
            # Use partial to avoid the lambda capturing issue
            delete_btn.clicked.connect(partial(self.delete_account, account['_id']))
            self.ui.accTableWid.setCellWidget(i, 3, delete_btn)

    def delete_account(self, account_id, checked=False):  # checked is not used but necessary for signal
        print(f"Deleting account {account_id}")
        #delet product first
        self.user_manager.delete_user_product(account_id)
        self.user_manager.delete_user(account_id)
        # Refresh or update the table as needed
        self.refresh_table()

    def refresh_table(self):
        # Re-fetch the accounts and repopulate the table
        accounts = self.user_manager.get_all_users()
        self.populate_acc_table(accounts)
            
    # logout and show login dialog
    def logout(self):
        #clear cookies
        self.user_manager.clear_cookies()
        self.close()  # Close the admin page
        self.logout_requested.emit()  # Emit the logout signal

