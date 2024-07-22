from fastapi import FastAPI

def create_app():
    app = FastAPI()

    # Importar e incluir roteadores aqui
    from routes import userRouter, tearRouter, operatorRouter, customerRouter
    app.include_router(userRouter.router)
    app.include_router(tearRouter.router)
    app.include_router(operatorRouter.router)
    app.include_router(customerRouter.router)

    return app