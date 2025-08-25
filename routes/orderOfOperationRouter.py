from schemas.orderOfOperationSchema import OrderOfOperationSchema, OrderOfOperationUpdate
from services.orderOfOperationService import OrderOfOperationrService
from services.authService import AuthService
from fastapi import APIRouter, Depends
from http import HTTPStatus


service = OrderOfOperationrService()
auth_service = AuthService()
router = APIRouter(
    prefix='/orderOfOperatios',
    tags=['Order Of Operatios Endpoints'],
    dependencies=[Depends(auth_service.get_current_user)]
)
    
@router.get('/getAllClosed', status_code=HTTPStatus.OK)
def getAllOPsClosed():
    try: 
        ops = service.getAllOPsClosed()
        return ops
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY
    
@router.get('/getAllOpenAndInProgress', status_code=HTTPStatus.OK)
def getAllOpenAndInProgress():
    try: 
        ops = service.getAllOpenAndInProgress()
        return ops
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.get('/{op_id}', status_code=HTTPStatus.OK)
def getOPById(op_id: int):
    try: 
        op = service.getOPById(op_id)
        return op
    except:
        return HTTPStatus.NOT_FOUND
    
@router.post('/register', status_code=HTTPStatus.CREATED)
def createOP(op: OrderOfOperationSchema):
    try: 
        service.createOP(op)
        return "Order de operação criado com sucesso !!"
    except:
        return HTTPStatus.INTERNAL_SERVER_ERROR

@router.put('/update/{op_id}', status_code=HTTPStatus.OK)
def updateOP(op_id: int, op: OrderOfOperationUpdate):
    service.updateOP(op_id, op)
    return "Order de operação atualizado com sucesso !!"

@router.put('/close/{op_id}', status_code=HTTPStatus.OK)
def removeOP(op_id: int):
    try: 
        service.closeOP(op_id)
        return "Order de operação fechada com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY