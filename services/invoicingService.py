import pdfkit, os
from utils.libs import Libs
from datetime import datetime
from sqlalchemy import select
from utils.connDB import ConnectDB
from sqlalchemy.exc import SQLAlchemyError
from services.wireService import WireService
from jinja2 import Environment, FileSystemLoader
from sqlalchemy.orm import Session, sessionmaker
from schemas.invoicingSchema import InvoicingSchema
from entities.invoicingEntity import InvoicingEntity
from entities.productionEntity import ProductionEntity
from entities.wireEntity import WireEntity


wire_service = WireService()
conn = ConnectDB()
Session = sessionmaker(bind=conn.engine)
session = Session()

class InvoicingService:
    def __init__(self):
        self.lib = Libs()

    def getAllInvoicings(self):
        try:
            select_query = select(InvoicingEntity)
            all_invoicing = session.execute(select_query).fetchall()
            all_invoicing = [invoicing[0] for invoicing in all_invoicing]
            all_invoicing = [
                {
                    "id": invoicing.id,
                    "records": invoicing.records,
                    "weight_per_wire": invoicing.weight_per_wire,
                    "total_weight": invoicing.total_weight,
                    "date": invoicing.date,
                    "customer": invoicing.customer,
                    "article": invoicing.article,
                    "op": invoicing.op
                }
                for invoicing in all_invoicing
            ]
            return all_invoicing
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def getInvoicingById(self, id):
        try:
            select_query = select(InvoicingEntity).filter_by(id=id)
            invoicing = session.execute(select_query).fetchall()
            return invoicing[0][0]
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def createInvoicing(self, invoicing: InvoicingSchema):
        try:
            for record in invoicing.records:
                session.query(ProductionEntity).filter(ProductionEntity.id == record['id']).update({"invoiced": True})
                session.commit()

            for wire in list(invoicing.weight_per_wire):
                weight = float(wire["weight"])
                wire_aux = wire_service.getWireByName(wire["name"])
                wire_aux.weight = wire_aux.weight - weight
                session.query(WireEntity).filter(WireEntity.id == wire_aux.id).update({"weight": wire_aux.weight})
                session.commit()
 
            invoicing_entity = InvoicingEntity(
                                    records=invoicing.records, 
                                    total_weight=invoicing.total_weight, 
                                    date=datetime.now(), 
                                    customer=invoicing.customer,
                                    article=invoicing.article,
                                    op=invoicing.op,
                                    weight_per_wire=invoicing.weight_per_wire)
            session.add(invoicing_entity)
            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def generatePDF(self, invoicing: InvoicingSchema):

        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template("invoicing_template.html")
        html_content = template.render(invoicing=invoicing)

        config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
        pdf_path = f"/tmp/invoice_{invoicing.customer}_{invoicing.op}.pdf"
        
        try:
            pdfkit.from_string(html_content, pdf_path, configuration=config)
        except Exception as e:
            print(f"Erro ao gerar o PDF: {e}")
            raise

        if os.path.exists(pdf_path):
            return pdf_path
        else:
            print("Erro: o arquivo PDF não foi encontrado.")
            raise FileNotFoundError("O arquivo PDF não foi criado.")

            return pdf_path