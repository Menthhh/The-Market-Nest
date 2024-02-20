from persistent import Persistent


class Product(Persistent):
    def __init__(self, title : str, category : str, description : str, price : int, amount : int):
        self.photos =[]
        self.title = title #String
        self.category = category #String
        self.description = description #String
        self.price = price
        self.amount = amount #int
        #self.weight = weight
        
    def get_photos(self):
        return self.photos
    
    def add_photo(self, photo_url):
        self.photos.append(photo_url)
    
    def get_title(self):
        return self.title
    
    def get_category(self):
        return self.category
    
    def get_description(self):
        return self.description
    
    def get_price(self):
        return self.price
    
    
    
    
        
        
        