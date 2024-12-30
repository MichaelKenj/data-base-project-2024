from fastapi import APIRouter, Depends, HTTPException, Form, Body
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .db import SessionLocal
from .crud import create_car, create_mechanic, create_order, get_cars, get_mechanics, get_orders
from .schemas import CarCreate, CarResponse, MechanicCreate, MechanicResponse, OrderCreate, OrderResponse

router = APIRouter()

# Dependency для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Создание автомобиля через форму
@router.post("/cars/form/", response_model=CarResponse)
def create_new_car_form(
    brand: str = Form(...),
    license_plate: str = Form(...),
    year: int = Form(...),
    owner_name: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        return create_car(db, brand=brand, license_plate=license_plate, year=year, owner_name=owner_name)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Car with license plate '{license_plate}' already exists.",
        )

# Создание автомобиля через JSON
@router.post("/cars/", response_model=CarResponse)
def create_new_car_json(
    car: CarCreate = Body(...),  # Используем Body для JSON
    db: Session = Depends(get_db)
):
    try:
        return create_car(db, brand=car.brand, license_plate=car.license_plate, year=car.year, owner_name=car.owner_name)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Car with license plate '{car.license_plate}' already exists.",
        )

# Создание механика через форму
@router.post("/mechanics/form/", response_model=MechanicResponse)
def create_new_mechanic_form(
    name: str = Form(...),
    experience: int = Form(...),
    rank: int = Form(...),
    db: Session = Depends(get_db)
):
    try:
        return create_mechanic(db, name=name, experience=experience, rank=rank)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Mechanic with name '{name}' already exists.",
        )

# Создание механика через JSON
@router.post("/mechanics/", response_model=MechanicResponse)
def create_new_mechanic_json(
    mechanic: MechanicCreate = Body(...),  # Используем Body для JSON
    db: Session = Depends(get_db)
):
    try:
        return create_mechanic(db, name=mechanic.name, experience=mechanic.experience, rank=mechanic.rank)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Mechanic with name '{mechanic.name}' already exists.",
        )

# Создание заказа через форму
@router.post("/orders/form/", response_model=OrderResponse)
def create_new_order_form(
    cost: float = Form(...),
    issue_date: str = Form(...),
    work_type: str = Form(...),
    planned_end_date: str = Form(...),
    car_id: int = Form(...),
    mechanic_id: int = Form(...),
    db: Session = Depends(get_db)
):
    try:
        return create_order(
            db, cost=cost, issue_date=issue_date, work_type=work_type,
            planned_end_date=planned_end_date, car_id=car_id, mechanic_id=mechanic_id
        )
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Order violates constraints. Please check car_id or mechanic_id.",
        )

# Создание заказа через JSON
@router.post("/orders/", response_model=OrderResponse)
def create_new_order_json(
    order: OrderCreate = Body(...),  # Используем Body для JSON
    db: Session = Depends(get_db)
):
    try:
        return create_order(
            db, cost=order.cost, issue_date=order.issue_date, work_type=order.work_type,
            planned_end_date=order.planned_end_date, car_id=order.car_id, mechanic_id=order.mechanic_id
        )
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Order violates constraints. Please check car_id or mechanic_id.",
        )

# Чтение автомобилей
@router.get("/cars/", response_model=list[CarResponse])
def read_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_cars(db, skip=skip, limit=limit)

# Чтение механиков
@router.get("/mechanics/", response_model=list[MechanicResponse])
def read_mechanics(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_mechanics(db, skip=skip, limit=limit)

# Чтение заказов
@router.get("/orders/", response_model=list[OrderResponse])
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_orders(db, skip=skip, limit=limit)
