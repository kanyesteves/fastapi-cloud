from pydantic import BaseModel
from typing import List, Optional


class OrderOfOperationrSchema(BaseModel):
    code: str
    weight_per_piece: float
    customer_id: int
    wire_id: str
    total_weight: float

class CustomerResponseModel(OrderOfOperationrSchema):
    id: int

class OrderOfOperationrUpdate(BaseModel):
    code: Optional[str] = None
    weight_per_piece: Optional[float] = None
    customer_id: Optional[int] = None
    wire_id: Optional[str] = None
    total_weight: Optional[float] = None

class OrderOfOperationrPublic(BaseModel):
    id: int
    code: str
    weight_per_piece: float
    customer_id: int
    wire_id: str
    total_weight: float

class OrderOfOperationrList(BaseModel):
    ops: List[OrderOfOperationrPublic]
