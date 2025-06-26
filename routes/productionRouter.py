from schemas.productionSchema import ProductionSchema, ProductionPublic, ProductionUpdate
from services.productionService import ProductionService
from services.authService import AuthService
from fastapi import APIRouter, Depends
from http import HTTPStatus


service = ProductionService()
auth_service = AuthService()
router = APIRouter(
    prefix='/productions',
    tags=['Productions Endpoints']
)
    
@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllRecords():
    try: 
        records = service.getAllRecords()
        return records
    except:
        return HTTPStatus.NOT_FOUND

@router.get('/getAllRecordsByOp/{op}', status_code=HTTPStatus.OK)
def getAllRecordsByOp(op: str):
    try:
        records_by_op = service.getAllRecordsByOp(op)
        return records_by_op
    except:
        return HTTPStatus.NOT_FOUND

@router.get('/getLastRecordByOp/{op}', status_code=HTTPStatus.OK)
def getLastRecordByOp(op: str):
    try:
        last_record_by_op = service.getLastRecordByOp(op)
        return last_record_by_op
    except:
        return HTTPStatus.NOT_FOUND
    
@router.get('/getLast3Records', status_code=HTTPStatus.OK)
def getLast3Records():
    try:
        last_3_records = service.getLast3Records()
        return last_3_records
    except:
        return HTTPStatus.NOT_FOUND
    
@router.get('/getOpOptions/{op}', status_code=HTTPStatus.OK)
def getOpOptions(op: str):
    try:
        op_options = {
            "total_weight": service.getTotalWeight(op),
            "total_pieces": service.getTotalPieces(op),
            "total_invoiced": service.getTotalInvoiced(op)
        }
        return op_options
    except:
        return HTTPStatus.NOT_FOUND

@router.get('/{record_id}', status_code=HTTPStatus.OK, response_model=ProductionPublic)
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