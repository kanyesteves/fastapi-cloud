from schemas.programingSchema import ProgramingSchema, ProgramingUpdate
from services.programingService import ProgramingService
from fastapi import APIRouter
from http import HTTPStatus


router = APIRouter(prefix='/programings', tags=['Programings Endpoints'])
service = ProgramingService()
    
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

@router.put('/update/{programing_id}', status_code=HTTPStatus.OK)
def updatePrograming(programing_id: int, programing: ProgramingUpdate):
    service.updatePrograming(programing_id, programing)
    return "Programação atualizada com sucesso !!"

@router.delete('/remove/{programing_id}', status_code=HTTPStatus.OK)
def removePrograming(programing_id: int):
    try: 
        service.deletePrograming(programing_id)
        return "Programação removido com sucesso !!"
    except:
        return HTTPStatus.INTERNAL_SERVER_ERROR