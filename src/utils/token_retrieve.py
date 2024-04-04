from PySide6.QtCore import QSettings
from utils.fetch import APIClient
from math import floor

class UserManager:
    def __init__(self, base_url="http://localhost:9000/api"):
        self.api_client = APIClient(base_url)
        self.settings = QSettings("se_project", "the_market_nest")

    def get_token(self):
        return self.settings.value("auth/token", defaultValue=None)

    def get_user_detail(self, detail):
        token = self.get_token()
        if token:
            response = self.api_client.get_request(f"users/find/{token}")
            return response.get(detail)
        return None

    def get_username(self):
        return self.get_user_detail("username")

    def get_name(self):
        return self.get_user_detail("name")

    def get_user_id(self):
        return self.get_user_detail("_id")

    def get_birthdate(self):
        return self.get_user_detail("birthDate")

    def get_email(self):
        return self.get_user_detail("email")

    def get_phone_number(self):
        return self.get_user_detail("phoneNumber")

    def get_password(self):
        # Note: It's unusual and insecure to retrieve a user's password.
        return self.get_user_detail("password")

    def post_user(self, body):
        response = self.api_client.post_request("users", body)
        return response
    
    # get all users number
    def get_all_users(self):
        response = self.api_client.get_request("users")
        # count all users
        return len(response)
    
    # get user with product
    def get_user_with_product(self):
        response = self.api_client.get_request("users")
        users = []
        for user in response:
            if user["products"]:
                users.append(user["username"])
        return len(users)
    
    # avg product per user // only for acc with product
    def avg_product_per_user(self):
        response = self.api_client.get_request("users")
        get_user_with_product = self.get_user_with_product()
        total_product = 0
        for user in response:
            if user["products"]:
                total_product += len(user["products"])
        return floor(total_product / get_user_with_product)
    
    # get product category percentage of each propotion
    def get_product_category_percentage(self):
        response = self.api_client.get_request("products")
        total_product = len(response)
        category = {}
        for product in response:
            if product["category"] in category:
                category[product["category"]] += 1
            else:
                category[product["category"]] = 1
        for key in category:
            category[key] = (category[key] / total_product) * 100
        return category

    
