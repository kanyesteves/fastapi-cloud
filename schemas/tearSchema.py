from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List, Optional


class TearSchema(BaseModel):
    name: str
    model: str

class TearResponseModel(TearSchema):
    id: int

class TearUpdate(BaseModel):
    name: Optional[str] = None
    model: Optional[str] = None

class TearPublic(BaseModel):
    id: int
    name: str
    model: str

class TearList(BaseModel):
    tears: List[TearPublic]
