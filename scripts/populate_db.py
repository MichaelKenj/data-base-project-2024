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
  {"brand": "BMW", "license_plate": "64TY927", "year": 2021, "owner_name": "Alice Cooper"},
  {"brand": "Chevrolet", "license_plate": "53AX672", "year": 2019, "owner_name": "Robert Brown"},
  {"brand": "Nissan", "license_plate": "39KR852", "year": 2020, "owner_name": "Michael Johnson"},
  {"brand": "Hyundai", "license_plate": "98SN234", "year": 2021, "owner_name": "David Lee"},
  {"brand": "Audi", "license_plate": "74GT832", "year": 2019, "owner_name": "Sarah Williams"},
  {"brand": "Mercedes", "license_plate": "10RX578", "year": 2020, "owner_name": "Chris Clark"},
  {"brand": "Honda", "license_plate": "41WL231", "year": 2021, "owner_name": "Linda Martinez"},
  {"brand": "Mazda", "license_plate": "53BT398", "year": 2018, "owner_name": "James Davis"},
  {"brand": "Kia", "license_plate": "75ZK491", "year": 2022, "owner_name": "Jessica Taylor"},
  {"brand": "Volkswagen", "license_plate": "29CV549", "year": 2019, "owner_name": "William Anderson"},
  {"brand": "Subaru", "license_plate": "18LR283", "year": 2020, "owner_name": "Elizabeth Wilson"},
  {"brand": "Jeep", "license_plate": "12YP167", "year": 2021, "owner_name": "Paul Thomas"},
  {"brand": "Ford", "license_plate": "36XZ229", "year": 2018, "owner_name": "Kevin Harris"},
  {"brand": "Chevrolet", "license_plate": "50WR551", "year": 2021, "owner_name": "Laura Walker"},
  {"brand": "Toyota", "license_plate": "89VC111", "year": 2020, "owner_name": "Daniel White"},
  {"brand": "BMW", "license_plate": "62FD673", "year": 2021, "owner_name": "Maria Lewis"},
  {"brand": "Mazda", "license_plate": "47BN832", "year": 2020, "owner_name": "William Young"},
  {"brand": "Nissan", "license_plate": "14TR238", "year": 2022, "owner_name": "Joseph Hall"},
  {"brand": "Honda", "license_plate": "31MN741", "year": 2019, "owner_name": "Monica Adams"},
  {"brand": "Audi", "license_plate": "65VX923", "year": 2020, "owner_name": "Richard Scott"},
  {"brand": "Hyundai", "license_plate": "27RM581", "year": 2022, "owner_name": "Barbara Green"},
  {"brand": "Mercedes", "license_plate": "10XY981", "year": 2021, "owner_name": "Thomas King"},
  {"brand": "Ford", "license_plate": "57PD261", "year": 2020, "owner_name": "Nancy Perez"},
  {"brand": "Chevrolet", "license_plate": "33VN742", "year": 2022, "owner_name": "Josephine Moore"},
  {"brand": "Toyota", "license_plate": "19BG674", "year": 2021, "owner_name": "Andrew Nelson"},
  {"brand": "BMW", "license_plate": "23QC798", "year": 2021, "owner_name": "Sophia Robinson"},
  {"brand": "Volkswagen", "license_plate": "91PT467", "year": 2020, "owner_name": "George Evans"},
  {"brand": "Kia", "license_plate": "62HP391", "year": 2021, "owner_name": "David Harris"},
  {"brand": "Mazda", "license_plate": "71EF250", "year": 2020, "owner_name": "Cynthia Carter"},
  {"brand": "Honda", "license_plate": "16KJ287", "year": 2022, "owner_name": "Emily Perry"},
  {"brand": "Audi", "license_plate": "85YT563", "year": 2021, "owner_name": "Chris Murphy"},
  {"brand": "Subaru", "license_plate": "44AQ276", "year": 2020, "owner_name": "Mary Morgan"},
  {"brand": "Toyota", "license_plate": "58BG845", "year": 2021, "owner_name": "David Edwards"},
  {"brand": "Kia", "license_plate": "49BZ527", "year": 2022, "owner_name": "Samuel Baker"},
  {"brand": "Volkswagen", "license_plate": "82NG420", "year": 2021, "owner_name": "Olivia Bell"},
  {"brand": "Ford", "license_plate": "35DX649", "year": 2019, "owner_name": "John Scott"},
  {"brand": "Chevrolet", "license_plate": "64HR930", "year": 2020, "owner_name": "Daniel Green"},
  {"brand": "Jeep", "license_plate": "28ZP136", "year": 2021, "owner_name": "Patricia Adams"},
  {"brand": "Subaru", "license_plate": "93NL501", "year": 2022, "owner_name": "Steven Baker"},
  {"brand": "Mazda", "license_plate": "44RU867", "year": 2021, "owner_name": "Gary Adams"},
  {"brand": "Toyota", "license_plate": "39BX470", "year": 2021, "owner_name": "Deborah Ross"},
  {"brand": "Nissan", "license_plate": "60PL873", "year": 2022, "owner_name": "Emily Harris"}
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
  {"name": "John", "experience": 12, "rank": 1},
  {"name": "Sophia", "experience": 7, "rank": 3},
  {"name": "Ethan", "experience": 6, "rank": 2},
  {"name": "Olivia", "experience": 3, "rank": 4},
  {"name": "Lucas", "experience": 15, "rank": 1},
  {"name": "Mia", "experience": 9, "rank": 3},
  {"name": "Isabella", "experience": 8, "rank": 2},
  {"name": "James", "experience": 14, "rank": 1},
  {"name": "Aiden", "experience": 4, "rank": 3},
  {"name": "Charlotte", "experience": 7, "rank": 2},
  {"name": "Amelia", "experience": 6, "rank": 4},
  {"name": "Benjamin", "experience": 11, "rank": 1},
  {"name": "Henry", "experience": 10, "rank": 2},
  {"name": "Mason", "experience": 5, "rank": 3},
  {"name": "Jack", "experience": 4, "rank": 4},
  {"name": "Harper", "experience": 3, "rank": 2},
  {"name": "Evan", "experience": 8, "rank": 1},
  {"name": "Emily", "experience": 6, "rank": 2},
  {"name": "Michael", "experience": 12, "rank": 1},
  {"name": "David", "experience": 9, "rank": 3},
  {"name": "Liam", "experience": 13, "rank": 1},
  {"name": "Ella", "experience": 5, "rank": 4},
  {"name": "Sebastian", "experience": 7, "rank": 2},
  {"name": "Eleanor", "experience": 10, "rank": 1},
  {"name": "Jackson", "experience": 4, "rank": 3},
  {"name": "Lily", "experience": 8, "rank": 2},
  {"name": "Maya", "experience": 6, "rank": 4},
  {"name": "Oscar", "experience": 3, "rank": 2},
  {"name": "Jack", "experience": 5, "rank": 1},
  {"name": "Grace", "experience": 11, "rank": 1},
  {"name": "Henry", "experience": 9, "rank": 3},
  {"name": "Zoe", "experience": 6, "rank": 4},
  {"name": "William", "experience": 14, "rank": 1},
  {"name": "Jackson", "experience": 8, "rank": 2},
  {"name": "James", "experience": 10, "rank": 3},
  {"name": "Daniel", "experience": 12, "rank": 1},
  {"name": "Sophia", "experience": 3, "rank": 2},
  {"name": "Levi", "experience": 7, "rank": 1},
  {"name": "Benjamin", "experience": 6, "rank": 4},
  {"name": "Carter", "experience": 5, "rank": 2},
  {"name": "Zoe", "experience": 10, "rank": 3},
  {"name": "John", "experience": 4, "rank": 2}
]

    for mechanic in mechanics:
        response = requests.post(f"{BASE_URL}/mechanics/", json=mechanic)  # JSON
        print(response.json())

