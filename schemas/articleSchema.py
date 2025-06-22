from pydantic import BaseModel
from typing import List, Optional

class ArticleSchema(BaseModel):
    name: str
    price: float
    description: str

class ArticleResponseModel(ArticleSchema):
    id: int

class ArticleUpdate(BaseModel):
    name:   Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None

class ArticlePublic(BaseModel):
    id: int
    name: str
    price: float
    description: str

class ArticleList(BaseModel):
    articles: List[ArticlePublic]
