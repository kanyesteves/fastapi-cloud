from pydantic import BaseModel
from typing import List, Optional


class WireSchema(BaseModel):
    name: str
    description: str

class WireResponseModel(WireSchema):
    id: int

class WireUpdate(BaseModel):
    name:   Optional[str] = None
    description: Optional[str] = None

class WirePublic(BaseModel):
    id: int
    name: str
    description: str
    percentage: Optional[int] = None

class WireList(BaseModel):
    wires: List[WirePublic]
