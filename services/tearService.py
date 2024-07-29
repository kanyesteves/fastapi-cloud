from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from utils.connDB import ConnectDB
from utils.libs import Libs
from schemas.tearSchema import TearSchema, TearUpdate
from entities.tearEntity import TearEntity

conn = ConnectDB()
Session = sessionmaker(bind=conn.engine)
session = Session()

class TearService:
    def __init__(self):
        self.lib = Libs()

    def getAllTeares(self):
        try:
            select_query = select(TearEntity)
            all_tear = session.execute(select_query).fetchall()
            all_tear = [tear[0] for tear in all_tear]
            all_tear = [
                {
                    "id": tear.id,
                    "name": tear.name,
                    "model": tear.model,
                    "status": tear.status,
                }
                for tear in all_tear
            ]
            return all_tear
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()
        
    def getTearById(self, id):
        try:
            select_query = select(TearEntity).filter_by(id=id)
            tear = session.execute(select_query).fetchall()
            return tear[0][0]
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def createTear(self, tear: TearSchema):
        try:
            tear_entity = TearEntity(name=tear.name, model=tear.model, status=tear.status)
            session.add(tear_entity)
            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def updateTear(self, id, tearSchema: TearUpdate):
        try:
            select_query = select(TearEntity).filter_by(id=id)
            teares = session.execute(select_query).fetchall()
            for tear in teares:
                for key, value in tearSchema.dict(exclude_unset=True).items():
                    setattr(tear[0], key, value)

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def deleteTear(self, id):
        try:
            select_query = select(TearEntity).filter_by(id=id)
            teares = session.execute(select_query).fetchall()
            for tear in teares:
                session.delete(tear[0])

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()