from fastapi import FastAPI # FastAPI: Intermediate between Frontend nad Backend
from sqlmodel import create_engine # SQLModel: ORM; used to use SQL as python classes
from sqlmodel import SQLModel
from contextlib import asynccontextmanager  


DATABASE_URL = "postgresql://postgres:test@localhost:5431/postgres"

engine = create_engine(DATABASE_URL, echo=True) 
# enigne is a connection between python and the database

@asynccontextmanager
async def lifespan(app: FastAPI): # execute something on boot up
    SQLModel.metadata.create_all(engine) #create tables stored in the metadata -- table is store in metadata upon setting table=True in class creation
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/workouts")
def return_message():
    return {"message": "Here are all your workouts"}


