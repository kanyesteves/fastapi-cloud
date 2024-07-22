from sqlalchemy import select
from sqlalchemy.orm import Session
from utils.connDB import ConnectDB
from utils.libs import Libs
from schemas.customerSchema import CustomerSchema, CustomerUpdate
from entities.customerEntity import CustomerEntity

conn = ConnectDB()

class CustomerService:
    def __init__(self):
        self.lib = Libs()

    def getAllCustomers(self):
        with Session(bind=conn.engine) as session:
            select_query = select(CustomerEntity)
            all_customers = session.execute(select_query).fetchall()
            all_customers = [tear[0] for tear in all_customers]
            all_customers = [
                {
                    "id": customer.id,
                    "name": customer.name,
                    "article": customer.article,
                }
                for customer in all_customers
            ]
            return all_customers
        
    def getCustomerById(self, id):
        with Session(bind=conn.engine) as session:
            select_query = select(CustomerEntity).filter_by(id=id)
            customer = session.execute(select_query).fetchall()
            return customer[0][0]

    def createCustomer(self, customer: CustomerSchema):
        with Session(bind=conn.engine) as session:
            customer_entity = CustomerEntity(name=customer.name, article=customer.article)
            session.add(customer_entity)
            session.commit()

    def updateCustomer(self, id, customerSchema: CustomerUpdate):
        with Session(bind=conn.engine) as session:
            select_query = select(CustomerEntity).filter_by(id=id)
            customers = session.execute(select_query).fetchall()
            for customet in customers:
                for key, value in customerSchema.dict(exclude_unset=True).items():
                    setattr(customet[0], key, value)

            session.commit()

    def deleteCustomer(self, id):
        with Session(bind=conn.engine) as session:
            select_query = select(CustomerEntity).filter_by(id=id)
            customers = session.execute(select_query).fetchall()
            for customer in customers:
                session.delete(customer[0])

            session.commit()