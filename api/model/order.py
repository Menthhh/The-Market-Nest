import persistent
import enum



class Order(persistent.Persistent):
    def __init__(self, userId: str, productId: str, quantity: int, price: int, status: str):
        self.senderId = senderId
        self.receiverId = receiverId
        self.productId = []
        self.shipDate = date
        self.shipmentStatus = status


