from pydantic import BaseModel, EmailStr
from typing import List, Optional


class UserSchema(BaseModel):
    name: str
    passwd: str
    email: EmailStr
    office: str

class UserResponseModel(UserSchema):
    id: int

class UserUpdate(BaseModel):
    name: Optional[str] = None
    passwd: Optional[str] = None
    email: Optional[EmailStr] = None
    office: Optional[str] = None

class UserPublic(BaseModel):
    id: int
    name: str
    email: EmailStr
    office: str

class UserList(BaseModel):
    users: List[UserPublic]
