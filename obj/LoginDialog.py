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
        self.ui.checkBoxOpt.clicked.connect(self.switchToPassport)
        self.user_role = None  # This will hold the user's role

    def switchToPassport(self):
        if self.ui.checkBoxOpt.isChecked():
            self.ui.IdentiLabel.setText("Passport Number")
        else:
            self.ui.IdentiLabel.setText("ID Number")

    def signup_clicked(self, event):
        self.ui.stackedWidget.setCurrentIndex(1)

        # Clear the input fields
        self.ui.usernameInput.clear()
        self.ui.nameInput.clear()
        self.ui.emailInput.clear()
        self.ui.phoneInput.clear()
        self.ui.birthInput.clear()
        self.ui.IdentiInput.clear()
        self.ui.passInput.clear()
        self.ui.confirmPassInput.clear()

    def setLogin(self):
        self.ui.stackedWidget.setCurrentIndex(0)

        # Clear the input fields
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()

    def handle_login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if username and password:
            if username in account:
                user_data = account[username]
                if password == user_data["password"]:
                    print("Login successful")
                    self.user_role = user_data.get("role", "user")  # Default to 'user' if role is not specified
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
        name = self.ui.nameInput.text()
        email = self.ui.emailInput.text()
        phone = self.ui.phoneInput.text()
        birth = self.ui.birthInput.text()
        identi = self.ui.IdentiInput.text()
        password = self.ui.passInput.text()
        confirm_password = self.ui.confirmPassInput.text()


        # prevent empty fields
        if not username or not email or not password or not confirm_password or not phone or not birth or not identi:
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
        
        # if passport number
        if self.ui.checkBoxOpt.isChecked():
            account[username] = {
                "name": name,
                "email": email,
                "phone": phone,
                "birth": birth,
                "nationalId": "N/A",
                "passport": identi,
                "password": password
            }
        else:
            account[username] = {
                "name": name,
                "email": email,
                "phone": phone,
                "birth": birth,
                "nationalId": identi,
                "passport": "N/A",
                "password": password
            }

        print("Account created successfully")
        print(account)
        self.setLogin()