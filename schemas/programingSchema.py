from datetime import date
from pydantic import BaseModel
from typing import List


class ProgramingSchema(BaseModel):
    name: str
    tear: int
    op: int
    date_start: date
    date_end: date

class ProgramingResponseModel(ProgramingSchema):
    id: int

class ProgramingPublic(BaseModel):
    id: int
    name: str
    date_start: date
    date_end: date

class ProgramingList(BaseModel):
    programings: List[ProgramingPublic]
