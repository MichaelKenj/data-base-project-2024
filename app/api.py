from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .db import SessionLocal
from .crud import create_car, get_cars, create_mechanic, get_mechanics, create_order, get_orders

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Автомобили
@router.post("/cars/")
def create_new_car(brand: str, license_plate: str, year: int, owner_name: str, db: Session = Depends(get_db)):
    return create_car(db, brand=brand, license_plate=license_plate, year=year, owner_name=owner_name)

@router.get("/cars/")
def read_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_cars(db, skip=skip, limit=limit)

# Автомеханики
@router.post("/mechanics/")
def create_new_mechanic(name: str, experience: int, rank: int, db: Session = Depends(get_db)):
    return create_mechanic(db, name=name, experience=experience, rank=rank)

@router.get("/mechanics/")
def read_mechanics(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_mechanics(db, skip=skip, limit=limit)

# Заказы
@router.post("/orders/")
def create_new_order(cost: float, issue_date, work_type: str, planned_end_date, car_id: int, mechanic_id: int, db: Session = Depends(get_db)):
    return create_order(
        db,
        cost=cost,
        issue_date=issue_date,
        work_type=work_type,
        planned_end_date=planned_end_date,
        car_id=car_id,
        mechanic_id=mechanic_id,
    )

@router.get("/orders/")
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_orders(db, skip=skip, limit=limit)
