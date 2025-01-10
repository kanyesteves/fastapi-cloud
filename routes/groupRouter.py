from schemas.groupSchema import GroupSchema, GroupPublic, GroupUpdate
from services.groupService import GroupService
from services.authService import AuthService
from services.userService import UserService
from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus


service = GroupService()
auth_service = AuthService()
user_service = UserService()
router = APIRouter(
    prefix='/groups', 
    tags=['Groups Endpoints'],
    dependencies=[Depends(auth_service.get_current_user)]
)
    
@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllGroups():
    try: 
        groups = service.getAllGroups()
        return groups
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.get('/{group_id}', status_code=HTTPStatus.OK, response_model=GroupPublic)
def getGroupById(group_id: int):
    try: 
        group = service.getGroupById(group_id)
        return group
    except:
        return HTTPStatus.NOT_FOUND

@router.post('/getPermissions', status_code=HTTPStatus.OK)
def getPermissions(data: dict):
    try:
        user = user_service.getUserByName(data["sub"])
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        group = service.getGroupHasUser(user.id)
        return group
    except KeyError:
        raise HTTPException(status_code=422, detail="Missing required field 'sub'.")
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

    
@router.get('/getUsersHasGroup/{group_id}', status_code=HTTPStatus.OK)
def getUsersHasGroup(group_id: int):
    try: 
        group = service.getUsersHasGroup(group_id)
        return group
    except:
        return HTTPStatus.NOT_FOUND
    
@router.post('/register', status_code=HTTPStatus.CREATED)
def createGroup(group: GroupSchema):
    try: 
        service.createGroup(group)
        return "Grupo criado com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.put('/update/{group_id}', status_code=HTTPStatus.OK)
def updateGroup(group_id: int, group: GroupUpdate):
    try:
        service.updateGroup(group_id, group)
        return "Grupo atualizado com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.delete('/remove/{group_id}', status_code=HTTPStatus.OK)
def removeGroup(group_id: int):
    try: 
        service.deleteGroup(group_id)
        return "Grupo removido com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY