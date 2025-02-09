from sqlalchemy import String, Float, Date, JSON, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class InvoicingBase(DeclarativeBase):
    pass

class InvoicingEntity(InvoicingBase):
    __tablename__ = 'invoicing'

    id:                Mapped[int]           = mapped_column(primary_key=True, autoincrement=True)
    records:           Mapped[dict]          = mapped_column(JSON)
    weight_per_wire:   Mapped[dict]          = mapped_column(JSON)
    total_weight:      Mapped[float]         = mapped_column(Float)
    date:              Mapped[str]           = mapped_column(Date)
    customer:          Mapped[str]           = mapped_column(String(50))
    article:           Mapped[str]           = mapped_column(String(50))
    op:                Mapped[str]           = mapped_column(String(50))
    volume:            Mapped[int]           = mapped_column(Integer)

    def __repr__(self):
        return f"InvoicingModel(f{self.id=}, {self.customer=})"