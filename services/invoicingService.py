from io import BytesIO
from utils.libs import Libs
from datetime import datetime
from sqlalchemy import select
from utils.connDB import ConnectDB
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from sqlalchemy.exc import SQLAlchemyError
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session, sessionmaker
from schemas.invoicingSchema import InvoicingSchema
from entities.invoicingEntity import InvoicingEntity
from entities.productionEntity import ProductionEntity


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
        print('Iniciando')

        records = invoicing.records
        total_weight = invoicing.total_weight
        date = datetime.now().strftime("%d-%m-%Y")
        customer = invoicing.customer
        article = invoicing.article
        op = invoicing.op
        weight_per_wire = invoicing.weight_per_wire

        buffer = BytesIO()

        p = canvas.Canvas(buffer, pagesize=A4)
        height = A4
        p.setFont("Helvetica-Bold", 16)
        p.drawString(100, height - 50, "Faturamento")

        p.setFont("Helvetica", 12)
        p.drawString(100, height - 80, f"Cliente: {customer}")
        p.drawString(100, height - 100, f"Artigo: {article}")
        p.drawString(100, height - 120, f"OP: {op}")

        p.drawString(100, height - 160, "Registros:")
        for i, record in enumerate(records):
            p.drawString(100, height - 180 - (i * 20), 
                        f"ID: {record['id']}, Código: {record['code_per_piece']}, "
                        f"Peso: {record['weight']}, Avaliação: {record['review']}, "
                        f"Faturado: {record['invoiced']}, Data: {record['date']}, "
                        f"Tear: {record['tear']}, Operador: {record['operator']}")

        p.drawString(100, height - 220 - (len(records) * 20), "Peso por Fio:")
        for i, wire in enumerate(weight_per_wire, start=1):
            p.drawString(100, height - 220 - (len(records) * 20) - (i * 20), 
                        f"{wire['name']}: {wire['value']}% - {wire['weight']} kg")

        p.drawString(100, height - 280 - (len(records) * 20), f"Peso Total: {total_weight} kg")

        p.showPage()
        p.save()
        buffer.seek(0)

        with open(f"faturamento_{customer}_{article}_{date}.pdf", "wb") as f:
            f.write(buffer.getvalue())

        print("PDF gerado e salvo localmente.")

        return StreamingResponse(buffer, media_type="application/pdf",
                                headers={"Content-Disposition": f"attachment; filename=faturamento_{customer}_{article}_{date}.pdf"})