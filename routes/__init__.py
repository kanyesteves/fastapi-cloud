from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_app():
    app = FastAPI()
    origins = '*'
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    # Importar e incluir roteadores aqui
    from routes import userRouter, tearRouter, operatorRouter, customerRouter, orderOfOperationRouter, wireRouter
    app.include_router(userRouter.router)
    app.include_router(tearRouter.router)
    app.include_router(operatorRouter.router)
    app.include_router(customerRouter.router)
    app.include_router(orderOfOperationRouter.router)
    app.include_router(wireRouter.router)

    return app