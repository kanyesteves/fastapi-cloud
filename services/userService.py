from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from utils.connDB import ConnectDB
from utils.libs import Libs
from schemas.userSchema import UserSchema, UserUpdate
from entities.userEntity import UserEntity

conn = ConnectDB()
Session = sessionmaker(bind=conn.engine)
session = Session()

libs = Libs()

class UserService:
    def __init__(self):
        self.lib = Libs()

    def getAllUsers(self):
        try:
            select_query = select(UserEntity)
            all_users = session.execute(select_query).fetchall()
            all_users = [user[0] for user in all_users]
            all_users = [
                {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "office": user.office,
                }
                for user in all_users
            ]
            return all_users
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()
        
    def getUserById(self, id):
        try:
            select_query = select(UserEntity).filter_by(id=id)
            user = session.execute(select_query).fetchall()
            return user[0][0]
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()
    

    def createUser(self, user: UserSchema):
        try:
            user_entity = UserEntity(name=user.name, password=user.password, office=user.office, email=user.email)
            session.add(user_entity)
            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()
        

    def updateUser(self, id, userSchema: UserUpdate):
        try:
            select_query = select(UserEntity).filter_by(id=id)
            users = session.execute(select_query).fetchall()
            for user in users:
                for key, value in userSchema.dict(exclude_unset=True).items():
                    setattr(user[0], key, value)

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def deleteUser(self, id):
        try:
            select_query = select(UserEntity).filter_by(id=id)
            users = session.execute(select_query).fetchall()
            for user in users:
                session.delete(user[0])

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()