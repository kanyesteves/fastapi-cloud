from sqlalchemy import String, Float, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class InputOutputOfWiresBase(DeclarativeBase):
    pass

class InputOutputOfWiresEntity(InputOutputOfWiresBase):
    __tablename__ = 'input_output_of_wires'

    id:             Mapped[int]   = mapped_column(primary_key=True, autoincrement=True)
    name:           Mapped[str]   = mapped_column(String(50))
    weight:         Mapped[float] = mapped_column(Float)
    type_register:  Mapped[str]   = mapped_column(String(50))
    fiscal_note:    Mapped[str]   = mapped_column(String(50))
    date_open:      Mapped[str]   = mapped_column(Date)

    def __repr__(self):
        return f"InputOutputOfWiresModel(f{self.id=}, {self.name=})"