from pydantic import BaseModel
from typing import List, Optional
from schemas.userSchema import UserPublic

class GroupSchema(BaseModel):
    name: str
    permissions: List[dict]

class GroupResponseModel(GroupSchema):
    id: int

class GroupUpdate(BaseModel):
    name:   Optional[str] = None
    permissions: Optional[List[dict]] = None
    

class GroupPublic(BaseModel):
    id: int
    name: str
    permissions: Optional[List[dict]] = None

class GroupList(BaseModel):
    groups: List[GroupPublic]
