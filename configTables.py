from utils.connDB import ConnectDB
from entities.userEntity import UserEntity
from sqlalchemy.orm import sessionmaker

connect = ConnectDB()
user_base = UserEntity()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=connect.engine)



# Criando tabelas do banco de dados
user_base.metadata.create_all(bind=connect.engine)