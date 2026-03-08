from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import date
from pydantic import BaseModel


class Workout(SQLModel, table=True):
    id: Optional[int] = Field(default=None,primary_key=True)
    date: date
    type: str
    duration: int
    distance: float
    tss: Optional[int]
    notes: Optional[str]


class Prompt(SQLModel):
    user_message: str

class AIAction(BaseModel):
    sql_command: str 
    workout_id: int | None = None
    workout_distance: float | None = None
    workout_duration: int | None = None
    workout_type: str | None = None
    workout_date: date | None = None

class AIPlan(BaseModel):
    actions: list[AIAction]