from fastapi import FastAPI # FastAPI: Intermediate between Frontend and Backend
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlmodel import create_engine, SQLModel, Session, select, Field # SQLModel: ORM; used to use SQL as python classes

from contextlib import asynccontextmanager  
from models import Workouts



DATABASE_URL = "postgresql://postgres:test@localhost:5431/postgres"

engine = create_engine(DATABASE_URL, echo=True) # echo = True; means the sql commnds should be printed
# enigne is a connection between python and the database

@asynccontextmanager
async def lifespan(app: FastAPI): # execute something on boot up
    SQLModel.metadata.create_all(engine) #create tables stored in the metadata -- table is store in metadata upon setting table=True in class creation
    yield

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:3000", # CORS whitelist
    "http://127.0.0.1:3000", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/workouts/{workout_id}")
def read_workout(workout_id: int):
    with Session(engine) as session:
        workout = session.get(Workouts, workout_id)

        if not workout:
            raise HTTPException(status_code=404, detail="Workout not found")

        return workout

@app.delete("/workouts/{workout_id}")
def delete_workout(workout_id:int):
    with Session(engine) as session:
        workout = session.get(Workouts, workout_id)
        if not workout:
            raise HTTPException(status_code=404, detail="not found")
        session.delete(workout)
        session.commit()

    return {"ok": True}

@app.get("/workouts")
def view_workouts():
    with Session(engine) as session:
        statement = select(Workouts)
        results = session.exec(statement)
        return results.all()

@app.post("/workouts") # post: protocol for sending data
def add_workout(workout: Workouts):
    with Session(engine) as session: # session: the delivery using the connection (engine) to access the database
         
        session.add(workout)

        session.commit()

        session.refresh(workout)

        return workout
