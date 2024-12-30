import requests

BASE_URL = "http://127.0.0.1:8000"

# Отправка данных через форму
# def populate_cars_form():
#     cars = [
#         {"brand": "Toyota", "license_plate": "ABC123", "year": 2020, "owner_name": "John Doe"},
#         {"brand": "Ford", "license_plate": "XYZ789", "year": 2018, "owner_name": "Jane Smith"},
#         {"brand": "Tesla", "license_plate": "TES456", "year": 2022, "owner_name": "Elon Musk"},
#     ]
#     for car in cars:
#         response = requests.post(
#             f"{BASE_URL}/cars/form/",  # Эндпоинт для формы
#             data=car  # Отправляем данные как форму
#         )
#         if response.status_code == 200:
#             print("Car added:", response.json())
#         else:
#             print("Error:", response.status_code, response.text)

# Отправка данных через JSON
def populate_cars_json():
    cars = [
        {"brand": "Toyota", "license_plate": "33FG256", "year": 2020, "owner_name": "John Doe"},
        {"brand": "Ford", "license_plate": "45AS632", "year": 2018, "owner_name": "Jane Smith"},
        {"brand": "Tesla", "license_plate": "78FG235", "year": 2022, "owner_name": "Elon Musk"},
    ]
    for car in cars:
        response = requests.post(
            f"{BASE_URL}/cars/",  # Эндпоинт для JSON
            json=car  # Отправляем данные как JSON
        )
        if response.status_code == 200:
            print("Car added:", response.json())
        else:
            print("Error:", response.status_code, response.text)

# Пример для механиков и заказов (аналогично для каждого типа данных)
def populate_mechanics():
    mechanics = [
        {"name": "Alex", "experience": 10, "rank": 1},
        {"name": "Maria", "experience": 5, "rank": 2},
    ]
    for mechanic in mechanics:
        response = requests.post(f"{BASE_URL}/mechanics/", json=mechanic)  # JSON
        print(response.json())

def populate_orders():
    orders = [
        {"cost": 500.0, "issue_date": "2024-01-01", "work_type": "Repair", "planned_end_date": "2024-01-15", "car_id": 1, "mechanic_id": 1},
        {"cost": 200.0, "issue_date": "2024-01-02", "work_type": "Oil Change", "planned_end_date": "2024-01-05", "car_id": 2, "mechanic_id": 2},
    ]
    for order in orders:
        response = requests.post(f"{BASE_URL}/orders/", json=order)  # JSON
        print(response.json())

if __name__ == "__main__":
    #populate_cars_form()  # Для отправки формы
    #populate_cars_json()  # Для отправки JSON
    #populate_mechanics()
    #populate_orders()
    pass