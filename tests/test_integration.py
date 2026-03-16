import requests

BASE_URL = "http://127.0.0.1:5000"

def test_home():
    r = requests.get(f"{BASE_URL}/")
    assert r.status_code == 200
    assert r.text == "Hello World!"

def test_add_and_get_items():
    # Ajouter un item
    item = {"name": "Test Item"}
    r = requests.post(f"{BASE_URL}/items", json=item)
    assert r.status_code == 201
    assert "added" in r.json()["message"]

    # Vérifier que l'item est présent
    r = requests.get(f"{BASE_URL}/items")
    assert r.status_code == 200
    assert item in r.json()
