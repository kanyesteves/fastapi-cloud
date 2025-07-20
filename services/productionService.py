from datetime import datetime
from utils.libs import Libs
from sqlalchemy import select, desc, func, and_
from utils.connDB import ConnectDB
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from schemas.productionSchema import ProductionSchema, ProductionUpdate
from entities.productionEntity import ProductionEntity
from entities.orderOfOperationEntity import OrderOfOperationEntity

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

    def getAllRecordsByOp(self, op: str):
        try:
            select_query = select(ProductionEntity).filter(and_(
                ProductionEntity.op == op,
                ProductionEntity.invoiced == False,
                ProductionEntity.second_quality == '1º'
            ))
            all_records = session.execute(select_query).fetchall()
            all_records = [record[0] for record in all_records]
            all_records = [
            {
                "id": record.id,
                "code_per_piece": record.code_per_piece,
                "weight": record.weight,
                "review": record.review,
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

    def getLastRecordByOp(self, op: str):
        try:
            select_query = select(ProductionEntity).filter(and_(   
                ProductionEntity.op == op,
                ProductionEntity.second_quality == '1º'
            )).order_by(
                desc(ProductionEntity.code_per_piece)
            ).limit(1)
            all_records = session.execute(select_query).fetchall()
            all_records = [record[0] for record in all_records]
            all_records = [
            {
                "id": record.id,
                "code_per_piece": record.code_per_piece,
                "weight": record.weight,
                "review": record.review,
                "invoiced": record.invoiced,
                "date": record.date,
                "tear": record.tear,
                "operator": record.operator,
                "op": record.op
            }
                for record in all_records
            ]
            return all_records[0]
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def getLast3Records(self):
        try:
            select_query = select(ProductionEntity).order_by(
                desc(ProductionEntity.id)
            ).limit(3)
            all_records = session.execute(select_query).fetchall()
            all_records = [record[0] for record in all_records]
            all_records = [
            {
                "id": record.id,
                "code_per_piece": record.code_per_piece,
                "weight": record.weight,
                "review": record.review,
                "invoiced": record.invoiced,
                "date": record.date,
                "tear": record.tear,
                "operator": record.operator,
                "op": record.op,
                "second_quality": record.second_quality
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
            record_entity = ProductionEntity(
                                    code_per_piece=record.code_per_piece, 
                                    weight=record.weight, 
                                    review=record.review, 
                                    invoiced=False,
                                    date=datetime.now(),
                                    tear=record.tear,
                                    op=record.op,
                                    operator=record.operator,
                                    second_quality=record.second_quality)
            session.add(record_entity)
            session.commit()

            if record.code_per_piece == 1:
                session.query(OrderOfOperationEntity).filter(OrderOfOperationEntity.code == record.op).update({"status": "in_progress"})
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

    def getTotalWeight(self, op: str):
        try:
            query = select(func.sum(ProductionEntity.weight)).filter(and_(
                ProductionEntity.op == op,
                ProductionEntity.second_quality == '1º'
            ))
            total_weight = session.execute(query).scalar()

            if total_weight is None: 
                total_weight = 0

            return total_weight
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def getTotalPieces(self, op: str):
        try:
            total_count = (
                session.query(func.count(ProductionEntity.id))
                .filter(and_(
                    ProductionEntity.op == op,
                    ProductionEntity.second_quality == '1º'
                ))
                .scalar()
            )
            return total_count
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def getTotalInvoiced(self, op: str):
        try:
            totalInvoiced = (
                session.query(func.count(ProductionEntity.id))
                .filter(and_(
                    ProductionEntity.op == op,
                    ProductionEntity.invoiced == True,
                    ProductionEntity.second_quality == '1º'
                ))
                .scalar()
            )
            return totalInvoiced
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def getTotalSecondQuality(self, op: str):
        try:
            query = select(func.sum(ProductionEntity.weight)).filter(and_(
                ProductionEntity.op == op,
                ProductionEntity.second_quality == '2º'
            ))
            total_weight = session.execute(query).scalar()

            if total_weight is None: 
                total_weight = 0

            return total_weight
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()