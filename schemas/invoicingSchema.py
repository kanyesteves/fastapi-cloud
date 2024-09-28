from datetime import date
from pydantic import BaseModel
from typing import List, Optional

class InvoicingSchema(BaseModel):
    records: dict
    weight_per_wire: dict
    total_weight: float
    customer: str
    article: str

class InvoincingResponseModel(InvoicingSchema):
    id: int

class InvoicingPublic(BaseModel):
    id: int
    records: dict
    weight_per_wire: dict
    total_weight: float
    customer: str
    article: str
    date: date

class InvoicingList(BaseModel):
    invoicings: List[InvoicingPublic]
