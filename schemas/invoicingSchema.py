from datetime import date
from pydantic import BaseModel
from typing import List

class InvoicingSchema(BaseModel):
    records: List[dict]
    weight_per_wire: List[dict]
    total_weight: float
    customer: str
    article: str
    op: str

class InvoincingResponseModel(InvoicingSchema):
    id: int

class InvoicingPublic(BaseModel):
    id: int
    records: List[dict]
    weight_per_wire: List[dict]
    total_weight: float
    customer: str
    article: str
    op: str
    date: date

class InvoicingList(BaseModel):
    invoicings: List[InvoicingPublic]
