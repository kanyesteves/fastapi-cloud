from schemas.inputOutputOfWiresSchema import InputOutputOfWiresSchema, InputOutputOfWiresPublic
from services.inputOutputOfWiresService import InputOutputOfWiresService
from services.authService import AuthService
from fastapi import APIRouter, Depends
from http import HTTPStatus

service = InputOutputOfWiresService()
auth_service = AuthService()
router = APIRouter(
    prefix='/inputOutputOfWires',
    tags=['InputOutputOfWires Endpoints'],
    dependencies=[Depends(auth_service.get_current_user)]
)

@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllInputOutputOfWires():
    try: 
        inputOutputOfWires = service.getAllInputOutputOfWires()
        return inputOutputOfWires
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.get('/{inputOutputOfWires_id}', status_code=HTTPStatus.OK, response_model=InputOutputOfWiresPublic)
def getInputOutputOfWiresById(inputOutputOfWires_id: int):
    try: 
        inputOutputOfWires = service.getInputOutputOfWiresById(inputOutputOfWires_id)
        return inputOutputOfWires
    except:
        return HTTPStatus.NOT_FOUND
    
@router.post('/register', status_code=HTTPStatus.CREATED)
def createInputOutputOfWires(inputOutputOfWires: InputOutputOfWiresSchema):
    try: 
        service.createInputOutputOfWires(inputOutputOfWires)
        return "Registro de recebimento criado com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY