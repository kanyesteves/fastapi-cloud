from pydantic import BaseModel
from typing import List, Optional


class CustomerSchema(BaseModel):
    name: str
    article: str

class CustomerResponseModel(CustomerSchema):
    id: int

class CustomerUpdate(BaseModel):
    name:   Optional[str] = None
    article: Optional[str] = None

class CustomerPublic(BaseModel):
    id: int
    name: str
    article: str

class CustomerList(BaseModel):
    operators: List[CustomerPublic]
