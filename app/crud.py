from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text
from fastapi import HTTPException
from typing import Optional
from app.models import Car
from .models import Car, Mechanic, Order
from . import models

# Функция для синхронизации последовательности
def sync_sequence(db: Session, table_name: str, id_column: str):
    db.execute(text(f"SELECT setval(pg_get_serial_sequence('{table_name}', '{id_column}'), COALESCE(MAX({id_column}), 1), MAX({id_column}) IS NOT NULL) FROM {table_name};"))
    db.commit()

# Автомобили
# Создание автомобиля
def create_car(db: Session, brand: str, license_plate: str, year: int, owner_name: str, color: Optional[str] = None):
    try:
        new_car = models.Car(
            brand=brand,
            license_plate=license_plate,
            year=year,
            owner_name=owner_name,
            color=color
        )
        db.add(new_car)
        db.commit()
        db.refresh(new_car)
        sync_sequence(db, 'cars', 'id')  # Синхронизируем последовательность для cars
        return new_car
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Car with license plate '{license_plate}' already exists."
        )


def get_cars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Car).offset(skip).limit(limit).all()

# Автомеханики
def create_mechanic(db: Session, name: str, experience: int, rank: int):
    try:
        mechanic = Mechanic(name=name, experience=experience, rank=rank)
        db.add(mechanic)
        db.commit()
        db.refresh(mechanic)
        sync_sequence(db, 'mechanics', 'id')  # Синхронизируем последовательность для mechanics
        return mechanic
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Mechanic with name '{name}' already exists."
        )

def get_mechanics(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Mechanic).offset(skip).limit(limit).all()

# Создание заказа
def create_order(db: Session, cost: float, issue_date, work_type: str, planned_end_date, car_id: int, mechanic_id: int):
    try:
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
        sync_sequence(db, 'orders', 'id')  # Синхронизируем последовательность для orders
        return order
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Order violates constraints. Please check car_id or mechanic_id."
        )

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Order).offset(skip).limit(limit).all()
  
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, name: str, email: str, hashed_password: str):
    user = models.User(name=name, email=email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

