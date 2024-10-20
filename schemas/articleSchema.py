from pydantic import BaseModel
from typing import List, Optional


class ArticleSchema(BaseModel):
    name: str
    description: str

class ArticleResponseModel(ArticleSchema):
    id: int

class ArticleUpdate(BaseModel):
    name: str
    description: str

class ArticlePublic(BaseModel):
    id: int
    name: str
    description: str

class ArticleList(BaseModel):
    articles: List[ArticlePublic]
