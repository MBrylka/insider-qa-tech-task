import requests
from config import settings
from models.pet import Pet

class PetService:
    def __init__(self, base_url=None):
        self.base_url = base_url or settings.BASE_URL

    def add_pet(self, pet_data: Pet):
        url = f"{self.base_url}/pet"
        headers = {'Content-Type': 'application/json'}
        return requests.post(url, json=pet_data.__dict__, headers=headers)

    def update_pet(self, pet_data: Pet):
        url = f"{self.base_url}/pet"
        headers = {'Content-Type': 'application/json'}
        return requests.put(url, json=pet_data.__dict__, headers=headers)

    def delete_pet(self, pet_id: int):
        url = f"{self.base_url}/pet/{pet_id}"
        return requests.delete(url)

    def find_pet_by_id(self, id: int):
        url = f"{self.base_url}/pet/{id}"
        return requests.get(url)
