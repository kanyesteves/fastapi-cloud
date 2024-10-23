from schemas.programingSchema import ProgramingSchema
from services.programingService import ProgramingService
from services.authService import AuthService
from fastapi import APIRouter, Depends
from http import HTTPStatus


service = ProgramingService()
auth_service = AuthService()
router = APIRouter(
    prefix='/programings',
    tags=['Programings Endpoints'],
    dependencies=[Depends(auth_service.get_current_user)]
)
    
@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllPrograming():
    try: 
        programings = service.getAllPrograming()
        return programings
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.get('/{programing_id}', status_code=HTTPStatus.OK)
def getProgramingById(programing_id: int):
    try: 
        programing = service.getProgramingById(programing_id)
        return programing
    except:
        return HTTPStatus.NOT_FOUND
    
@router.post('/register', status_code=HTTPStatus.CREATED)
def createPrograming(programing: ProgramingSchema):
    try: 
        service.createPrograming(programing)
        return "Programação criado com sucesso !!"
    except:
        return HTTPStatus.INTERNAL_SERVER_ERROR

@router.delete('/remove/{programing_id}', status_code=HTTPStatus.OK)
def removePrograming(programing_id: int):
    try: 
        service.deletePrograming(programing_id)
        return "Programação removido com sucesso !!"
    except:
        return HTTPStatus.INTERNAL_SERVER_ERROR