from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from entities.orderOfOperationEntity import OrderOfOperationEntity 
from entities.programingEntity import ProgramingEntity

class ProgramingHasOpBase(DeclarativeBase):
    pass

class ProgramingHasOpEntity(ProgramingHasOpBase):
    __tablename__ = 'programing_has_op'

    id:            Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    programing_id: Mapped[int] = mapped_column(Integer, ForeignKey(ProgramingEntity.id,       ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    op_id:         Mapped[int] = mapped_column(Integer, ForeignKey(OrderOfOperationEntity.id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    def __repr__(self):
        return f"ProgramingHasTearModel(id={self.id}, programing_id={self.programing_id}, op_id={self.op_id})"
