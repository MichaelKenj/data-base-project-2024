from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, UniqueConstraint
from sqlalchemy.orm import relationship
from .db import Base

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, nullable=False, index=True)  
    license_plate = Column(String, unique=True, nullable=False, index=True) 
    year = Column(Integer, nullable=False) 
    owner_name = Column(String, nullable=False) 
    color = Column(String, nullable=True)
    
    orders = relationship("Order", back_populates="car")

    __table_args__ = (
        UniqueConstraint("license_plate", name="uq_license_plate"), 
    )


class Mechanic(Base):
    __tablename__ = "mechanics"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    experience = Column(Integer, nullable=False)
    rank = Column(Integer, nullable=False)

    orders = relationship("Order", back_populates="mechanic")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    cost = Column(Float, nullable=False)
    issue_date = Column(Date, nullable=False)
    work_type = Column(String, nullable=False)
    planned_end_date = Column(Date, nullable=False)
    car_id = Column(Integer, ForeignKey("cars.id"), nullable=False)
    mechanic_id = Column(Integer, ForeignKey("mechanics.id"), nullable=True)

    car = relationship("Car", back_populates="orders")
    mechanic = relationship("Mechanic", back_populates="orders", uselist=False)