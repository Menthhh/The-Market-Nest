from PySide6.QtWidgets import QDialog
from loginUi import Ui_Dialog
from config import account

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.pushButton.clicked.connect(self.handle_login)  # Connect the login button
        self.ui.signupLabel.mousePressEvent = self.signup_clicked  # Connect the signup label
        self.ui.cancelBtn.clicked.connect(self.setLogin)  # Connect the cancel button
        self.ui.signupConfirmBtn.clicked.connect(self.signupConfirm_clicked)  # Connect the signup confirm button

    def signup_clicked(self, event):
        self.ui.stackedWidget.setCurrentIndex(1)

        # Clear the input fields
        self.ui.usernameInput.clear()
        self.ui.emailInput.clear()
        self.ui.phoneInput.clear()
        self.ui.passInput.clear()
        self.ui.confirmPassInput.clear()

    def setLogin(self):
        self.ui.stackedWidget.setCurrentIndex(0)

        # Clear the input fields
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()

    def handle_login(self):
        # Placeholder for actual login logic
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        # prevent empty fields
        if username and password:
            # check if username exists
            if username in account:
                user_data = account[username]
                # check if password is correct
                if password == user_data["password"]:
                    print("Login successful")
                    self.accept()
                else:
                    print("Incorrect password")
            else:
                print("Username does not exist")

        else:
            print("Please fill in all fields")

    def signupConfirm_clicked(self):
        # Placeholder for actual signup logic
        username = self.ui.usernameInput.text()
        email = self.ui.emailInput.text()
        phone = self.ui.phoneInput.text()
        password = self.ui.passInput.text()
        confirm_password = self.ui.confirmPassInput.text()

        # prevent empty fields
        if not username or not email or not password or not confirm_password:
            print("Please fill in all fields")
            return
        
        # check if password and confirm password match
        if password != confirm_password:
            print("Passwords do not match")
            return
        
        # check if username already exists
        if username in account:
            print("Username already exists")
            return
        
        # add user to account
        account[username] = {
            "email": email,
            "phone": phone,
            "password": password
        }
        print("Account created successfully")
        print(account)
        self.setLogin()