from fastapi import FastAPI
from .db import Base, engine
from .models import User

app = FastAPI()

# Создать таблицы, если их нет
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}
