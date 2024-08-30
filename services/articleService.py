from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from utils.connDB import ConnectDB
from utils.libs import Libs
from schemas.articleSchema import ArticleSchema, ArticleUpdate
from entities.articleEntity import ArticleEntity

conn = ConnectDB()
Session = sessionmaker(bind=conn.engine)
session = Session()

class ArticleService:
    def __init__(self):
        self.lib = Libs()

    def getAllArticles(self):
        try:
            select_query = select(ArticleEntity)
            all_articles = session.execute(select_query).fetchall()
            all_articles = [article[0] for article in all_articles]
            all_articles = [
                {
                    "id": article.id,
                    "name": article.name,
                    "description": article.description
                }
                for article in all_articles
            ]
            return all_articles
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()
        
    def getArticleById(self, id):
        try:
            select_query = select(ArticleEntity).filter_by(id=id)
            article = session.execute(select_query).fetchall()
            return article[0][0]
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def createArticle(self, article: ArticleSchema):
        try:
            article_entity = ArticleEntity(name=article.name, description=article.description)
            session.add(article_entity)
            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def updateArticle(self, id, articleSchema: ArticleUpdate):
        try:
            select_query = select(ArticleEntity).filter_by(id=id)
            articles = session.execute(select_query).fetchall()
            for article in articles:
                for key, value in articleSchema.dict(exclude_unset=True).items():
                    setattr(article[0], key, value)

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def deleteArticle(self, id):
        try:
            select_query = select(ArticleEntity).filter_by(id=id)
            articles = session.execute(select_query).fetchall()
            for article in articles:
                session.delete(article[0])

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()