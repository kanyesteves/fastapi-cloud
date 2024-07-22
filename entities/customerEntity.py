from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class CustomerBase(DeclarativeBase):
    pass

class CustomerEntity(CustomerBase):
    __tablename__ = 'customers'

    id:             Mapped[int]  = mapped_column(primary_key=True, autoincrement=True)
    name:           Mapped[str]  = mapped_column(String(50))
    article:        Mapped[str]  = mapped_column(String(50))

    def __repr__(self):
        return f"CustomerModel(f{self.id=}, {self.name=})"