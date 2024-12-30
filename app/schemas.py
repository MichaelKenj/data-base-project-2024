from pydantic import BaseModel
from datetime import date
from typing import Optional

# Схемы для создания объектов
class CarCreate(BaseModel):
    brand: str
    license_plate: str
    year: int
    owner_name: str
    color: Optional[str] = None

class MechanicCreate(BaseModel):
    name: str
    experience: int
    rank: int

class OrderCreate(BaseModel):
    cost: float
    issue_date: date
    work_type: str
    planned_end_date: date
    car_id: int
    mechanic_id: int

# Схемы для ответа
class CarResponse(BaseModel):
    id: int
    brand: str
    license_plate: str
    year: int
    owner_name: str
    color: Optional[str] = None

    class Config:
        orm_mode = True

class MechanicResponse(BaseModel):
    id: int
    name: str
    experience: int
    rank: int

    class Config:
        orm_mode = True

class OrderResponse(BaseModel):
    id: int
    cost: float
    issue_date: date
    work_type: str
    planned_end_date: date
    car_id: int
    mechanic_id: int

    class Config:
        orm_mode = True
