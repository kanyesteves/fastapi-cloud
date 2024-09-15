from sqlalchemy import String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class ProgramingBase(DeclarativeBase):
    pass

class ProgramingEntity(ProgramingBase):
    __tablename__ = 'programing'

    id:             Mapped[int]  = mapped_column(primary_key=True, autoincrement=True)
    name:           Mapped[str]  = mapped_column(String(50))

    def __repr__(self):
        return f"ProgramingModel(f{self.id=}, {self.name=})"