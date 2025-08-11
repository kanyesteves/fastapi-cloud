from utils.libs import Libs
from datetime import datetime
from sqlalchemy import select
from utils.connDB import ConnectDB
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from schemas.programingSchema import ProgramingSchema
from entities.programingHasTearEntity import ProgramingHasTearEntity
from entities.programingHasOpEntity import ProgramingHasOpEntity
from entities.programingEntity import ProgramingEntity
from entities.programingReportEntity import ProgramingReportEntity
from entities.tearEntity import TearEntity
from entities.orderOfOperationEntity import OrderOfOperationEntity
from services.orderOfOperationService import OrderOfOperationrService
from services.tearService import TearService

conn = ConnectDB()
Session = sessionmaker(bind=conn.engine)
session = Session()
op_service = OrderOfOperationrService()
tear_service = TearService()

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
                    "date_start": programing.date_start,
                    "date_end": programing.date_end,
                    "rpm": programing.rpm,
                    "efficiency": programing.efficiency,
                    "weight_daily": programing.weight_daily,
                    "days_for_done": programing.days_for_done,
                    "wires": programing.wires,
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
                    "date_start": programing.date_start,
                    "date_end": programing.date_end,
                    "rpm": programing.rpm,
                    "efficiency": programing.efficiency,
                    "weight_daily": programing.weight_daily,
                    "days_for_done": programing.days_for_done,
                    "wires": programing.wires,
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
            programing_entity = ProgramingEntity(
                name=programing.name, 
                date_start=self.formatDate(programing.date_start), 
                date_end=self.formatDate(programing.date_end),
                rpm=programing.rpm,
                efficiency=programing.efficiency,
                weight_daily=programing.weight_daily,
                days_for_done=programing.days_for_done,
                wires=programing.wires)

            session.add(programing_entity)
            session.commit()
            last_id = programing_entity.id

            session.add(ProgramingHasTearEntity(programing_id=last_id, tear_id=programing.tear))
            session.add(ProgramingHasOpEntity(programing_id=last_id, op_id=programing.op))
            session.commit()

            self.createReport(programing, 'create')

        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def deletePrograming(self, id):
        try:
            programing_data = self.getProgramingById(id)
            select_query = select(ProgramingEntity).filter_by(id=id)
            programings = session.execute(select_query).fetchall()
            for programing in programings:
                session.delete(programing[0])

            session.commit()
            
            self.createReport(programing_data, 'remove')
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()


    def createReport(self, programing: ProgramingSchema, input_type: str):
        try:
            print(programing)
            op = op_service.getCodeById(programing.op)
            tear = tear_service.getTearById(programing.tear)

            programing_report = ProgramingReportEntity(
                name=programing.name,
                rpm=programing.rpm,
                op=op['code'],
                tear=tear.name,
                date_start=self.formatDate(programing.date_start),
                date_end=self.formatDate(programing.date_end),
                efficiency=programing.efficiency,
                weight_daily=programing.weight_daily,
                days_for_done=programing.days_for_done,
                type_register=input_type
            )
            session.add(programing_report)
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


    def formatDate(self, date):
        date_aux = date
        input_format = "%Y-%m-%dT%H:%M:%S.%fZ"
        date_ok = datetime.strptime(date_aux, input_format)

        format_out = "%Y-%m-%d"
        return date_ok.strftime(format_out)