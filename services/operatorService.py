from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from utils.connDB import ConnectDB
from utils.libs import Libs
from schemas.operatorSchema import OperatorSchema, OperatorUpdate
from entities.operatorEntity import OperatorEntity

conn = ConnectDB()
Session = sessionmaker(bind=conn.engine)
session = Session()

class OperatorService:
    def __init__(self):
        self.lib = Libs()

    def getAllOperators(self):
        try:
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
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()
        
    def getOperatorById(self, id):
        try:
            select_query = select(OperatorEntity).filter_by(id=id)
            operator = session.execute(select_query).fetchall()
            return operator[0][0]
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def createOperator(self, operator: OperatorSchema):
        try:
            operator_entity = OperatorEntity(name=operator.name, office=operator.office)
            session.add(operator_entity)
            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def updateOperator(self, id, operatorSchema: OperatorUpdate):
        try:
            select_query = select(OperatorEntity).filter_by(id=id)
            operators = session.execute(select_query).fetchall()
            for operator in operators:
                for key, value in operatorSchema.dict(exclude_unset=True).items():
                    setattr(operator[0], key, value)

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def deleteOperator(self, id):
        try:
            select_query = select(OperatorEntity).filter_by(id=id)
            operators = session.execute(select_query).fetchall()
            for operator in operators:
                session.delete(operator[0])

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()