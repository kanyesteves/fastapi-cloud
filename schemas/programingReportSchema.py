from pydantic import BaseModel
from typing import List

class ProgramingReportSchema(BaseModel):
    name: str
    rpm: float
    op: str
    tear: str
    date_start: str
    date_end: str
    efficiency: float
    weight_daily: float
    days_for_done: float
    type_register: str


class ProgramingReportResponseModel(ProgramingReportSchema):
    id: int

class ProgramingReportPublic(BaseModel):
    id: int
    name: str
    rpm: float
    op: str
    tear: str
    date_start: str
    date_end: str
    efficiency: float
    weight_daily: float
    days_for_done: float
    type_register: str

class ProgramingReport(BaseModel):
    programingReport: List[ProgramingReportPublic]