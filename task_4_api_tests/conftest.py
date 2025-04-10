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

    # Removing test pet after the test
    pet_service.delete_pet(test_pet.id)