def populate_orders():
    orders = [
  {"cost": 500.0, "issue_date": "2024-01-01", "work_type": "Repair", "planned_end_date": "2024-01-15", "car_id": 1, "mechanic_id": 1},
  {"cost": 200.0, "issue_date": "2024-01-02", "work_type": "Oil Change", "planned_end_date": "2024-01-05", "car_id": 2, "mechanic_id": 2},
  {"cost": 800.0, "issue_date": "2024-01-03", "work_type": "Brake Replacement", "planned_end_date": "2024-01-20", "car_id": 3, "mechanic_id": 1},
  {"cost": 300.0, "issue_date": "2024-01-04", "work_type": "Tire Rotation", "planned_end_date": "2024-01-10", "car_id": 4, "mechanic_id": 3},
  {"cost": 600.0, "issue_date": "2024-01-05", "work_type": "Suspension Repair", "planned_end_date": "2024-01-25", "car_id": 5, "mechanic_id": 2},
  {"cost": 250.0, "issue_date": "2024-01-06", "work_type": "Oil Change", "planned_end_date": "2024-01-12", "car_id": 6, "mechanic_id": 4},
  {"cost": 900.0, "issue_date": "2024-01-07", "work_type": "Transmission Repair", "planned_end_date": "2024-01-30", "car_id": 7, "mechanic_id": 5},
  {"cost": 400.0, "issue_date": "2024-01-08", "work_type": "Engine Overhaul", "planned_end_date": "2024-02-01", "car_id": 8, "mechanic_id": 6},
  {"cost": 500.0, "issue_date": "2024-01-09", "work_type": "Brake Replacement", "planned_end_date": "2024-01-15", "car_id": 9, "mechanic_id": 7},
  {"cost": 200.0, "issue_date": "2024-01-10", "work_type": "Tire Change", "planned_end_date": "2024-01-11", "car_id": 10, "mechanic_id": 8},
  {"cost": 550.0, "issue_date": "2024-01-11", "work_type": "Battery Replacement", "planned_end_date": "2024-01-20", "car_id": 11, "mechanic_id": 9},
  {"cost": 650.0, "issue_date": "2024-01-12", "work_type": "Transmission Repair", "planned_end_date": "2024-02-01", "car_id": 12, "mechanic_id": 10},
  {"cost": 300.0, "issue_date": "2024-01-13", "work_type": "Clutch Replacement", "planned_end_date": "2024-01-18", "car_id": 13, "mechanic_id": 11},
  {"cost": 450.0, "issue_date": "2024-01-14", "work_type": "Oil Change", "planned_end_date": "2024-01-20", "car_id": 14, "mechanic_id": 12},
  {"cost": 350.0, "issue_date": "2024-01-15", "work_type": "Engine Repair", "planned_end_date": "2024-01-25", "car_id": 15, "mechanic_id": 13},
  {"cost": 200.0, "issue_date": "2024-01-16", "work_type": "Brake Service", "planned_end_date": "2024-01-20", "car_id": 16, "mechanic_id": 14},
  {"cost": 600.0, "issue_date": "2024-01-17", "work_type": "Suspension Repair", "planned_end_date": "2024-01-30", "car_id": 17, "mechanic_id": 15},
  {"cost": 700.0, "issue_date": "2024-01-18", "work_type": "A/C Repair", "planned_end_date": "2024-01-25", "car_id": 18, "mechanic_id": 16},
  {"cost": 250.0, "issue_date": "2024-01-19", "work_type": "Tire Change", "planned_end_date": "2024-01-22", "car_id": 19, "mechanic_id": 17},
  {"cost": 800.0, "issue_date": "2024-01-20", "work_type": "Transmission Overhaul", "planned_end_date": "2024-02-05", "car_id": 20, "mechanic_id": 18},
  {"cost": 500.0, "issue_date": "2024-01-21", "work_type": "Exhaust Repair", "planned_end_date": "2024-01-30", "car_id": 21, "mechanic_id": 19},
  {"cost": 350.0, "issue_date": "2024-01-22", "work_type": "Radiator Repair", "planned_end_date": "2024-02-01", "car_id": 22, "mechanic_id": 20},
  {"cost": 900.0, "issue_date": "2024-01-23", "work_type": "Electrical Repair", "planned_end_date": "2024-02-10", "car_id": 23, "mechanic_id": 21},
  {"cost": 200.0, "issue_date": "2024-01-24", "work_type": "Oil Change", "planned_end_date": "2024-01-28", "car_id": 24, "mechanic_id": 22},
  {"cost": 650.0, "issue_date": "2024-01-25", "work_type": "Brake Fluid Change", "planned_end_date": "2024-02-05", "car_id": 25, "mechanic_id": 23},
  {"cost": 400.0, "issue_date": "2024-01-26", "work_type": "Starter Motor Replacement", "planned_end_date": "2024-02-01", "car_id": 26, "mechanic_id": 24},
  {"cost": 750.0, "issue_date": "2024-01-27", "work_type": "Headlight Repair", "planned_end_date": "2024-02-05", "car_id": 27, "mechanic_id": 25},
  {"cost": 600.0, "issue_date": "2024-01-28", "work_type": "Bodywork", "planned_end_date": "2024-02-10", "car_id": 28, "mechanic_id": 26},
  {"cost": 300.0, "issue_date": "2024-01-29", "work_type": "Window Repair", "planned_end_date": "2024-02-01", "car_id": 29, "mechanic_id": 27},
  {"cost": 500.0, "issue_date": "2024-01-30", "work_type": "Air Filter Replacement", "planned_end_date": "2024-02-05", "car_id": 30, "mechanic_id": 28}
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