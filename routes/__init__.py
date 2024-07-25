from fastapi import FastAPI

def create_app():
    app = FastAPI()

    # Importar e incluir roteadores aqui
    from routes import userRouter, tearRouter, operatorRouter, customerRouter, orderOfOperationRouter
    app.include_router(userRouter.router)
    app.include_router(tearRouter.router)
    app.include_router(operatorRouter.router)
    app.include_router(customerRouter.router)
    app.include_router(orderOfOperationRouter.router)

    return app