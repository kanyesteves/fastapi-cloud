from entities.userEntity import UserEntity, UserBase
from services.userService import UserService
from fastapi import APIRouter


router = APIRouter()
user_endpoint = "/user"

@router.get(f"{user_endpoint}/")
def getAll():

    return {"message": "Olá mundo"}

    