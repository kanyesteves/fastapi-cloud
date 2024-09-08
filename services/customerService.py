import json
from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from utils.connDB import ConnectDB
from utils.libs import Libs
from schemas.customerSchema import CustomerSchema, CustomerUpdate
from entities.customerEntity import CustomerEntity

conn = ConnectDB()
Session = sessionmaker(bind=conn.engine)
session = Session()

class CustomerService:
    def __init__(self):
        self.lib = Libs()

    def getAllCustomers(self):
        try:
            select_query = select(CustomerEntity)
            all_customers = session.execute(select_query).fetchall()
            all_customers = [customer[0] for customer in all_customers]
            all_customers = [
                {
                    "id": customer.id,
                    "name": customer.name,
                    "description": customer.description,
                }
                for customer in all_customers
            ]
            return all_customers
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()
        
    def getCustomerById(self, id):
        try:
            select_query = select(CustomerEntity).filter_by(id=id)
            customer = session.execute(select_query).fetchall()
            return customer[0][0]
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def createCustomer(self, customer: CustomerSchema):
        try:
            customer_entity = CustomerEntity(name=customer.name, description=customer.description)
            session.add(customer_entity)
            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def updateCustomer(self, id, customerSchema: CustomerUpdate):
        try:
            select_query = select(CustomerEntity).filter_by(id=id)
            customers = session.execute(select_query).fetchall()
            for customet in customers:
                for key, value in customerSchema.dict(exclude_unset=True).items():
                    setattr(customet[0], key, value)

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def deleteCustomer(self, id):
        try:
            select_query = select(CustomerEntity).filter_by(id=id)
            customers = session.execute(select_query).fetchall()
            for customer in customers:
                session.delete(customer[0])

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()