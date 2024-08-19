from pydantic import BaseModel
from typing import List, Optional


class OperatorSchema(BaseModel):
    name: str
    office: str
    turn: str

class OperatorResponseModel(OperatorSchema):
    id: int

class OperatorUpdate(BaseModel):
    name:   Optional[str] = None
    office: Optional[str] = None
    turn:   Optional[str] = None

class OperatorPublic(BaseModel):
    id: int
    name: str
    office: str
    turn: str

class OperatorList(BaseModel):
    operators: List[OperatorPublic]
