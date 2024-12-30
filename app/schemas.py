from pydantic import BaseModel
from typing import Optional
from datetime import date

# Схемы для создания записей
class CarCreate(BaseModel):
    brand: str
    license_plate: str
    year: int
    owner_name: str

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