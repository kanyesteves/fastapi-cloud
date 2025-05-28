from sqlalchemy import String, Date, Float, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class ProgramingBase(DeclarativeBase):
    pass

class ProgramingEntity(ProgramingBase):
    __tablename__ = 'programing'

    id:             Mapped[int]     = mapped_column(primary_key=True, autoincrement=True)
    name:           Mapped[str]     = mapped_column(String(100))
    date_start:     Mapped[str]     = mapped_column(Date)
    date_end:       Mapped[str]     = mapped_column(Date)
    rpm:            Mapped[float]   = mapped_column(Float)
    efficiency:     Mapped[float]   = mapped_column(Float)
    weight_daily:   Mapped[float]   = mapped_column(Float)
    days_for_done:  Mapped[float]   = mapped_column(Float)
    wires:          Mapped[dict]    = mapped_column(JSON)

    def __repr__(self):
        return f"ProgramingModel(f{self.id=}, {self.name=})"