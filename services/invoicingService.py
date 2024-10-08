from datetime import datetime
from utils.libs import Libs
from sqlalchemy import select
from utils.connDB import ConnectDB
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from schemas.invoicingSchema import InvoicingSchema
from entities.invoicingEntity import InvoicingEntity
from entities.productionEntity import ProductionEntity


conn = ConnectDB()
Session = sessionmaker(bind=conn.engine)
session = Session()

class InvoicingService:
    def __init__(self):
        self.lib = Libs()

    def getAllInvoicings(self):
        try:
            select_query = select(InvoicingEntity)
            all_invoicing = session.execute(select_query).fetchall()
            all_invoicing = [invoicing[0] for invoicing in all_invoicing]
            all_invoicing = [
                {
                    "id": invoicing.id,
                    "records": invoicing.records,
                    "weight_per_wire": invoicing.weight_per_wire,
                    "total_weight": invoicing.total_weight,
                    "date": invoicing.date,
                    "customer": invoicing.customer,
                    "article": invoicing.article,
                    "op": invoicing.op
                }
                for invoicing in all_invoicing
            ]
            return all_invoicing
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def getInvoicingById(self, id):
        try:
            select_query = select(InvoicingEntity).filter_by(id=id)
            invoicing = session.execute(select_query).fetchall()
            return invoicing[0][0]
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def createInvoicing(self, invoicing: InvoicingSchema):
        try:
            for record in invoicing.records:
                session.query(ProductionEntity).filter(ProductionEntity.id == record['id']).update({"invoiced": True})
                session.commit()

            invoicing_entity = InvoicingEntity(
                                    records=invoicing.records, 
                                    total_weight=invoicing.total_weight, 
                                    date=datetime.now(), 
                                    customer=invoicing.customer,
                                    article=invoicing.article,
                                    op=invoicing.op,
                                    weight_per_wire=invoicing.weight_per_wire)
            session.add(invoicing_entity)
            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()