from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from entities.orderOfOperationEntity import OrderOfOperationEntity
from entities.customerEntity import CustomerEntity

class OpHasCustomerBase(DeclarativeBase):
    pass

class OpHasCustomerEntity(OpHasCustomerBase):
    __tablename__ = 'op_has_customer'

    id:           Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    op_id:        Mapped[int] = mapped_column(Integer, ForeignKey(OrderOfOperationEntity.id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    customer_id:  Mapped[int] = mapped_column(Integer, ForeignKey(CustomerEntity.id,         ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    def __repr__(self):
        return f"OpHasCustomerModel(id={self.id}, op_id={self.op_id}, customer_id={self.customer_id})"
