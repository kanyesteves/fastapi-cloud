from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from entities.tearEntity import TearEntity
from entities.programingEntity import ProgramingEntity

class ProgramingHasTearBase(DeclarativeBase):
    pass

class ProgramingHasTearEntity(ProgramingHasTearBase):
    __tablename__ = 'programing_has_tear'

    id:            Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    programing_id: Mapped[int] = mapped_column(Integer, ForeignKey(ProgramingEntity.id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    tear_id:       Mapped[int] = mapped_column(Integer, ForeignKey(TearEntity.id,       ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    def __repr__(self):
        return f"ProgramingHasTearModel(id={self.id}, programing_id={self.programing_id}, tear_id={self.tear_id})"
