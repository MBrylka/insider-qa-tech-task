import pytest
from services.pet_service import PetService
from models.pet import Pet

@pytest.fixture(scope="session")
def pet_service():
    return PetService()

@pytest.fixture(scope="session")
def pet():
    pet_service = PetService()    
    test_pet = Pet(id=123, name="Lightning", status="available", category={"id": 123, "name":"testCategory"}, photoUrls=["url1", "url2"], tags=[{"id": 123, "name":"testTag"}]) 
    yield test_pet
    pet_service.delete_pet(test_pet.id)

@pytest.fixture(scope="session")
def invalid_pet():
    pet_service = PetService()  
    test_pet = Pet(id=None, name=None, status="available", category={"id": 123, "name":"testCategory"}, photoUrls=None, tags=[{"id": 123, "name":"testTag"}]) 
    yield test_pet