from pydantic import BaseModel
from typing import List, Optional

class CustomerSchema(BaseModel):
    name: str
    description: Optional[str] = None

class CustomerResponseModel(CustomerSchema):
    id: int

class CustomerUpdate(BaseModel):
    name:   Optional[str] = None
    description: Optional[str] = None

class CustomerPublic(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

class CustomerList(BaseModel):
    customers: List[CustomerPublic]
