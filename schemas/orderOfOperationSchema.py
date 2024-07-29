from pydantic import BaseModel
from typing import List, Optional


class OrderOfOperationSchema(BaseModel):
    code: str
    weight_per_piece: float
    customer_id: int
    wire_id: str
    total_weight: float

class OrderOfOperationResponseModel(OrderOfOperationSchema):
    id: int

class OrderOfOperationUpdate(BaseModel):
    code: Optional[str] = None
    weight_per_piece: Optional[float] = None
    customer_id: Optional[int] = None
    wire_id: Optional[str] = None
    total_weight: Optional[float] = None

class OrderOfOperationPublic(BaseModel):
    id: int
    code: str
    weight_per_piece: float
    customer_id: int
    wire_id: str
    total_weight: float

class OrderOfOperationList(BaseModel):
    ops: List[OrderOfOperationPublic]
