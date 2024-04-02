from PySide6.QtCore import QSettings

def get_token():
    settings = QSettings("se_project", "the_market_nest")
    token = settings.value("auth/token", defaultValue=None)
    return token



    


if __name__ == "__main__":
    from fetch import APIClient

    api = APIClient("http://localhost:9000/api")

    def getUser():
        api_client = APIClient("http://localhost:9000/api")
        response = api_client.get_request(f"users/find/{get_token()}")

        return response 

    print(getUser())
    print(get_token())