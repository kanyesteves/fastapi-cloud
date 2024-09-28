from utils.libs import Libs
from sqlalchemy import select, delete
from utils.connDB import ConnectDB
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from schemas.programingSchema import ProgramingSchema
from entities.programingHasTearEntity import ProgramingHasTearEntity
from entities.programingHasOpEntity import ProgramingHasOpEntity
from entities.programingEntity import ProgramingEntity
from entities.tearEntity import TearEntity
from entities.orderOfOperationEntity import OrderOfOperationEntity

conn = ConnectDB()
Session = sessionmaker(bind=conn.engine)
session = Session()

class ProgramingService:
    def __init__(self):
        self.lib = Libs()

    def getAllPrograming(self):
        try:
            select_query = select(ProgramingEntity)
            all_programing = session.execute(select_query).fetchall()
            all_programing = [programing[0] for programing in all_programing]
            all_programing = [
                {
                    "id": programing.id,
                    "name": programing.name,
                    "tear": self.getTearHasPrograming(programing.id),
                    "op": self.getOpHasPrograming(programing.id)
                }
                for programing in all_programing
            ]
            return all_programing
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()
    
    def getProgramingById(self, id):
        try:
            select_query = select(ProgramingEntity).filter_by(id=id)
            all_programing = session.execute(select_query).fetchall()
            all_programing = [programing[0] for programing in all_programing]
            all_programing = [
                {
                    "id": programing.id,
                    "name": programing.name,
                    "tear": self.getTearHasPrograming(programing.id),
                    "op": self.getOpHasPrograming(programing.id)
                }
                for programing in all_programing
            ]
            return all_programing
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def createPrograming(self, programing: ProgramingSchema):
        try:
            programing_entity = ProgramingEntity(name=programing.name)
            session.add(programing_entity)
            session.commit()
            last_id = programing_entity.id

            relation_has_tear = ProgramingHasTearEntity(programing_id=last_id, tear_id=programing.tear)
            session.add(relation_has_tear)
            session.commit()

            relation_has_op = ProgramingHasOpEntity(programing_id=last_id, op_id=programing.op)
            session.add(relation_has_op)
            session.commit()

        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def deletePrograming(self, id):
        try:
            select_query = select(ProgramingEntity).filter_by(id=id)
            programings = session.execute(select_query).fetchall()
            for programing in programings:
                session.delete(programing[0])

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

# ----------------- Métodos de relacionamento
    def getTearHasPrograming(self, programing_id):
        try:
            select_query = (
                select(TearEntity)
                .join(ProgramingHasTearEntity, TearEntity.id == ProgramingHasTearEntity.tear_id)
                .filter(ProgramingHasTearEntity.programing_id == programing_id)
            )
            teares = session.execute(select_query).fetchall()
            teares = [tear[0] for tear in teares]
            teares = [
                {
                    "id": tear.id,
                    "name": tear.name,
                    "status": tear.status,
                    "model": tear.model,
                }
                for tear in teares
            ]
            return teares
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def getOpHasPrograming(self, programing_id):
        try:
            select_query = (
                select(OrderOfOperationEntity)
                .join(ProgramingHasOpEntity, OrderOfOperationEntity.id == ProgramingHasOpEntity.op_id)
                .filter(ProgramingHasOpEntity.programing_id == programing_id)
            )
            ops = session.execute(select_query).fetchall()
            ops = [op[0] for op in ops]
            ops = [
                {
                    "id": op.id,
                    "code": op.code,
                    "weight_per_piece": op.weight_per_piece,
                    "total_weight": op.total_weight,
                    "total_pieces": op.total_pieces,
                    "status": op.status,
                    "label_item": op.label_item,
                }
                for op in ops
            ]
            return ops
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()