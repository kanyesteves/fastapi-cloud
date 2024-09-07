from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class UserBase(DeclarativeBase):
    pass

class UserEntity(UserBase):
    __tablename__ = 'users'

    id:             Mapped[int]  = mapped_column(primary_key=True, autoincrement=True)
    name:           Mapped[str]  = mapped_column(String(50))
    password:       Mapped[str]  = mapped_column(String(128))
    office:         Mapped[str]  = mapped_column(String(50))
    email:          Mapped[str]  = mapped_column(String(50))


    def __repr__(self):
        return f"UserModel({self.id=}, {self.name=})"