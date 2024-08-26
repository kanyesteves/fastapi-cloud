from pydantic import BaseModel
from typing import List, Optional


class ArticleSchema(BaseModel):
    name: str
    description: str
    file_path: Optional[str] = None


class ArticleResponseModel(ArticleSchema):
    id: int

class ArticleUpdate(BaseModel):
    name:   Optional[str] = None
    description: Optional[str] = None
    file_path: Optional[str] = None

class ArticlePublic(BaseModel):
    id: int
    name: str
    description: str
    file_path: str

class ArticleList(BaseModel):
    articles: List[ArticlePublic]
