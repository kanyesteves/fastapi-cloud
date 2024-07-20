from schemas.userSchema import UserSchema, UserPublic, UserUpdate
from services.userService import UserService
from fastapi import APIRouter
from http import HTTPStatus


router = APIRouter(prefix='/users', tags=['Users Endpoints'])
service = UserService()

@router.post('/register', status_code=HTTPStatus.CREATED)
def createUser(user: UserSchema):
    try: 
        service.createUser(user)
        return "Usuário criado com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY
    
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

@router.put('/update/{user_id}', status_code=HTTPStatus.OK)
def updateUser(user_id: int, user: UserSchema):
    try: 
        service.updateUser(user_id, user)
        return "Usuário atualizado com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.delete('/remove/{user_id}', status_code=HTTPStatus.OK)
def removeUser(user_id: int):
    try: 
        service.deleteUser(user_id)
        return "Usuário removido com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY