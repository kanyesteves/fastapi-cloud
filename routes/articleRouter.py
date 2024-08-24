from schemas.articleSchema import ArticleSchema, ArticlePublic, ArticleUpdate
from services.articleService import ArticleService
from fastapi import APIRouter
from http import HTTPStatus


router = APIRouter(prefix='/articles', tags=['Articles Endpoints'])
service = ArticleService()
    
@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllArticles():
    try: 
        articles = service.getAllArticles()
        return articles
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.get('/{article_id}', status_code=HTTPStatus.OK, response_model=ArticlePublic)
def getArticleById(article_id: int):
    try: 
        article = service.getArticleById(article_id)
        return article
    except:
        return HTTPStatus.NOT_FOUND
    
@router.post('/register', status_code=HTTPStatus.CREATED)
def createArticle(article: ArticleSchema):
    try: 
        service.createArticle(article)
        return "Artigo criado com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.put('/update/{article_id}', status_code=HTTPStatus.OK)
def updateArticle(article_id: int, article: ArticleUpdate):
    service.updateArticle(article_id, article)
    return "Artigo atualizado com sucesso !!"

@router.delete('/remove/{article_id}', status_code=HTTPStatus.OK)
def removeArticle(article_id: int):
    try: 
        service.deleteArticle(article_id)
        return "Artigo removido com sucesso !!"
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY