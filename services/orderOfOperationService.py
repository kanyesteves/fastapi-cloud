from datetime import datetime
from utils.libs import Libs
from sqlalchemy import select, delete
from utils.connDB import ConnectDB
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from schemas.orderOfOperationSchema import OrderOfOperationSchema, OrderOfOperationUpdate
from entities.orderOfOperationEntity import OrderOfOperationEntity
from entities.opHasCustomerEntity import OpHasCustomerEntity
from entities.opHasArticleEntity import OpHasArticleEntity
from entities.opHasWiresEntity import OpHasWiresEntity
from entities.customerEntity import CustomerEntity
from entities.articleEntity import ArticleEntity
from entities.wireEntity import WireEntity

conn = ConnectDB()
Session = sessionmaker(bind=conn.engine)
session = Session()

class OrderOfOperationrService:
    def __init__(self):
        self.lib = Libs()

    def getAllOPs(self):
        try:
            select_query = select(OrderOfOperationEntity)
            all_ops = session.execute(select_query).fetchall()
            all_ops = [op[0] for op in all_ops]
            all_ops = [
                {
                    "id": op.id,
                    "code": op.code,
                    "weight_per_piece": op.weight_per_piece,
                    "total_weight": op.total_weight,
                    "total_pieces": op.total_pieces,
                    "status": op.status,
                    "label_item": op.label_item,
                    "customer": self.getCustomerHasOp(op.id),
                    "article": self.getArticleHasOp(op.id),
                    "wires": self.getWiresHasOp(op.id)
                }
                for op in all_ops
            ]
            return all_ops
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()
    
    def getAllOpenAndInProgress(self):
        try:
            select_query = select(OrderOfOperationEntity).filter(
                OrderOfOperationEntity.status.in_(['open', 'in_progress'])
            )
            all_ops = session.execute(select_query).fetchall()
            all_ops = [op[0] for op in all_ops]
            all_ops = [
                {
                    "id": op.id,
                    "code": op.code,
                    "weight_per_piece": op.weight_per_piece,
                    "total_weight": op.total_weight,
                    "total_pieces": op.total_pieces,
                    "status": op.status,
                    "label_item": op.label_item,
                    "customer": self.getCustomerHasOp(op.id),
                    "article": self.getArticleHasOp(op.id),
                    "wires": self.getWiresHasOp(op.id)
                }
                for op in all_ops
            ]
            return all_ops
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()
        
    def getOPById(self, id):
        try:
            select_query = select(OrderOfOperationEntity).filter_by(id=id)
            ops = session.execute(select_query).fetchall()
            ops = [op[0] for op in ops]
            op = [
                {
                    "id": op.id,
                    "code": op.code,
                    "weight_per_piece": op.weight_per_piece,
                    "total_weight": op.total_weight,
                    "total_pieces": op.total_pieces,
                    "status": op.status,
                    "label_item": op.label_item,
                    "customer": self.getCustomerHasOp(op.id),
                    "article": self.getArticleHasOp(op.id),
                    "wires": self.getWiresHasOp(op.id)
                }
                for op in ops
            ]
            return op[0]
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def createOP(self, op: OrderOfOperationSchema):
        try:
            op_entity = OrderOfOperationEntity(
                                        code=op.code,
                                        weight_per_piece=op.weight_per_piece,
                                        label_item=op.label_item,
                                        total_weight=op.total_weight,
                                        total_pieces=op.total_pieces,
                                        status='open')
            session.add(op_entity)
            session.commit()
            last_id = op_entity.id

            relation_has_customer = OpHasCustomerEntity(op_id=last_id, customer_id=op.customer)
            session.add(relation_has_customer)
            session.commit()

            relation_has_article = OpHasArticleEntity(op_id=last_id, article_id=op.article)
            session.add(relation_has_article)
            session.commit()

            for wire_id in op.wires:
                relation_has_wires = OpHasWiresEntity(op_id=last_id, wire_id=wire_id)
                session.add(relation_has_wires)
                session.commit()

        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def updateOP(self, id, orderOfOperationsSchema: OrderOfOperationUpdate):
        try:
            self.updateCustomerHasOp(id, orderOfOperationsSchema.customer)
            self.updateArticleHasOp(id, orderOfOperationsSchema.article)
            self.updateWiresHasOp(id, orderOfOperationsSchema.wires)

            select_query = select(OrderOfOperationEntity).filter_by(id=id)
            ops = session.execute(select_query).fetchall()
            for op in ops:
                for key, value in orderOfOperationsSchema.dict(exclude_unset=True).items():
                    setattr(op[0], key, value)

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def closeOP(self, id):
        try:
            select_query = select(OrderOfOperationEntity).filter_by(id=id)
            ops = session.execute(select_query).fetchall()
            for op in ops:
                setattr(op[0], 'status', 'closed')
                setattr(op[0], 'date_closed', datetime.now())

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

# ----------------- Métodos de relacionamento
    def updateCustomerHasOp(self, op_id, customer_id):
        select_query = select(OpHasCustomerEntity).filter_by(op_id=op_id, customer_id=customer_id)
        existing_relation = session.execute(select_query).scalar()

        if not existing_relation:
            new_relation = OpHasCustomerEntity(op_id=op_id, customer_id=customer_id)
            session.add(new_relation)
            session.commit()

    def updateArticleHasOp(self, op_id, article_id):
        select_query = select(OpHasArticleEntity).filter_by(op_id=op_id, article_id=article_id)
        existing_relation = session.execute(select_query).scalar()

        if not existing_relation:
            new_relation = OpHasArticleEntity(op_id=op_id, article_id=article_id)
            session.add(new_relation)
            session.commit()

    def updateWiresHasOp(self, op_id, wires_id):
        try:
            select_query = select(OpHasWiresEntity).filter_by(op_id=op_id)
            relations_with_wires = session.execute(select_query).fetchall()
            relations_with_wires = [ wire[0] for wire in relations_with_wires ]

            existing_wire_ids = { relation.wire_id for relation in relations_with_wires }
            new_wire_ids = set(wires_id)

            wires_to_remove = existing_wire_ids - new_wire_ids
            wires_to_add = new_wire_ids - existing_wire_ids

            if wires_to_remove:
                delete_query = delete(OpHasWiresEntity).where(
                    OpHasWiresEntity.op_id == op_id,
                    OpHasWiresEntity.wire_id.in_(wires_to_remove)
                )
                session.execute(delete_query)

            for wire_id in wires_to_add:
                new_relation = OpHasWiresEntity(op_id=op_id, wire_id=wire_id)
                session.add(new_relation)

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def getCustomerHasOp(self, op_id):
        try:
            select_query = (
                select(CustomerEntity)
                .join(OpHasCustomerEntity, CustomerEntity.id == OpHasCustomerEntity.customer_id)
                .filter(OpHasCustomerEntity.op_id == op_id)
            )
            customers = session.execute(select_query).fetchall()
            customers = [customer[0] for customer in customers]
            customers = [
                {
                    "id": customer.id,
                    "name": customer.name,
                    "description": customer.description,
                }
                for customer in customers
            ]
            return customers
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def getArticleHasOp(self, op_id):
        try:
            select_query = (
                select(ArticleEntity)
                .join(OpHasArticleEntity, ArticleEntity.id == OpHasArticleEntity.article_id)
                .filter(OpHasArticleEntity.op_id == op_id)
            )
            articles = session.execute(select_query).fetchall()
            articles = [article[0] for article in articles]
            articles = [
                {
                    "id": article.id,
                    "name": article.name,
                    "description": article.description,
                }
                for article in articles
            ]
            return articles
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def getWiresHasOp(self, op_id):
        try:
            select_query = (
                select(WireEntity)
                .join(OpHasWiresEntity, WireEntity.id == OpHasWiresEntity.wire_id)
                .filter(OpHasWiresEntity.op_id == op_id)
            )
            wires = session.execute(select_query).fetchall()
            wires = [wire[0] for wire in wires]
            wires = [
                {
                    "id": wire.id,
                    "name": wire.name,
                    "description": wire.description,
                    "percentage": wire.percentage,
                }
                for wire in wires
            ]
            return wires
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

