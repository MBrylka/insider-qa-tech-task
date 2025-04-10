import requests
from config import settings
from models.pet import Pet

class PetService:
    def __init__(self, base_url=None):
        self.base_url = base_url or settings.BASE_URL

    def add_pet(self, pet_data):
        url = f"{self.base_url}/pet"
        headers = {'Content-Type': 'application/json'}

        if isinstance(pet_data, Pet):
            json_payload = pet_data.__dict__
        elif isinstance(pet_data, dict):
            json_payload = pet_data
        else:
            json_payload = None

        return requests.post(url, json=json_payload, headers=headers)
    
    def update_pet(self, pet_data: Pet):
        url = f"{self.base_url}/pet"
        headers = {'Content-Type': 'application/json'}
        
        if isinstance(pet_data, Pet):
            json_payload = pet_data.__dict__
        elif isinstance(pet_data, dict):
            json_payload = pet_data
        else:
            json_payload = None

        return requests.put(url, json=json_payload, headers=headers)

    def delete_pet(self, pet_id: int):
        url = f"{self.base_url}/pet/{pet_id}"
        return requests.delete(url)

    def find_pet_by_id(self, id: int):
        url = f"{self.base_url}/pet/{id}"
        return requests.get(url)
