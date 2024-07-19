from fastapi import FastAPI

def create_app():
    app = FastAPI()

    # Importar e incluir roteadores aqui
    from routes import userRouter
    app.include_router(userRouter.router)

    return app