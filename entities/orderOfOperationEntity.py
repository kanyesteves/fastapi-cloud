from sqlalchemy import String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from schemas.customerSchema import CustomerSchema


class OrderOfOperationBase(DeclarativeBase):
    pass

class OrderOfOperationrEntity(OrderOfOperationBase):
    __tablename__ = 'order_of_operation'

    id:                Mapped[int]            = mapped_column(primary_key=True, autoincrement=True)
    code:              Mapped[str]            = mapped_column(String(50))
    weight_per_piece:  Mapped[float]          = mapped_column(Float(50))
    customer_id:       Mapped[CustomerSchema] = mapped_column(CustomerSchema)


    def __repr__(self):
        return f"OrderOfOperationModel(f{self.id=}, {self.name=})"