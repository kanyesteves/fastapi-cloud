from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from entities.orderOfOperationEntity import OrderOfOperationEntity
from entities.wireEntity import WireEntity

class OpHasWiresBase(DeclarativeBase):
    pass

class OpHasWiresEntity(OpHasWiresBase):
    __tablename__ = 'op_has_wires'

    id:           Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    op_id:        Mapped[int] = mapped_column(Integer, ForeignKey(OrderOfOperationEntity.id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    wire_id:      Mapped[int] = mapped_column(Integer, ForeignKey(WireEntity.id,             ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    def __repr__(self):
        return f"OpHasWiresModel(id={self.id}, op_id={self.op_id}, wire_id={self.wire_id})"