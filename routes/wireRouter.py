from schemas.wireSchema import WireSchema, WirePublic, WireUpdate
from services.wireService import WireService
from fastapi import APIRouter
from http import HTTPStatus


router = APIRouter(prefix='/wires', tags=['Wires Endpoints'])
service = WireService()
    
@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllWires():
    try: 
        wires = service.getAllWires()
        return wires
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.get('/{customer_id}', status_code=HTTPStatus.OK, response_model=WirePublic)
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

@router.delete('/remove/{customer_id}', status_code=HTTPStatus.OK)
def removeWire(Wire_id: int):
    try: 
        service.deleteWire(Wire_id)
        return "Fio removido com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY