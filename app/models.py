from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, UniqueConstraint
from sqlalchemy.orm import relationship
from .db import Base

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, nullable=False, index=True)  # Указываем, что поле не может быть пустым
    license_plate = Column(String, unique=True, nullable=False, index=True)  # Добавлено nullable=False
    year = Column(Integer, nullable=False)  # Добавлено nullable=False
    owner_name = Column(String, nullable=False)  # Добавлено nullable=False
    color = Column(String, nullable=True)
    
    # Связь с заказами
    orders = relationship("Order", back_populates="car")

    __table_args__ = (
        UniqueConstraint("license_plate", name="uq_license_plate"),  # Дополнительный уникальный индекс для номера
    )


class Mechanic(Base):
    __tablename__ = "mechanics"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Указываем, что поле обязательно
    experience = Column(Integer, nullable=False)  # Добавлено nullable=False
    rank = Column(Integer, nullable=False)  # Добавлено nullable=False

    # Связь с заказами
    orders = relationship("Order", back_populates="mechanic")


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    cost = Column(Float, nullable=False)  # Добавлено nullable=False
    issue_date = Column(Date, nullable=False)  # Добавлено nullable=False
    work_type = Column(String, nullable=False)  # Добавлено nullable=False
    planned_end_date = Column(Date, nullable=False)  # Добавлено nullable=False
    car_id = Column(Integer, ForeignKey("cars.id"), nullable=False)  # Добавлено nullable=False
    mechanic_id = Column(Integer, ForeignKey("mechanics.id"), nullable=False)  # Добавлено nullable=False

    # Связь с другими таблицами
    car = relationship("Car", back_populates="orders")
    mechanic = relationship("Mechanic", back_populates="orders")