from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_app():
    app = FastAPI()
    origins = ['*']
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    # Importar e incluir roteadores aqui
    from routes import userRouter
    from routes import tearRouter
    from routes import operatorRouter
    from routes import customerRouter
    from routes import orderOfOperationRouter
    from routes import wireRouter
    from routes import articleRouter
    from routes import productionRouter
    from routes import groupRouter
    from routes import programingRouter
    from routes import invoicingRouter
    from routes import configurationRouter
    from routes import authRouter
    from routes import inputOutputOfWiresRouter
    from routes import programingReportRouter

    app.include_router(userRouter.router)
    app.include_router(tearRouter.router)
    app.include_router(operatorRouter.router)
    app.include_router(customerRouter.router)
    app.include_router(orderOfOperationRouter.router)
    app.include_router(wireRouter.router)
    app.include_router(productionRouter.router)
    app.include_router(articleRouter.router)
    app.include_router(groupRouter.router)
    app.include_router(programingRouter.router)
    app.include_router(invoicingRouter.router)
    app.include_router(configurationRouter.router)
    app.include_router(authRouter.router)
    app.include_router(inputOutputOfWiresRouter.router)
    app.include_router(programingReportRouter.router)

    return app