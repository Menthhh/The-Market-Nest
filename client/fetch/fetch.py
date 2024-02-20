import requests


data, loading, error = [], False,  False

def useFetch(urls):
    def fetchData(url):
        global data, loading, error
        loading = True
        try:    
            response = requests.get(url)
            data = response.json()

        except Exception as e:
            error = e

        loading = False
    fetchData(urls)
    return data, loading, error

def usePost(urls, body):
    def postData(url, body):
        global data, loading, error
        loading = True
        try:    
            response = requests.post(url, body)
            data = response.json()

        except Exception as e:
            error = e

        loading = False
    postData(urls, body)
    return data, loading, error

   