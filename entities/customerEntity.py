from sqlalchemy import String, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class CustomerBase(DeclarativeBase):
    pass

class CustomerEntity(CustomerBase):
    __tablename__ = 'customers'

    id:             Mapped[int]  = mapped_column(primary_key=True, autoincrement=True)
    name:           Mapped[str]  = mapped_column(String(50))
    article:        Mapped[dict]  = mapped_column(JSON)

    def __repr__(self):
        return f"CustomerModel(f{self.id=}, {self.name=})"