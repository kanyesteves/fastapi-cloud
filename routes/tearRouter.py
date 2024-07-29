from schemas.tearSchema import TearSchema, TearPublic, TearUpdate
from services.tearService import TearService
from fastapi import APIRouter
from http import HTTPStatus


router = APIRouter(prefix='/teares', tags=['Teares Endpoints'])
service = TearService()
    
@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllTeares():
    try: 
        teares = service.getAllTeares()
        return teares
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.get('/{tear_id}', status_code=HTTPStatus.OK, response_model=TearPublic)
def getTearById(tear_id: int):
    try: 
        tear = service.getTearById(tear_id)
        return tear
    except:
        return HTTPStatus.NOT_FOUND
    
@router.post('/register', status_code=HTTPStatus.CREATED)
def createTear(tear: TearSchema):
    try: 
        service.createTear(tear)
        return "Tear criado com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.put('/update/{tear_id}', status_code=HTTPStatus.OK)
def updateTear(tear_id: int, tear: TearUpdate):
    service.updateTear(tear_id, tear)
    return "Tear atualizado com sucesso !!"

@router.delete('/remove/{tear_id}', status_code=HTTPStatus.OK)
def removeTear(tear_id: int):
    try: 
        service.deleteTear(tear_id)
        return "Tear removido com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY