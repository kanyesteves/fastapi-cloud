from utils.libs import Libs
from sqlalchemy import select
from utils.connDB import ConnectDB
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from schemas.orderOfOperationSchema import OrderOfOperationSchema, OrderOfOperationUpdate
from entities.orderOfOperationEntity import OrderOfOperationEntity

conn = ConnectDB()
Session = sessionmaker(bind=conn.engine)
session = Session()

class OrderOfOperationrService:
    def __init__(self):
        self.lib = Libs()

    def getAllOPs(self):
        try:
            select_query = select(OrderOfOperationEntity)
            all_ops = session.execute(select_query).fetchall()
            all_ops = [op[0] for op in all_ops]
            all_ops = [
                {
                    "id": op.id,
                    "code": op.code,
                    "weight_per_piece": op.weight_per_piece,
                    "customer_id": op.customer_id,
                    "total_weight": op.total_weight,
                    "wire_id": op.wire_id,

                }
                for op in all_ops
            ]
            return all_ops
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()
        
    def getOPById(self, id):
        try:
            select_query = select(OrderOfOperationEntity).filter_by(id=id)
            op = session.execute(select_query).fetchall()
            return op[0][0]
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def createOP(self, op: OrderOfOperationSchema):
        try:
            op_entity = OrderOfOperationEntity(
                                        code=op.code, 
                                        weight_per_piece=op.weight_per_piece, 
                                        customer_id=op.customer_id, 
                                        total_weight=op.total_weight, 
                                        wire_id=op.wire_id)
            session.add(op_entity)
            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def updateOP(self, id, orderOfOperationsSchema: OrderOfOperationUpdate):
        try:
            select_query = select(OrderOfOperationEntity).filter_by(id=id)
            ops = session.execute(select_query).fetchall()
            for op in ops:
                for key, value in orderOfOperationsSchema.dict(exclude_unset=True).items():
                    setattr(op[0], key, value)

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def deleteOP(self, id):
        try:
            select_query = select(OrderOfOperationEntity).filter_by(id=id)
            ops = session.execute(select_query).fetchall()
            for op in ops:
                session.delete(op[0])

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()