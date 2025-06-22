from sqlalchemy import String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class ArticleBase(DeclarativeBase):
    pass

class ArticleEntity(ArticleBase):
    __tablename__ = 'articles'

    id:             Mapped[int]   = mapped_column(primary_key=True, autoincrement=True)
    name:           Mapped[str]   = mapped_column(String(50))
    price:          Mapped[float] = mapped_column(Float)
    description:    Mapped[str]   = mapped_column(String(500))

    def __repr__(self):
        return f"ArticleModel(f{self.id=}, {self.name=})"