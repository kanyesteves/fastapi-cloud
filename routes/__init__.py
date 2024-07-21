from fastapi import FastAPI

def create_app():
    app = FastAPI()

    # Importar e incluir roteadores aqui
    from routes import userRouter, tearRouter
    app.include_router(userRouter.router)
    app.include_router(tearRouter.router)

    return app