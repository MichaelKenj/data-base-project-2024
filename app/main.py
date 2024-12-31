from sqlalchemy.orm import Session  # Добавьте импорт Session
from fastapi import FastAPI, Depends
from .db import Base, engine, get_db
from .models import Car, Mechanic, Order
from .api import router

app = FastAPI()

# Создать таблицы, если их нет
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "API is running!"}

@app.get("/orders/")
def get_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).all()
    return orders

@app.get("/cars/")
def get_cars(db: Session = Depends(get_db)):
    cars = db.query(Car).all()
    return cars


# Эндпоинт для получения всех механиков
@app.get("/mechanics/")
def get_mechanics(db: Session = Depends(get_db)):
    mechanics = db.query(Mechanic).all()
    return mechanics



app.include_router(router)