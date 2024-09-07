from sqlalchemy import String, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class GroupBase(DeclarativeBase):
    pass

class GroupEntity(GroupBase):
    __tablename__ = 'groups'

    id:             Mapped[int]  = mapped_column(primary_key=True, autoincrement=True)
    name:           Mapped[str]  = mapped_column(String(50))
    permissions:    Mapped[str]  = mapped_column(JSON)

    def __repr__(self):
        return f"GroupModel(f{self.id=}, {self.name=})"