from persistent import Persistent


class Product(Persistent):
    def __init__(self, title : str, category : str, description : str, price : int, amount : int, address : str, photos = None):
        self.photos = []
        self.title = title #String
        self.category = category #String
        self.description = description #String
        self.price = price
        self.amount = amount #int
        self.address = address
        self.photos = photos if photos is not None else []
    
    def addPhoto(self, photoURL):
        self.photos.append(photoURL)
        
    
    
    
    
        
        
        