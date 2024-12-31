from sqlalchemy import or_
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text
from fastapi import HTTPException
from typing import Optional
from app.models import Car
from .models import Car, Mechanic, Order
from . import models
from datetime import date


# Функция для синхронизации последовательности
def sync_sequence(db: Session, table_name: str, id_column: str):
    db.execute(text(f"SELECT setval(pg_get_serial_sequence('{table_name}', '{id_column}'), COALESCE(MAX({id_column}), 1), MAX({id_column}) IS NOT NULL) FROM {table_name};"))
    db.commit()

#---------------CAR---------------
#---------------------------------
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

def search_cars(db: Session, query: str):
    return db.query(models.Car).filter(
        or_(
            models.Car.brand.ilike(f"%{query}%"),
            models.Car.license_plate.ilike(f"%{query}%"),
            models.Car.owner_name.ilike(f"%{query}%")
        )
    ).all()

def delete_car(db: Session, car_id: int):
    car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if car:
        db.delete(car)
        db.commit()
        return {"message": f"Car with id {car_id} deleted successfully"}
    else:
        return {"error": f"Car with id {car_id} not found"}
    
def edit_car(db: Session, car_id: int, brand: Optional[str] = None, license_plate: Optional[str] = None, 
             year: Optional[int] = None, owner_name: Optional[str] = None, color: Optional[str] = None):
    car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    
    if brand:
        car.brand = brand
    if license_plate:
        car.license_plate = license_plate
    if year:
        car.year = year
    if owner_name:
        car.owner_name = owner_name
    if color:
        car.color = color

    db.commit()
    db.refresh(car)
    return car

def get_cars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Car).offset(skip).limit(limit).all()
#---------------------------------

#------------MECHANIC-------------
#---------------------------------
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

def search_mechanics(db: Session, name: str):
    return db.query(models.Mechanic).filter(models.Mechanic.name.ilike(f"%{name}%")).all()

def delete_mechanic(db: Session, mechanic_id: int):
    mechanic = db.query(models.Mechanic).filter(models.Mechanic.id == mechanic_id).first()
    if mechanic:
        db.delete(mechanic)
        db.commit()
        return {"message": f"Mechanic with id {mechanic_id} deleted successfully"}
    else:
        return {"error": f"Mechanic with id {mechanic_id} not found"}

def edit_mechanic(db: Session, mechanic_id: int, name: Optional[str] = None, experience: Optional[int] = None, 
                  rank: Optional[int] = None):
    mechanic = db.query(models.Mechanic).filter(models.Mechanic.id == mechanic_id).first()
    if not mechanic:
        raise HTTPException(status_code=404, detail="Mechanic not found")
    
    if name:
        mechanic.name = name
    if experience:
        mechanic.experience = experience
    if rank:
        mechanic.rank = rank

    db.commit()
    db.refresh(mechanic)
    return mechanic

def get_mechanics(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Mechanic).offset(skip).limit(limit).all()
#---------------------------------


#-------------ORDER---------------
#---------------------------------
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

def search_orders(db: Session, work_type: str):
    return db.query(models.Order).filter(models.Order.work_type.ilike(f"%{work_type}%")).all()

def delete_order(db: Session, order_id: int):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if order:
        db.delete(order)
        db.commit()
        return {"message": f"Order with id {order_id} deleted successfully"}
    else:
        return {"error": f"Order with id {order_id} not found"}

def edit_order(db: Session, order_id: int, cost: Optional[float] = None, issue_date: Optional[date] = None, 
               work_type: Optional[str] = None, planned_end_date: Optional[date] = None, 
               car_id: Optional[int] = None, mechanic_id: Optional[int] = None):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    if cost:
        order.cost = cost
    if issue_date:
        order.issue_date = issue_date
    if work_type:
        order.work_type = work_type
    if planned_end_date:
        order.planned_end_date = planned_end_date
    if car_id:
        order.car_id = car_id
    if mechanic_id:
        order.mechanic_id = mechanic_id

    db.commit()
    db.refresh(order)
    return order

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Order).offset(skip).limit(limit).all()
#---------------------------------

#--------------USER---------------
#---------------------------------
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, name: str, email: str, hashed_password: str):
    user = models.User(name=name, email=email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
#---------------------------------