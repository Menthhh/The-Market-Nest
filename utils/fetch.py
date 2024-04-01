import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def _handle_request_error(self, e, response=None):
        """Handle request errors and attempt to include server's error message."""
        error_msg = "Error:"
        if response is not None:
            try:
                # Attempt to include error details from response body if available
                server_error_info = response.json()
                return f"{error_msg} {e}. Server response: {server_error_info}"
            except ValueError:
                # In case the response body does not contain JSON
                pass
        return f"{error_msg} {e}"

    def post_request(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            return self._handle_request_error(e, response=e.response)

    def get_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return self._handle_request_error(e, response=e.response)

    def put_request(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.put(url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return self._handle_request_error(e, response=e.response)

    def delete_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.delete(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return self._handle_request_error(e, response=e.response)

            

# Example usage:
if __name__ == "__main__":
    api_client = APIClient("http://localhost:9000/api")

    
    body = {
    "name": "Alex Smith",
    "birthDate": "1988-12-09",
    "citizenID": 9876523410002,
    "phoneNumber": 9876543220,
    "email": "alex.smith@example.com",
    "username": "alexsmith",
    "password": "securePassword2"
  }


    response = api_client.post_request("users", body)
    print("POST Response:", response)

 