from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

# Таблица "Автомобиль"
class Car(Base):
    __tablename__ = "cars"
    
    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор
    brand = Column(String, index=True)  # Марка
    license_plate = Column(String, unique=True, index=True)  # Номер
    year = Column(Integer)  # Год выпуска
    owner_name = Column(String)  # ФИО владельца
    
    # Связь с заказами
    orders = relationship("Order", back_populates="car")


# Таблица "Автомеханик"
class Mechanic(Base):
    __tablename__ = "mechanics"
    
    id = Column(Integer, primary_key=True, index=True)  # Табельный номер
    name = Column(String, index=True)  # ФИО
    experience = Column(Integer)  # Стаж
    rank = Column(Integer)  # Разряд
    
    # Связь с заказами
    orders = relationship("Order", back_populates="mechanic")


# Таблица "Заказ"
class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор
    cost = Column(Float)  # Стоимость
    issue_date = Column(Date)  # Дата выдачи
    work_type = Column(String)  # Вид работ
    planned_end_date = Column(Date)  # Плановая дата окончания
    actual_end_date = Column(Date, nullable=True)  # Реальная дата окончания (может быть пустой)
    
    # Связи с Автомобилем и Автомехаником
    car_id = Column(Integer, ForeignKey("cars.id"))  # Внешний ключ на Автомобиль
    mechanic_id = Column(Integer, ForeignKey("mechanics.id"))  # Внешний ключ на Автомеханика
    
    car = relationship("Car", back_populates="orders")
    mechanic = relationship("Mechanic", back_populates="orders")
