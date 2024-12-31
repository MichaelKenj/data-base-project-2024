from fastapi import APIRouter, Depends, HTTPException, Form, Body
from fastapi import Query
from datetime import date
from sqlalchemy.orm import Session
from .models import Car, Mechanic, Order
from sqlalchemy.exc import IntegrityError
from typing import Optional
from .db import SessionLocal
from .schemas import CarCreate, CarResponse, MechanicCreate, MechanicResponse, OrderCreate, OrderResponse
from .crud import (
    create_car, create_mechanic, create_order,
    get_cars, get_mechanics, get_orders,
    search_cars, search_mechanics, search_orders, 
    delete_car, delete_mechanic, delete_order,
    edit_car, edit_mechanic, edit_order 
)

router = APIRouter()

# Dependency для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#----------------------------------CAR-----------------------------------
#------------------------------------------------------------------------
@router.post("/cars/form/", response_model=CarResponse)
def create_new_car_form(
    brand: str = Form(...),
    license_plate: str = Form(...),
    year: int = Form(...),
    owner_name: str = Form(...),
    color: Optional[str] = None,
    db: Session = Depends(get_db)
):
    try:
        return create_car(db, brand=brand, license_plate=license_plate, year=year, owner_name=owner_name, color=color)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Car with license plate '{license_plate}' already exists.",
        )

@router.post("/cars/", response_model=CarResponse)
def create_new_car_json(
    car: CarCreate = Body(...),  # Используем Body для JSON
    db: Session = Depends(get_db)
):
    try:
        return create_car(db, brand=car.brand, license_plate=car.license_plate, year=car.year, owner_name=car.owner_name, color=car.color)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Car with license plate '{car.license_plate}' already exists.",
        )

@router.get("/cars/search")
def search_cars_api(search_key: str, search_value: str, db: Session = Depends(get_db)):
    if search_key == "brand":
        result = db.query(Car).filter(Car.brand == search_value).all()
    else:
        result = []
    return result

@router.delete("/cars/{car_id}/")
def delete_car_api(car_id: int, db: Session = Depends(get_db)):
    result = delete_car(db, car_id=car_id)
    return result

@router.put("/cars/{car_id}/", response_model=CarResponse)
def edit_car_api(
    car_id: int, 
    brand: Optional[str] = None, 
    license_plate: Optional[str] = None, 
    year: Optional[int] = None, 
    owner_name: Optional[str] = None, 
    color: Optional[str] = None, 
    db: Session = Depends(get_db)
):
    try:
        return edit_car(db, car_id, brand, license_plate, year, owner_name, color)
    except HTTPException as e:
        raise e

@router.get("/cars/", response_model=list[CarResponse])
def read_cars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_cars(db, skip=skip, limit=limit)
#------------------------------------------------------------------------


#-------------------------------MECHANIC---------------------------------
#------------------------------------------------------------------------
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

@router.get("/mechanics/search/")
def search_mechanics_route(name: str, db: Session = Depends(get_db)):
    return search_mechanics(db, name=name)

@router.delete("/mechanics/{mechanic_id}")
def delete_mechanic_route(mechanic_id: int, db: Session = Depends(get_db)):
    return delete_mechanic(db, mechanic_id=mechanic_id)

@router.put("/mechanics/{mechanic_id}/", response_model=MechanicResponse)
def edit_mechanic_api(
    mechanic_id: int, 
    name: Optional[str] = None, 
    experience: Optional[int] = None, 
    rank: Optional[int] = None, 
    db: Session = Depends(get_db)
):
    try:
        return edit_mechanic(db, mechanic_id, name, experience, rank)
    except HTTPException as e:
        raise e

@router.get("/mechanics/", response_model=list[MechanicResponse])
def read_mechanics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_mechanics(db, skip=skip, limit=limit)
#------------------------------------------------------------------------


#---------------------------------ORDER----------------------------------
#------------------------------------------------------------------------
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

@router.get("/orders/search/")
def search_orders_route(work_type: str, db: Session = Depends(get_db)):
    return search_orders(db, work_type=work_type)

@router.delete("/orders/{order_id}")
def delete_order_route(order_id: int, db: Session = Depends(get_db)):
    return delete_order(db, order_id=order_id)

@router.put("/orders/{order_id}/", response_model=OrderResponse)
def edit_order_api(
    order_id: int, 
    cost: Optional[float] = None, 
    issue_date: Optional[date] = None, 
    work_type: Optional[str] = None, 
    planned_end_date: Optional[date] = None, 
    car_id: Optional[int] = None, 
    mechanic_id: Optional[int] = None, 
    db: Session = Depends(get_db)
):
    try:
        return edit_order(db, order_id, cost, issue_date, work_type, planned_end_date, car_id, mechanic_id)
    except HTTPException as e:
        raise e


@router.get("/orders/", response_model=list[OrderResponse])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_orders(db, skip=skip, limit=limit)
#------------------------------------------------------------------------