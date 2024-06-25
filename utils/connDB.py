from sqlalchemy import create_engine

PATH_TO_DB = '/Users/kanydianesteves/projetos/fastapi-cloud/db/db_users.sqlite'

class ConnectDB():
    def __init__(self):
        self.engine = create_engine(f'sqlite:///{PATH_TO_DB}')