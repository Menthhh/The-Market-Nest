import requests
from fetch.fetch import *


data, loading, error = useFetch("http://localhost:9000/api/products/")



if loading == True:
    print("Loading...")
else:
    print(data)
    