from schemas.customerSchema import CustomerSchema, CustomerPublic, CustomerUpdate
from services.customerService import CustomerService
from fastapi import APIRouter
from http import HTTPStatus


router = APIRouter(prefix='/customers', tags=['Customers Endpoints'])
service = CustomerService()
    
@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllCustomers():
    try: 
        customers = service.getAllCustomers()
        return customers
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.get('/{customer_id}', status_code=HTTPStatus.OK, response_model=CustomerPublic)
def getCustomerById(customer_id: int):
    try: 
        customer = service.getCustomerById(customer_id)
        return customer
    except:
        return HTTPStatus.NOT_FOUND
    
@router.post('/register', status_code=HTTPStatus.CREATED)
def createCustomer(customer: CustomerSchema):
    try: 
        service.createCustomer(customer)
        return "Cliente criado com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.put('/update/{customer_id}', status_code=HTTPStatus.OK)
def updateCustomer(customer_id: int, customer: CustomerUpdate):
    try:
        service.updateCustomer(customer_id, customer)
        return "Cliente atualizado com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.delete('/remove/{customer_id}', status_code=HTTPStatus.OK)
def removeCustomer(customer_id: int):
    try: 
        service.deleteCustomer(customer_id)
        return "Cliente removido com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY