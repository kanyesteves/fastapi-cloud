from sqlalchemy import select
from sqlalchemy.orm import Session
from utils.connDB import ConnectDB
from utils.libs import Libs
from schemas.operatorSchema import OperatorSchema, OperatorUpdate
from entities.operatorEntity import OperatorEntity

conn = ConnectDB()

class OperatorService:
    def __init__(self):
        self.lib = Libs()

    def getAllOperators(self):
        with Session(bind=conn.engine) as session:
            select_query = select(OperatorEntity)
            all_operators = session.execute(select_query).fetchall()
            all_operators = [tear[0] for tear in all_operators]
            all_operators = [
                {
                    "id": operator.id,
                    "name": operator.name,
                    "office": operator.office,
                }
                for operator in all_operators
            ]
            return all_operators
        
    def getOperatorById(self, id):
        with Session(bind=conn.engine) as session:
            select_query = select(OperatorEntity).filter_by(id=id)
            operator = session.execute(select_query).fetchall()
            return operator[0][0]

    def createOperator(self, operator: OperatorSchema):
        with Session(bind=conn.engine) as session:
            operator_entity = OperatorEntity(name=operator.name, office=operator.office)
            session.add(operator_entity)
            session.commit()

    def updateOperator(self, id, operatorSchema: OperatorUpdate):
        with Session(bind=conn.engine) as session:
            select_query = select(OperatorEntity).filter_by(id=id)
            operators = session.execute(select_query).fetchall()
            for operator in operators:
                for key, value in operatorSchema.dict(exclude_unset=True).items():
                    setattr(operator[0], key, value)

            session.commit()

    def deleteOperator(self, id):
        with Session(bind=conn.engine) as session:
            select_query = select(OperatorEntity).filter_by(id=id)
            operators = session.execute(select_query).fetchall()
            for operator in operators:
                session.delete(operator[0])

            session.commit()