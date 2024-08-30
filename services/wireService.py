from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from utils.connDB import ConnectDB
from utils.libs import Libs
from schemas.wireSchema import WireSchema, WireUpdate
from entities.wireEntity import WireEntity

conn = ConnectDB()
Session = sessionmaker(bind=conn.engine)
session = Session()

class WireService:
    def __init__(self):
        self.lib = Libs()

    def getAllWires(self):
        try:
            select_query = select(WireEntity)
            all_wires = session.execute(select_query).fetchall()
            all_wires = [wire[0] for wire in all_wires]
            all_wires = [
                {
                    "id": wire.id,
                    "name": wire.name,
                    "description": wire.description,
                    "percentage": wire.percentage
                }
                for wire in all_wires
            ]
            return all_wires
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()
        
    def getWireById(self, id):
        try:
            select_query = select(WireEntity).filter_by(id=id)
            wire = session.execute(select_query).fetchall()
            return wire[0][0]
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def createWire(self, wire: WireSchema):
        try:
            wire_entity = WireEntity(name=wire.name, description=wire.description)
            session.add(wire_entity)
            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def updateWire(self, id, wireSchema: WireUpdate):
        try:
            select_query = select(WireEntity).filter_by(id=id)
            wires = session.execute(select_query).fetchall()
            for wire in wires:
                for key, value in wireSchema.dict(exclude_unset=True).items():
                    setattr(wire[0], key, value)

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def deleteWire(self, id):
        try:
            select_query = select(WireEntity).filter_by(id=id)
            wires = session.execute(select_query).fetchall()
            for wire in wires:
                session.delete(wire[0])

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()