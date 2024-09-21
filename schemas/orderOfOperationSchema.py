from datetime import date
from pydantic import BaseModel
from typing import List, Optional

class OrderOfOperationSchema(BaseModel):
    code: str
    weight_per_piece: float
    total_weight: float
    total_pieces: Optional[int] = None
    status: Optional[str] = None
    label_item: Optional[bool] = None
    customer: int
    article: int
    wires: List[int]
    wire_porcentage: List[dict]

class OrderOfOperationResponseModel(OrderOfOperationSchema):
    id: int

class OrderOfOperationUpdate(BaseModel):
    code: Optional[str] = None
    weight_per_piece: Optional[float] = None
    total_weight: Optional[float] = None
    total_pieces: Optional[int] = None
    status: Optional[str] = None
    label_item: Optional[bool] = None
    customer: int
    article: int
    wires: List[int]
    wire_porcentage: List[dict]


class OrderOfOperationPublic(BaseModel):
    id: int
    code: str
    weight_per_piece: float
    total_weight: float
    status: str
    label_item: bool
    total_pieces: Optional[int] = None
    date_closed: Optional[date] = None
    wire_porcentage: List[dict]

class OrderOfOperationList(BaseModel):
    ops: List[OrderOfOperationPublic]
