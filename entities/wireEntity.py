from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class WireBase(DeclarativeBase):
    pass

class WireEntity(WireBase):
    __tablename__ = 'wires'

    id:             Mapped[int]  = mapped_column(primary_key=True, autoincrement=True)
    name:           Mapped[str]  = mapped_column(String(50))
    description:    Mapped[str]  = mapped_column(String(500))

    def __repr__(self):
        return f"WireModel(f{self.id=}, {self.name=})"