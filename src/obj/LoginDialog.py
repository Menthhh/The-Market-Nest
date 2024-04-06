from PySide6.QtWidgets import QDialog, QMessageBox
from loginUi import Ui_Dialog
from config import account
from utils.fetch import APIClient
from PySide6.QtCore import QSettings

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
        # self.user_role = None  # This will hold the user's role
        self.username = None

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

        body = {
            "username": username,
            "name": name,
            "email": email,
            "phoneNumber": int(phone),
            "birthDate": birth,
            "citizenID": int(identi),
            "password": password,
        }

        self.siginup(body)
        

    def siginup(self, body):
        api_client = APIClient("http://localhost:9000/api")
        response = api_client.post_request("users", body)
        print(response)

        if response["message"] == "User created successfully":
            QMessageBox.information(self, "Success", response["message"])
            self.ui.stackedWidget.setCurrentIndex(0)

        else:
            QMessageBox.critical(self, "Error", response["message"])
            print(response)

    def get_token(self):
        settings = QSettings("se_project", "the_market_nest")
        token = settings.value("auth/token", defaultValue=None)
        return token

    def login(self, body):
        api_client = APIClient("http://localhost:9000/api")
        response = api_client.post_request("auth", body)

        if "token" in response:
            settings = QSettings("se_project", "the_market_nest")  
            settings.setValue("auth/token", response["token"])
            settings.sync()  

            print("Token from q setting",self.get_token())
            self.username = body["username"]
            self.accept()
        
        else:
            print(response)


  

        




       