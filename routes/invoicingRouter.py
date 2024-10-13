from schemas.invoicingSchema import InvoicingSchema, InvoicingPublic
from services.invoicingService import InvoicingService
from fastapi import APIRouter
from http import HTTPStatus


router = APIRouter(prefix='/invoicings', tags=['Invoicings Endpoints'])
service = InvoicingService()
    
@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllInvoicings():
    try: 
        invoicings = service.getAllInvoicings()
        return invoicings
    except:
        return HTTPStatus.NOT_FOUND

@router.get('/{invoicing_id}', status_code=HTTPStatus.OK, response_model=InvoicingPublic)
def getInvoicingById(invoicing_id: int):
    try: 
        invoicing = service.getInvoicingById(invoicing_id)
        return invoicing
    except:
        return HTTPStatus.NOT_FOUND
    
@router.post('/register', status_code=HTTPStatus.CREATED)
def createInvoicing(invoicing: InvoicingSchema):
    try: 
        service.createInvoicing(invoicing)
        return "Faturado com sucesso !!"
    except:
        return HTTPStatus.INTERNAL_SERVER_ERROR

@router.post('/generatePDF', status_code=HTTPStatus.CREATED)
def generatePDF(invoicing: InvoicingSchema):
    try: 
        service.generatePDF(invoicing)
        return "Exportado com sucesso !!"
    except:
        return HTTPStatus.INTERNAL_SERVER_ERROR