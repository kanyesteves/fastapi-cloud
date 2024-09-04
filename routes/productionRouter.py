from schemas.productionSchema import ProductionSchema, ProductionPublic, ProductionUpdate
from services.productionService import ProductionService
from fastapi import APIRouter
from http import HTTPStatus


router = APIRouter(prefix='/productions', tags=['Productions Endpoints'])
service = ProductionService()
    
@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllRecords():
    try: 
        records = service.getAllRecords()
        return records
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.get('/{op_id}', status_code=HTTPStatus.OK, response_model=ProductionPublic)
def getRecordById(record_id: int):
    try: 
        record = service.getRecordById(record_id)
        return record
    except:
        return HTTPStatus.NOT_FOUND
    
@router.post('/register', status_code=HTTPStatus.CREATED)
def createOP(record: ProductionSchema):
    try: 
        service.createRecord(record)
        return "Malha registrada com sucesso !!"
    except:
        return HTTPStatus.INTERNAL_SERVER_ERROR

@router.put('/update/{op_id}', status_code=HTTPStatus.OK)
def updateRecord(record_id: int, record: ProductionUpdate):
    service.updateRecord(record_id, record)
    return "Malha atualizada com sucesso !!"

# @router.put('/close/{op_id}', status_code=HTTPStatus.OK)
# def removeOP(op_id: int):
#     try: 
#         service.closeOP(op_id)
#         return "Order de operação fechada com sucesso !!"
#     except:
#         return HTTPStatus.UNPROCESSABLE_ENTITY