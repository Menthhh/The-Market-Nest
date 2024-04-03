from dotenv import load_dotenv
import os
load_dotenv()
UTILS = os.getenv("utils")
from pathlib import Path
module_dir = Path(UTILS)
import sys
sys.path.append(str(module_dir))

from fetch import APIClient
import unittest

product_id = "1eb41c30-6e5c-477c-8d87-e7d275ee8919"

api = APIClient("http://localhost:9000/api")


class TestProductAPI(unittest.TestCase):
    def test_product_details_api(self):
        products_details = api.get_request(f"products/find/{product_id}")
        self.assertEqual(products_details["title"], "Smartphone")
        self.assertEqual(products_details["category"], "Electronics")
        self.assertEqual(products_details["description"], "Latest Smartphone with Advanced Features")
        self.assertEqual(products_details["price"], 1000)
        self.assertEqual(products_details["amount"], 1)
        self.assertEqual(products_details["address"], "thailand")

    def test_product_image_api(self):
        product_picture = api.get_products_images("products/images", product_id)
        self.assertEqual(product_picture.status_code, 200)
        self.assertTrue(os.path.exists(f"pics/product_images/{product_id}.png"))


#ลองเรียกใช้
def save_image(path, product_id):
    FILE_PATH = Path(f"pics/product_images/{product_id}.png")
    product_picture = api.get_products_images("products/images", product_id)
    with open(FILE_PATH, "wb") as file:
        file.write(product_picture.content)
    return (product_picture.status_code, FILE_PATH)
  
def product_details(product_id):
    product_details = api.get_request(f"products/find/{product_id}")
    return product_details

def display():
    print("TestProductAPI")
    print("image", save_image("pics/product_images", product_id))
    print("details",product_details(product_id))


if __name__ == "__main__":
    display()
    unittest.main()





