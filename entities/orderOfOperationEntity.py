from sqlalchemy import String, Float, Date, JSON, Integer, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class OrderOfOperationBase(DeclarativeBase):
    pass

class OrderOfOperationEntity(OrderOfOperationBase):
    __tablename__ = 'order_of_operation'

    id:                Mapped[int]            = mapped_column(primary_key=True, autoincrement=True)
    code:              Mapped[str]            = mapped_column(String(200))
    weight_per_piece:  Mapped[float]          = mapped_column(Float)
    total_weight:      Mapped[float]          = mapped_column(Float)
    total_pieces:      Mapped[int]            = mapped_column(Integer)
    status:            Mapped[str]            = mapped_column(String(20))
    date_closed:       Mapped[str]            = mapped_column(Date)
    date_open:         Mapped[str]            = mapped_column(Date)
    label_item:        Mapped[bool]           = mapped_column(Boolean, default=False)
    wire_porcentage:   Mapped[dict]            = mapped_column(JSON)

    def __repr__(self):
        return f"OrderOfOperationModel(f{self.id=}, {self.code=})"