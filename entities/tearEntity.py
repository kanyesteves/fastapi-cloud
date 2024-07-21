from sqlalchemy import String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class TearBase(DeclarativeBase):
    pass

class TearEntity(TearBase):
    __tablename__ = 'teares'

    id:             Mapped[int]  = mapped_column(primary_key=True, autoincrement=True)
    name:           Mapped[str]  = mapped_column(String(50))
    model:          Mapped[str]  = mapped_column(String(50))

    def __repr__(self):
        return f"TearModel(f{self.id=}, {self.name=})"