from pydantic import BaseModel
from typing import List, Optional

class InputOutputOfWiresSchema(BaseModel):
    name: str
    weight: float
    type_register: str
    fiscal_note: str
    date_open: str

class InputOutputOfWiresResponseModel(InputOutputOfWiresSchema):
    id: int

class InputOutputOfWiresUpdate(BaseModel):
    name: str = None
    type_register: Optional[str] = None
    fiscal_note: Optional[str] = None
    date_open: Optional[str] = None

class InputOutputOfWiresPublic(BaseModel):
    id: int
    name: str
    type_register: str
    fiscal_note: str
    date_open: str

class InputOutputOfWiresList(BaseModel):
    inputOutputOfWires: List[InputOutputOfWiresPublic]