from schemas.userSchema import UserSchema, UserPublic, UserUpdate
from services.userService import UserService
from services.authService import AuthService
from fastapi import APIRouter, Depends
from http import HTTPStatus


service = UserService()
auth_service = AuthService()
router = APIRouter(
    prefix='/users', 
    tags=['Users Endpoints'], 
    dependencies=[Depends(auth_service.get_current_user)]
)
    
@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllUsers():
    try: 
        users = service.getAllUsers()
        return users
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.get('/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic)
def getUserById(user_id: int):
    try: 
        user = service.getUserById(user_id)
        return user
    except:
        return HTTPStatus.NOT_FOUND
    
@router.post('/register', status_code=HTTPStatus.CREATED)
def createUser(user: UserSchema):
    try: 
        service.createUser(user)
        return "Usuário criado com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.put('/update/{user_id}', status_code=HTTPStatus.OK)
def updateUser(user_id: int, user: UserUpdate):
    service.updateUser(user_id, user)
    return "Usuário atualizado com sucesso !!"

@router.delete('/remove/{user_id}', status_code=HTTPStatus.OK)
def removeUser(user_id: int):
    try: 
        service.deleteUser(user_id)
        return "Usuário removido com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY