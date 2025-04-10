import pytest

def test_add_pet(pet, pet_service):
    response = pet_service.add_pet(pet)
    assert response.status_code == 200
    assert response.json()['name'] == pet.name
    assert response.json()['status'] == pet.status
    assert response.json()['id'] == pet.id
    assert response.json()['category'] == pet.category
    assert response.json()['photoUrls'] == pet.photoUrls
    assert response.json()['tags'] == pet.tags
    
    get_response = pet_service.find_pet_by_id(pet.id)
    assert get_response.status_code == 200
    assert get_response.json()['name'] == pet.name
    assert get_response.json()['status'] == pet.status
    assert get_response.json()['id'] == pet.id
    assert get_response.json()['category'] == pet.category
    assert get_response.json()['photoUrls'] == pet.photoUrls
    assert get_response.json()['tags'] == pet.tags

def test_update_pet(pet, pet_service):
    pet.name = "Updated Name"
    response = pet_service.update_pet(pet)
    assert response.status_code == 200

    get_response = pet_service.find_pet_by_id(pet.id)
    assert get_response.status_code == 200
    assert get_response.json()['name'] == pet.name
    assert get_response.json()['status'] == pet.status
    assert get_response.json()['id'] == pet.id
    assert get_response.json()['category'] == pet.category
    assert get_response.json()['photoUrls'] == pet.photoUrls
    assert get_response.json()['tags'] == pet.tags

def test_get_pet(pet, pet_service):
    get_response = pet_service.find_pet_by_id(pet.id)
    assert get_response.status_code == 200
    assert get_response.json()['name'] == pet.name
    assert get_response.json()['status'] == pet.status
    assert get_response.json()['id'] == pet.id
    assert get_response.json()['category'] == pet.category
    assert get_response.json()['photoUrls'] == pet.photoUrls
    assert get_response.json()['tags'] == pet.tags

def test_delete_pet(pet, pet_service):
    delete_response = pet_service.delete_pet(pet.id)
    assert delete_response.status_code == 200
    assert delete_response.json()['message'] == str(pet.id)
    assert delete_response.json()['code'] == 200
    assert delete_response.json()['type'] == "unknown"
    
    get_response = pet_service.find_pet_by_id(pet.id)
    assert get_response.status_code == 404