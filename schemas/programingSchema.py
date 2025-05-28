from datetime import date
from pydantic import BaseModel
from typing import List


class ProgramingSchema(BaseModel):
    name: str
    tear: int
    op: int
    date_start: str
    date_end: str
    rpm: float
    efficiency: float
    weight_daily: float
    days_for_done: float
    wires: List[dict]

class ProgramingResponseModel(ProgramingSchema):
    id: int

class ProgramingPublic(BaseModel):
    id: int
    name: str
    date_start: date
    date_end: date
    rpm: float
    efficiency: float
    weight_daily: float
    days_for_done: float
    wires: List[dict]

class ProgramingList(BaseModel):
    programings: List[ProgramingPublic]
