from sqlalchemy import String, Float, Integer, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class OrderOfOperationBase(DeclarativeBase):
    pass

class OrderOfOperationEntity(OrderOfOperationBase):
    __tablename__ = 'order_of_operation'

    id:                Mapped[int]            = mapped_column(primary_key=True, autoincrement=True)
    code:              Mapped[str]            = mapped_column(String(200))
    weight_per_piece:  Mapped[float]          = mapped_column(Float)
    customer_id:       Mapped[int]            = mapped_column(Integer)
    total_weight:      Mapped[float]          = mapped_column(Float)
    wire_id:           Mapped[str]            = mapped_column(Text)



    def __repr__(self):
        return f"OrderOfOperationModel(f{self.id=}, {self.code=})"