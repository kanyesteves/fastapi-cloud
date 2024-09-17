from datetime import date
from pydantic import BaseModel
from typing import List
from schemas.operatorSchema import OperatorPublic
from schemas.orderOfOperationSchema import OrderOfOperationPublic
from schemas.tearSchema import TearPublic

class ProductionSchema(BaseModel):
    code_per_piece: int
    weight: float
    review: str
    tear: str
    op: str
    operator: str

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

class ProductionList(BaseModel):
    productions: List[ProductionPublic]