import requests

data, loading, error = [], False, False

def fetch_data_from_url(url):
    global data, loading, error
    loading = True
    try:    
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        error = e
    loading = False
    return data, loading, error

def post_data_to_url(url, body):
    global data, loading, error
    loading = True
    try:    
        response = requests.post(url, body)
        data = response.json()
    except Exception as e:
        error = e
    loading = False
    return data, loading, error

def put_data_to_url(url, body):
    global data, loading, error
    loading = True
    try:    
        response = requests.put(url, body)
        data = response.json()
    except Exception as e:
        error = e
    loading = False
    return data, loading, error

def delete_data_from_url(url):
    global data, loading, error
    loading = True
    try:    
        response = requests.delete(url)
        data = response.json()
    except Exception as e:
        error = e
    loading = False
    return data, loading, error

