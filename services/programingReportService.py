from utils.libs import Libs
from datetime import datetime
from sqlalchemy import select
from utils.connDB import ConnectDB
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker
from entities.programingReportEntity import ProgramingReportEntity
from schemas.programingReportSchema import ProgramingReportSchema

conn = ConnectDB()
Session = sessionmaker(bind=conn.engine)
session = Session()

class ProgramingReportService:
    def __init__(self):
        self.lib = Libs()

    def getAllProgramingReport(self):
        try:
            select_query = select(ProgramingReportEntity)
            all_programing_report = session.execute(select_query).fetchall()
            all_programing_report = [programing_report[0] for programing_report in all_programing_report]
            all_programing_report = [
                {
                    "id": programing_report.id,
                    "name": programing_report.name,
                    "rpm": programing_report.rpm,
                    "op": programing_report.op,
                    "tear": programing_report.tear,
                    "date_start": programing_report.date_start,
                    "date_end": programing_report.date_end,
                    "efficiency": programing_report.efficiency,
                    "weight_daily": programing_report.weight_daily,
                    "days_for_done": programing_report.days_for_done,
                    "type_register": programing_report.type
                }
                for programing_report in all_programing_report
            ]
            return all_programing_report
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()
        
    def getProgramingReportById(self, id):
        try:
            select_query = select(ProgramingReportEntity).filter_by(id=id)
            programing_report = session.execute(select_query).fetchall()
            return programing_report[0][0]
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()
