from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from entities.orderOfOperationEntity import OrderOfOperationEntity
from entities.articleEntity import ArticleEntity

class OpHasArticleBase(DeclarativeBase):
    pass

class OpHasArticleEntity(OpHasArticleBase):
    __tablename__ = 'op_has_article'

    id:           Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    op_id:        Mapped[int] = mapped_column(Integer, ForeignKey(OrderOfOperationEntity.id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    article_id:   Mapped[int] = mapped_column(Integer, ForeignKey(ArticleEntity.id,          ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    def __repr__(self):
        return f"OpHasArticleModel(id={self.id}, op_id={self.op_id}, article_id={self.article_id})"