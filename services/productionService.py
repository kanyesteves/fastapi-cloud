from datetime import datetime
from utils.libs import Libs
from sqlalchemy import select
from utils.connDB import ConnectDB
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from schemas.productionSchema import ProductionSchema, ProductionUpdate
from schemas.tearSchema import TearPublic
from schemas.operatorSchema import OperatorPublic
from schemas.orderOfOperationSchema import OrderOfOperationPublic
from entities.productionEntity import ProductionEntity

conn = ConnectDB()
Session = sessionmaker(bind=conn.engine)
session = Session()

class ProductionService:
    def __init__(self):
        self.lib = Libs()

    def getAllRecords(self):
        try:
            select_query = select(ProductionEntity)
            all_records = session.execute(select_query).fetchall()
            all_records = [record[0] for record in all_records]
            all_records = [
                {
                "id": record.id,
                "code_per_pice": record.code_per_piece,
                "weight": record.weight,
                "review": record.review,
                "labeled_item": record.labeled_item,
                "invoiced": record.invoiced,
                "date": record.date,
                "tear": record.tear,
                "operator": record.operator,
                "op": record.op
                }
                for record in all_records
            ]
            return all_records
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def getRecordById(self, id):
        try:
            select_query = select(ProductionEntity).filter_by(id=id)
            record = session.execute(select_query).fetchall()
            return record[0][0]
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def createRecord(self, record: ProductionSchema):
        try:
            record = self.schemaForDict(record)
            record_entity = ProductionEntity(
                                    code_per_piece=record.code_per_piece, 
                                    weight=record.weight, 
                                    review=record.review, 
                                    labeled_item=record.labeled_item, 
                                    invoiced=record.invoiced,
                                    date=datetime.now(),
                                    tear=record.tear,
                                    op=record.op,
                                    operator=record.operator)
            session.add(record_entity)
            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def updateRecord(self, id, record: ProductionUpdate):
        try:
            select_query = select(ProductionEntity).filter_by(id=id)
            records = session.execute(select_query).fetchall()
            for record in records:
                for key, value in record.dict(exclude_unset=True).items():
                    setattr(record[0], key, value)

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def schemaForDict(self, record: ProductionSchema):
        if record.tear:
            record.tear = record.tear.dict() if isinstance(record.tear, TearPublic) else record.tear

        if record.op:
            record.op = record.op.dict() if isinstance(record.op, OrderOfOperationPublic) else record.op

        if record.operator:
            record.operator = record.operator.dict() if isinstance(record.operator, OperatorPublic) else record.operator

        return record


    def toInvoice(self, id):
        try:
            select_query = select(ProductionEntity).filter_by(id=id)
            record = session.execute(select_query).fetchall()
            for op in record:
                setattr(op[0], 'status', 'closed')
                setattr(op[0], 'date_closed', datetime.now())

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()