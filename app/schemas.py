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
    owner_name: Optional[str]
    color: Optional[str]

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
    issue_date: Optional[date]  # Сделано Optional для работы с пустыми значениями
    work_type: Optional[str]  # Сделано Optional для работы с пустыми значениями
    planned_end_date: Optional[date]  # Сделано Optional для работы с пустыми значениями
    car_id: int
    mechanic_id: Optional[int]  # Сделано Optional для работы с пустыми значениями (если механик не назначен)

    class Config:
        orm_mode = True
