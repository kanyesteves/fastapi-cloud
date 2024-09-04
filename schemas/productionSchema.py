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
    date: date
    tear: TearPublic
    op: OrderOfOperationPublic
    operator: OperatorPublic

class ProductionResponseModel(ProductionSchema):
    id: int

class ProductionUpdate(BaseModel):
    code_per_piece: int
    weight: float
    review: str
    date: date
    tear: TearPublic
    op: OrderOfOperationPublic
    operator: OperatorPublic

class ProductionPublic(BaseModel):
    id: int
    code_per_piece: int
    weight: float
    review: str
    invoiced: bool
    date: date
    tear: TearPublic
    op: OrderOfOperationPublic
    operator: OperatorPublic

class ProductionList(BaseModel):
    productions: List[ProductionPublic]