from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from .db import Base

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True)
    license_plate = Column(String, unique=True, index=True)
    year = Column(Integer)
    owner_name = Column(String)

    orders = relationship("Order", back_populates="car")

class Mechanic(Base):
    __tablename__ = "mechanics"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    experience = Column(Integer)
    rank = Column(Integer)

    orders = relationship("Order", back_populates="mechanic")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    cost = Column(Float)
    issue_date = Column(Date)
    work_type = Column(String)
    planned_end_date = Column(Date)
    car_id = Column(Integer, ForeignKey("cars.id"))
    mechanic_id = Column(Integer, ForeignKey("mechanics.id"))

    car = relationship("Car", back_populates="orders")
    mechanic = relationship("Mechanic", back_populates="orders")
