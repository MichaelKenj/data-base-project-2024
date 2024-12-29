from fastapi import FastAPI
from .db import Base, engine
from .models import Car, Mechanic, Order
from .api import router

app = FastAPI()

# Создать таблицы, если их нет
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "API is running!"}

app.include_router(router)