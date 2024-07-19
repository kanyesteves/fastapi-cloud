from sqlalchemy import create_engine


PATH_TO_DB = 'mysql+pymysql://root:#GIK64LK:;)IP//"@34.134.251.247/volatex'


class ConnectDB():
    def __init__(self):
        self.engine = create_engine(PATH_TO_DB)