from sqlalchemy import String, Float, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class ProgramingReportBase(DeclarativeBase):
    pass

class ProgramingReportEntity(ProgramingReportBase):
    __tablename__ = 'programing_report'

    id:             Mapped[int]   = mapped_column(primary_key=True, autoincrement=True)
    name:           Mapped[str]   = mapped_column(String(100))
    rpm:            Mapped[float] = mapped_column(Float)
    op:             Mapped[str]   = mapped_column(String(100))
    tear:           Mapped[str]   = mapped_column(String(100))
    date_start:     Mapped[str]   = mapped_column(Date)
    date_end:       Mapped[str]   = mapped_column(Date)
    efficiency:     Mapped[float] = mapped_column(Float)
    weight_daily:   Mapped[float] = mapped_column(Float)
    days_for_done:  Mapped[float] = mapped_column(Float)
    type_register:  Mapped[str]   = mapped_column(String(100))

    def __repr__(self):
        return f"ProgramingReportModel(f{self.id=}, {self.name=})"