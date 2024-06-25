from sqlalchemy import String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class UserBase(DeclarativeBase):
    pass

class UserEntity(UserBase):
    __tablename__ = 'users'

    id:             Mapped[int]  = mapped_column(primary_key=True)
    name:           Mapped[str]  = mapped_column(String(50))
    senha:          Mapped[str]  = mapped_column(String(128))
    office:         Mapped[str]  = mapped_column(String(50))
    acess_gestor:   Mapped[bool] = mapped_column(Boolean, default=False)


    def __repr__(self):
        return f"UserModel(f{self.id=}, {self.name=})"