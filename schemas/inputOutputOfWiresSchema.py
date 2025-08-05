from pydantic import BaseModel
from typing import List

class InputOutputOfWiresSchema(BaseModel):
    name: str
    weight: float
    type_register: str
    fiscal_note: str
    date_open: str

class InputOutputOfWiresResponseModel(InputOutputOfWiresSchema):
    id: int

class InputOutputOfWiresPublic(BaseModel):
    id: int
    name: str
    type_register: str
    fiscal_note: str
    date_open: str

class InputOutputOfWiresList(BaseModel):
    inputOutputOfWires: List[InputOutputOfWiresPublic]