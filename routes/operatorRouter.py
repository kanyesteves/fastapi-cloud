from schemas.operatorSchema import OperatorSchema, OperatorPublic, OperatorUpdate
from services.operatorService import OperatorService
from services.authService import AuthService
from fastapi import APIRouter, Depends
from http import HTTPStatus


service = OperatorService()
auth_service = AuthService()
router = APIRouter(
    prefix='/operators',
    tags=['Operators Endpoints'],
    dependencies=[Depends(auth_service.get_current_user)]
)
    
@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllOperators():
    try: 
        operators = service.getAllOperators()
        return operators
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.get('/{operator_id}', status_code=HTTPStatus.OK, response_model=OperatorPublic)
def getOperatorById(operator_id: int):
    try: 
        operator = service.getOperatorById(operator_id)
        return operator
    except:
        return HTTPStatus.NOT_FOUND
    
@router.post('/register', status_code=HTTPStatus.CREATED)
def createOperator(operator: OperatorSchema):
    try: 
        service.createOperator(operator)
        return "Operador criado com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.put('/update/{operator_id}', status_code=HTTPStatus.OK)
def updateOperator(operator_id: int, operator: OperatorUpdate):
    service.updateOperator(operator_id, operator)
    return "Operador atualizado com sucesso !!"

@router.delete('/remove/{operator_id}', status_code=HTTPStatus.OK)
def removeOperator(operator_id: int):
    try: 
        service.deleteOperator(operator_id)
        return "Operador removido com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY