from pydantic import BaseModel
from typing import List, Optional

class WireSchema(BaseModel):
    name: str
    description: str
    weight: float

class WireResponseModel(WireSchema):
    id: int

class WireUpdate(BaseModel):
    name:   Optional[str] = None
    description: Optional[str] = None
    weight: Optional[float] = None

class WirePublic(BaseModel):
    id: int
    name: str
    description: str
    weight: float

class WireList(BaseModel):
    wires: List[WirePublic]
