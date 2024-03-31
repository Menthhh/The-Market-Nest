import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))
from fetch import fetch

data, loading, error = fetch.fetch_data_from_url("http://localhost:9000/api/products/")

if loading == True:
    print("Loading...")
else:
    for product in data:
        print(product["title"])


    