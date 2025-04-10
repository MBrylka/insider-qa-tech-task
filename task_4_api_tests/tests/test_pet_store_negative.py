import pytest


# POST endpoint
def test_add_pet_invalid_data(pet_service):
    response = pet_service.add_pet(None)
    assert response.status_code == 405

def test_add_pet_broken_json(pet_service):
    response = pet_service.add_pet({"id": "text"})
    assert response.status_code == 400


# PUT endpoint
def test_update_non_existing_pet(invalid_pet, pet_service):
    response = pet_service.update_pet(invalid_pet)
    assert response.status_code == 404

def test_update_invalid_data(pet_service):
    response = pet_service.update_pet(None)
    assert response.status_code == 405

def test_update_pet_broken_json(pet_service):
    response = pet_service.update_pet({"id": "text"})
    assert response.status_code == 400


# GET endpoint
def test_get_non_existing_pet(pet_service):
    response = pet_service.find_pet_by_id(999999)
    assert response.status_code == 404

def test_get_invalid_id(pet_service):
    response = pet_service.find_pet_by_id("text")
    assert response.status_code == 400


# DELETE endpoint
def test_delete_non_existing_pet(pet_service):
    response = pet_service.delete_pet(999999)
    assert response.status_code == 404

def test_delete_pet_invalid_id(pet_service):
    response = pet_service.delete_pet("text")
    assert response.status_code == 400