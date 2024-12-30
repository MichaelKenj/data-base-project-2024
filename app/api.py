from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .db import SessionLocal
from .crud import create_car, get_cars, create_mechanic, get_mechanics, create_order, get_orders
from .schemas import CarCreate, CarResponse, MechanicCreate, MechanicResponse, OrderCreate, OrderResponse

router = APIRouter()

# Dependency для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Автомобили
@router.post("/cars/", response_model=CarResponse)
def create_new_car(
    car: CarCreate = Depends(),  # JSON через Pydantic
    brand: str = Form(...),
    license_plate: str = Form(...),
    year: int = Form(...),
    owner_name: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        # Используем данные из формы, если car не передан в JSON
        if car:
            return create_car(db, **car.dict())
        return create_car(db, brand=brand, license_plate=license_plate, year=year, owner_name=owner_name)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Car with license plate '{license_plate}' already exists.",
        )

@router.get("/cars/", response_model=list[CarResponse])
def read_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_cars(db, skip=skip, limit=limit)

# Автомеханики
@router.post("/mechanics/", response_model=MechanicResponse)
def create_new_mechanic(
    mechanic: MechanicCreate = Depends(),  # JSON через Pydantic
    name: str = Form(...),
    experience: int = Form(...),
    rank: int = Form(...),
    db: Session = Depends(get_db)
):
    try:
        # Используем данные из формы, если mechanic не передан в JSON
        if mechanic:
            return create_mechanic(db, **mechanic.dict())
        return create_mechanic(db, name=name, experience=experience, rank=rank)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Mechanic with name '{name}' might already exist or violates constraints.",
        )

@router.get("/mechanics/", response_model=list[MechanicResponse])
def read_mechanics(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_mechanics(db, skip=skip, limit=limit)

# Заказы
@router.post("/orders/", response_model=OrderResponse)
def create_new_order(
    order: OrderCreate = Depends(),  # JSON через Pydantic
    cost: float = Form(...),
    issue_date: str = Form(...),
    work_type: str = Form(...),
    planned_end_date: str = Form(...),
    car_id: int = Form(...),
    mechanic_id: int = Form(...),
    db: Session = Depends(get_db)
):
    try:
        # Используем данные из формы, если order не передан в JSON
        if order:
            return create_order(db, **order.dict())
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

@router.get("/orders/", response_model=list[OrderResponse])
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_orders(db, skip=skip, limit=limit)
