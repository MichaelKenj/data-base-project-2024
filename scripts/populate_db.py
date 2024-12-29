import requests

BASE_URL = "http://127.0.0.1:8000"

def populate_data():
    # Пример данных
    cars = [
        {"brand": "Toyota", "license_plate": "ABC123", "year": 2015, "owner_name": "John"},
        {"brand": "Honda", "license_plate": "XYZ789", "year": 2018, "owner_name": "Alice"},
    ]

    for car in cars:
        response = requests.post(f"{BASE_URL}/cars/", json=car)
        if response.status_code == 201:
            print(f"Машина {car['brand']} успешно добавлена!")
        else:
            print(f"Ошибка: {response.status_code}, {response.json()}")

if __name__ == "__main__":
    populate_data()
