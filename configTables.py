from utils.connDB import ConnectDB
from entities.userEntity import UserEntity

connect = ConnectDB()
user_base = UserEntity()

# Criando tabelas do banco de dados
user_base.metadata.create_all(bind=connect.engine)