from pydantic import BaseModel

class UserModel(BaseModel):
    id: int
    name: str
    passwd: str
    office: str
    acess_gestor: bool