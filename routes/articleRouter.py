from schemas.articleSchema import ArticleSchema, ArticlePublic, ArticleUpdate
from services.articleService import ArticleService
from services.authService import AuthService
from fastapi import APIRouter, File, UploadFile, Depends
from fastapi.responses import JSONResponse
from http import HTTPStatus


service = ArticleService()
auth_service = AuthService()
router = APIRouter(
    prefix='/articles', 
    tags=['Articles Endpoints'],
    dependencies=[Depends(auth_service.get_current_user)]
)
    
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

@router.post('/upload')
async def upload_file(file: UploadFile = File(...)):
    file_location = f'./uploads/{file.filename}'
    with open(file_location, 'wb') as buffer:
        buffer.write(await file.read())
    return JSONResponse({"info": f"{file_location}"})

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