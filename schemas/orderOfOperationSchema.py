from datetime import date
from pydantic import BaseModel
from typing import List, Optional
from schemas.articleSchema import ArticlePublic
from schemas.wireSchema import WirePublic


class OrderOfOperationSchema(BaseModel):
    code: str
    weight_per_piece: float
    total_weight: float
    total_pieces: Optional[int] = None
    status: Optional[str] = None
    article: ArticlePublic
    wires: List[WirePublic]

class OrderOfOperationResponseModel(OrderOfOperationSchema):
    id: int

class OrderOfOperationUpdate(BaseModel):
    code: Optional[str] = None
    weight_per_piece: Optional[float] = None
    total_weight: Optional[float] = None
    total_pieces: Optional[int] = None
    status: Optional[str] = None
    article: ArticlePublic
    wires: List[WirePublic]


class OrderOfOperationPublic(BaseModel):
    id: int
    code: str
    weight_per_piece: float
    total_weight: float
    status: str
    total_pieces: Optional[int] = None
    date_closed: Optional[date] = None
    article: ArticlePublic
    wires: List[WirePublic]

class OrderOfOperationList(BaseModel):
    ops: List[OrderOfOperationPublic]
