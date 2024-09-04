from sqlalchemy import String, Float, Date, JSON, Integer, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class ProductionBase(DeclarativeBase):
    pass

class ProductionEntity(ProductionBase):
    __tablename__ = 'productions'

    id:                Mapped[int]            = mapped_column(primary_key=True, autoincrement=True)
    code_per_piece:    Mapped[int]            = mapped_column(Integer)
    weight:            Mapped[float]          = mapped_column(Float)
    review:            Mapped[str]            = mapped_column(String(200))
    invoiced:          Mapped[bool]           = mapped_column(Boolean)
    date:              Mapped[str]            = mapped_column(Date)
    tear:              Mapped[dict]           = mapped_column(JSON)
    op:                Mapped[dict]           = mapped_column(JSON)
    operator:          Mapped[dict]           = mapped_column(JSON)
    


    def __repr__(self):
        return f"ProductionModel(f{self.id=}, {self.code=})"