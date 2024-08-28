from pydantic import BaseModel
from typing import List, Optional
from schemas.articleSchema import ArticlePublic

class CustomerSchema(BaseModel):
    name: str
    article: Optional[List[ArticlePublic]] = None

class CustomerResponseModel(CustomerSchema):
    id: int

class CustomerUpdate(BaseModel):
    name:   Optional[str] = None
    article: Optional[List[ArticlePublic]] = None

class CustomerPublic(BaseModel):
    id: int
    name: str
    article: Optional[List[ArticlePublic]] = None

class CustomerList(BaseModel):
    operators: List[CustomerPublic]
