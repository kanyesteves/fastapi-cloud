from pydantic import BaseModel, EmailStr



class UserModel(BaseModel):
    name: str
    passwd: str
    email: EmailStr
    office: str

class UserResponseModel(UserModel):
    id: int

class UserPublic(BaseModel):
    id: int
    name: str
    email: EmailStr
    office: str

class UserList(BaseModel):
    users: list[UserPublic]
