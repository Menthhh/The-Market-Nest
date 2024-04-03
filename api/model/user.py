import persistent

class User(persistent.Persistent):
    def __init__(self, name: str, birthDate: str, citizenID: int, phoneNumber: int, email: str, username: str, password: str):
        self.name = name
        self.isAdmin = False
        self.birthDate = birthDate
        self.citizenID = citizenID
        self.phoneNumber = phoneNumber
        self.email = email
        self.username = username
        self.password = password
        self.profilePicture = None
        self.products = []

    def addPicture(self, pictureURL: str):
        self.profilePicture = pictureURL

    def addProduct(self, productId: str):
        self.products.append(productId)

    def makeAdmin(self):
        self.isAdmin = True


