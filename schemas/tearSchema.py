from pydantic import BaseModel
from typing import List, Optional


class TearSchema(BaseModel):
    name: str
    model: str
    status: bool

class TearResponseModel(TearSchema):
    id: int

class TearUpdate(BaseModel):
    name: Optional[str] = None
    model: Optional[str] = None
    status: Optional[bool] = None

class TearPublic(BaseModel):
    id: int
    name: str
    model: str
    status: bool

class TearList(BaseModel):
    tears: List[TearPublic]
