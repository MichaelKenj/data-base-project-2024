import requests

BASE_URL = "http://127.0.0.1:8000"

def populate_cars():
    cars = [
        {"brand": "Toyota", "license_plate": "ABC123", "year": 2020, "owner_name": "John Doe"},
        {"brand": "Ford", "license_plate": "XYZ789", "year": 2018, "owner_name": "Jane Smith"},
        {"brand": "Tesla", "license_plate": "TES456", "year": 2022, "owner_name": "Elon Musk"},
    ]
    for car in cars:
        response = requests.post(
            f"{BASE_URL}/cars/form/",  # Убедитесь, что URL правильный
            data=car  # Отправляем данные как форму
        )
        if response.status_code == 200:
            print("Car added:", response.json())
        else:
            print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    populate_cars()
