from pydantic import BaseModel
from typing import List, Optional
from schemas.userSchema import UserPublic

class GroupSchema(BaseModel):
    name: str
    users: List[UserPublic]
    permissions: str

class GroupResponseModel(GroupSchema):
    id: int

class GroupUpdate(BaseModel):
    name:   Optional[str] = None
    users: Optional[List[UserPublic]] = None
    permissions: Optional[str] = None
    

class GroupPublic(BaseModel):
    id: int
    name: str
    users: Optional[List[UserPublic]] = None
    permissions: Optional[str] = None

class GroupList(BaseModel):
    groups: List[GroupPublic]
