from pydantic import BaseModel
from typing import List, Optional

class CustomerSchema(BaseModel):
    name: str
    description: str

class CustomerResponseModel(CustomerSchema):
    id: int

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class CustomerPublic(BaseModel):
    id: int
    name: str
    description: str

class CustomerList(BaseModel):
    customers: List[CustomerPublic]
