from datetime import date
from pydantic import BaseModel
from typing import List, Optional
from schemas.operatorSchema import OperatorPublic
from schemas.orderOfOperationSchema import OrderOfOperationPublic
from schemas.tearSchema import TearPublic

class ProductionSchema(BaseModel):
    code_per_piece: int
    weight: float
    review: Optional[str] = None
    tear: str
    op: str
    operator: str
    second_quality: str

class ProductionResponseModel(ProductionSchema):
    id: int

class ProductionUpdate(BaseModel):
    code_per_piece: int
    weight: float
    review: str
    date: date
    tear: str
    op: str
    operator: str
    second_quality: str

class ProductionPublic(BaseModel):
    id: int
    code_per_piece: int
    weight: float
    review: str
    invoiced: bool
    date: date
    tear: str
    op: str
    operator: str
    second_quality: str

class ProductionList(BaseModel):
    productions: List[ProductionPublic]