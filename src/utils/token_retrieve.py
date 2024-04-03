from PySide6.QtCore import QSettings
from fetch import APIClient

def get_token():
    settings = QSettings("se_project", "the_market_nest")
    token = settings.value("auth/token", defaultValue=None)
    return token

def get_username():# set username based on the token
    token = get_token()
    api_client = APIClient("http://localhost:9000/api")
    response = api_client.get_request(f"users/find/{get_token()}")
    return response["username"]

def get_user_name():# set username based on the token
    token = get_token()
    api_client = APIClient("http://localhost:9000/api")
    response = api_client.get_request(f"users/find/{get_token()}")
    return response["name"]

def get_user_id():# set username based on the token
    token = get_token()
    api_client = APIClient("http://localhost:9000/api")
    response = api_client.get_request(f"users/find/{get_token()}")
    return response["_id"]

def get_user_birthdate():# set username based on the token
    token = get_token()
    api_client = APIClient("http://localhost:9000/api")
    response = api_client.get_request(f"users/find/{get_token()}")
    return response["birthDate"]

def get_user_email():# set username based on the token
    token = get_token()
    api_client = APIClient("http://localhost:9000/api")
    response = api_client.get_request(f"users/find/{get_token()}")
    return response["email"]

def get_user_phone():# set username based on the token
    token = get_token()
    api_client = APIClient("http://localhost:9000/api")
    response = api_client.get_request(f"users/find/{get_token()}")
    return response["phoneNumber"]

def get_user_password():# set username based on the token
    token = get_token()
    api_client = APIClient("http://localhost:9000/api")
    response = api_client.get_request(f"users/find/{get_token()}")
    return response["password"]

def post_user(body):# set username based on the token
    api_client = APIClient("http://localhost:9000/api")
    response = api_client.post_request(f"users", body)
    return response

print(get_token())