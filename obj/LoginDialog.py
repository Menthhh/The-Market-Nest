from PySide6.QtWidgets import QDialog
from loginUi import Ui_Dialog
from config import account
from utils.fetch import APIClient

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

        body = {
            "username": username,
            "password": password
        }

        self.login(body)

    

    def signupConfirm_clicked(self):
        # Placeholder variables for the UI elements' text
        username = self.ui.usernameInput.text()
        name = self.ui.nameInput.text()
        email = self.ui.emailInput.text()
        phone = self.ui.phoneInput.text()
        birth = self.ui.birthInput.text()
        identi = self.ui.IdentiInput.text()
        password = self.ui.passInput.text()
        confirm_password = self.ui.confirmPassInput.text()

        from datetime import datetime
        original_date = datetime.strptime(birth, "%m/%d/%Y")
        new_date_str = original_date.strftime("%Y-%m-%d")


        body = {
            "username": username,
            "name": name,
            "email": email,
            "phoneNumber": int(phone),
            "birthDate": new_date_str,
            "citizenID": int(identi),
            "password": password,
        }

        self.siginup(body)
        

    def siginup(self, body):
        api_client = APIClient("http://localhost:9000/api")
        response = api_client.post_request("users", body)

        print(response)

    def login(self, body):
        api_client = APIClient("http://localhost:9000/api")
        response = api_client.post_request("auth", body)

        print(response)
  

        




       