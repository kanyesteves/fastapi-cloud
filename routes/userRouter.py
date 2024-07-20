from models.userModel import UserModel, UserPublic, UserList, UserResponseModel
from services.userService import UserService
from fastapi import APIRouter
from http import HTTPStatus


router = APIRouter(prefix='/users', tags=['users'])
service = UserService()

@router.post('/register', status_code=HTTPStatus.CREATED)
def createUser(user: UserModel):
    try:
        service.createUser(user)
        return HTTPStatus.CREATED
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY
    
# @router.get('/', response_model=UserModel)
# # ...
# @router.put('/{user_id}', response_model=UserModel)
# # ...
# @router.delete('/{user_id}', response_model=UserModel)
# ...