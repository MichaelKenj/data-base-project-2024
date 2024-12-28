from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models import Car
from .models import Car, Mechanic, Order

# Автомобили
def create_car(db: Session, brand: str, license_plate: str, year: int, owner_name: str):
    new_car = Car(
        brand=brand,
        license_plate=license_plate,
        year=year,
        owner_name=owner_name,
    )
    try:
        db.add(new_car)
        db.commit()
        db.refresh(new_car)
        return new_car
    except IntegrityError:
        db.rollback()
        raise ValueError(f"Car with license plate '{license_plate}' already exists")

def get_cars(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Car).offset(skip).limit(limit).all()

# Автомеханики
def create_mechanic(db: Session, name: str, experience: int, rank: int):
    mechanic = Mechanic(name=name, experience=experience, rank=rank)
    db.add(mechanic)
    db.commit()
    db.refresh(mechanic)
    return mechanic

def get_mechanics(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Mechanic).offset(skip).limit(limit).all()

# Заказы
def create_order(db: Session, cost: float, issue_date, work_type: str, planned_end_date, car_id: int, mechanic_id: int):
    order = Order(
        cost=cost,
        issue_date=issue_date,
        work_type=work_type,
        planned_end_date=planned_end_date,
        car_id=car_id,
        mechanic_id=mechanic_id,
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def get_orders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Order).offset(skip).limit(limit).all()
