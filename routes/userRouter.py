from entities.userEntity import UserEntity, UserBase
from models.userModel import UserModel
from services.userService import UserService
from fastapi import APIRouter
from http import HTTPStatus


router = APIRouter(prefix='/users', tags=['users'])

@router.post('/', status_code=HTTPStatus.CREATED, response_model=UserModel)
# ...    
@router.get('/', response_model=UserModel)
# ...
@router.put('/{user_id}', response_model=UserModel)
# ...
@router.delete('/{user_id}', response_model=UserModel)

    