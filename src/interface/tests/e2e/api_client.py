import requests
from interface import config


class ManufacturingQualityAssuranceAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_all_products(self):
        url = f"{self.base_url}/products"
        response = requests.get(url)
        return response.json()

    def get_product(self, product_id):
        url = f"{self.base_url}/products/{product_id}"
        response = requests.get(url)
        return response.json()

    def create_product(self, name, description):
        url = f"{self.base_url}/products"
        data = {"name": name, "description": description}
        response = requests.post(url, json=data)
        return response.json()

    def update_product(self, product_id, name=None, description=None):
        url = f"{self.base_url}/products/{product_id}"
        data = {}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        response = requests.put(url, json=data)
        return response.json()

    def delete_product(self, product_id):
        url = f"{self.base_url}/products/{product_id}"
        response = requests.delete(url)
        return response.json()
