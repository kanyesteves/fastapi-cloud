from schemas.wireSchema import WireSchema, WirePublic, WireUpdate
from services.wireService import WireService
from services.authService import AuthService
from fastapi import APIRouter, Depends
from http import HTTPStatus


service = WireService()
auth_service = AuthService()
router = APIRouter(
    prefix='/wires',
    tags=['Wires Endpoints'],
    dependencies=[Depends(auth_service.get_current_user)]
)

@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllWires():
    try: 
        wires = service.getAllWires()
        return wires
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.get('/{wire_id}', status_code=HTTPStatus.OK, response_model=WirePublic)
def getWireById(wire_id: int):
    try: 
        wire = service.getWireById(wire_id)
        return wire
    except:
        return HTTPStatus.NOT_FOUND
    
@router.post('/register', status_code=HTTPStatus.CREATED)
def createWire(wire: WireSchema):
    try: 
        service.createWire(wire)
        return "Fio criado com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.put('/update/{wire_id}', status_code=HTTPStatus.OK)
def updateWire(wire_id: int, wire: WireUpdate):
    service.updateWire(wire_id, wire)
    return "Fio atualizado com sucesso !!"

@router.delete('/remove/{wire_id}', status_code=HTTPStatus.OK)
def removeWire(wire_id: int):
    try: 
        service.deleteWire(wire_id)
        return "Fio removido com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY