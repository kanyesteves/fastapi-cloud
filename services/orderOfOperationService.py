from sqlalchemy import select
from sqlalchemy.orm import Session
from utils.connDB import ConnectDB
from utils.libs import Libs
from schemas.orderOfOperationSchema import OrderOfOperationrSchema, OrderOfOperationrUpdate
from entities.orderOfOperationEntity import OrderOfOperationrEntity

conn = ConnectDB()

class OrderOfOperationrService:
    def __init__(self):
        self.lib = Libs()

    def getAllOPs(self):
        with Session(bind=conn.engine) as session:
            select_query = select(OrderOfOperationrEntity)
            all_ops = session.execute(select_query).fetchall()
            all_ops = [tear[0] for tear in all_ops]
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
        
    def getOPById(self, id):
        with Session(bind=conn.engine) as session:
            select_query = select(OrderOfOperationrEntity).filter_by(id=id)
            op = session.execute(select_query).fetchall()
            return op[0][0]

    def createOP(self, op: OrderOfOperationrSchema):
        with Session(bind=conn.engine) as session:
            op_entity = OrderOfOperationrEntity(
                                        code=op.code, 
                                        weight_per_piece=op.weight_per_piece, 
                                        customer_id=op.customer_id, 
                                        total_weight=op.total_weight, 
                                        wire_id=op.wire_id)
            session.add(op_entity)
            session.commit()

    def updateOP(self, id, orderOfOperationsSchema: OrderOfOperationrUpdate):
        with Session(bind=conn.engine) as session:
            select_query = select(OrderOfOperationrEntity).filter_by(id=id)
            ops = session.execute(select_query).fetchall()
            for op in ops:
                for key, value in orderOfOperationsSchema.dict(exclude_unset=True).items():
                    setattr(op[0], key, value)

            session.commit()

    def deleteOP(self, id):
        with Session(bind=conn.engine) as session:
            select_query = select(OrderOfOperationrEntity).filter_by(id=id)
            ops = session.execute(select_query).fetchall()
            for op in ops:
                session.delete(op[0])

            session.commit()