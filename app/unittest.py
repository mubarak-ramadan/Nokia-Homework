from django.http import response
from fastapi.testclient import TestClient
from main import app 


client = TestClient(app)

test_meal = {
    "id": 1,
    "name" : "Gyros",
    "price" : 12.5,
    "ingredients": "bread, meat, veges",
    "spicy" : True,
    "vegan" : False,
    "gluten" : False,
    "description" : "Yummy",
    "kcal" : 2.5,
    "picture" : "www.jollof.com"
}

update_data = {
    "id": 1,
    "name" : "Rice",
    "price" : 20,
    "ingredients": "raw rice, meat, veges",
    "spicy" : True,
    "vegan" : True,
    "gluten" : False,
    "description" : "Yummy",
    "kcal" : 3.5,
    "picture" : "www.rice.com"
    }

#tests if creating a meal entry is successful
def test_create():
    response = client.post('/meals', json=test_meal)
    assert response.status_code == 200
    assert response.json == test_meal



#test if we can get all meals successfully
def test_get_all_meals():
    response = client.get('/meals', json=test_meal)
    assert response.status_code == 200
    assert response in response.json


#test if we can get a meal

def test_get_a_meal():
    #post the meal first and then get it
    response = client.post('/meals', json=test_meal)
    assert response.status_code == 200
    assert response.json == test_meal
    
    final_response = client.get('/meals/1')
    assert final_response.status_code == 200
    assert response.json == test_meal


def test_update_meal():
   response = client.put('/meals', json=update_data)

   assert response.status_code == 200
   assert response.json == update_data


def test_delete_meal():
    response = client.post('/meals', json=test_meal)
    assert response.status_code == 200
    assert response.json == test_meal
    
    final_response = client.delete('/meals/1')
    assert final_response.status_code == 200

