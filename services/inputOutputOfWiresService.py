from utils.libs import Libs
from datetime import datetime
from sqlalchemy import select
from utils.connDB import ConnectDB
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker
from entities.inputOutputOfWiresEntity import InputOutputOfWiresEntity
from schemas.inputOutputOfWiresSchema import InputOutputOfWiresSchema

conn = ConnectDB()
Session = sessionmaker(bind=conn.engine)
session = Session()

class InputOutputOfWiresService:
    def __init__(self):
        self.lib = Libs()

    def getAllInputOutputOfWires(self):
        try:
            select_query = select(InputOutputOfWiresEntity)
            all_inputOutputOfWires = session.execute(select_query).fetchall()
            all_inputOutputOfWires = [inputOutputOfWire[0] for inputOutputOfWire in all_inputOutputOfWires]
            all_inputOutputOfWires = [
                {
                    "id": inputOutputOfWire.id,
                    "name": inputOutputOfWire.name,
                    "weight": inputOutputOfWire.weight,
                    "type_register": inputOutputOfWire.type_register,
                    "fiscal_note": inputOutputOfWire.fiscal_note,
                    "date_open": inputOutputOfWire.date_open
                }
                for inputOutputOfWire in all_inputOutputOfWires
            ]
            return all_inputOutputOfWires
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()
        
    def getInputOutputOfWiresById(self, id):
        try:
            select_query = select(InputOutputOfWiresEntity).filter_by(id=id)
            inputOutputOfWires = session.execute(select_query).fetchall()
            return inputOutputOfWires[0][0]
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()
