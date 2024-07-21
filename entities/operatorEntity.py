from sqlalchemy import String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class OperatorBase(DeclarativeBase):
    pass

class OperatorEntity(OperatorBase):
    __tablename__ = 'operators'

    id:             Mapped[int]  = mapped_column(primary_key=True, autoincrement=True)
    name:           Mapped[str]  = mapped_column(String(50))
    office:         Mapped[str]  = mapped_column(String(50))

    def __repr__(self):
        return f"OperatorModel(f{self.id=}, {self.name=})"