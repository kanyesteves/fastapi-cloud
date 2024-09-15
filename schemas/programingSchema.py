from pydantic import BaseModel
from typing import List


class ProgramingSchema(BaseModel):
    name: str
    tear: int
    op: int

class ProgramingResponseModel(ProgramingSchema):
    id: int

class ProgramingUpdate(BaseModel):
    name: str
    tear: int
    op: int

class ProgramingPublic(BaseModel):
    id: int
    name: str

class ProgramingList(BaseModel):
    programings: List[ProgramingPublic]
