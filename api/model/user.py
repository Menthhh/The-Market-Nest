import persistent

class User(persistent.Persistent):
    def __init__(self, name: str, birthDate: str, citizenID: int, phoneNumber: int, email: str, username: str, password: str):
        self.name = name
        self.birthDate = birthDate
        self.citizenID = citizenID
        self.phoneNumber = phoneNumber
        self.email = email
        self.username = username
        self.password = password
        self.orders = []
        self.profilePicture = None
        self.products = []

    def addOrders(self, orderId: str):
        self.orders.append(orderId)

    def addPicture(self, pictureURL: str):
        self.profilePicture = pictureURL

    def addProduct(self, productId: str):
        self.products.append(productId)
