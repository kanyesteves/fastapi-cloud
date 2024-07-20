import pandas as pd
from sqlalchemy import select
from sqlalchemy.orm import Session
from utils.connDB import ConnectDB
from utils.libs import Libs
from schemas.userSchema import UserPublic, UserSchema
from entities.userEntity import UserEntity

conn = ConnectDB()

class UserService:
    def __init__(self):
        self.lib = Libs()

    def getAllUsers(self):
        with Session(bind=conn.engine) as session:
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
        
    def getUserById(self, id):
        with Session(bind=conn.engine) as session:
            select_query = select(UserEntity).filter_by(id=id)
            user = session.execute(select_query).fetchall()
            return user[0][0]

    def createUser(self, user: UserSchema):
        with Session(bind=conn.engine) as session:
            user_entity = UserEntity(name=user.name, password=user.passwd, office=user.office, email=user.email)
            session.add(user_entity)
            session.commit()

    def updateUser(self, id, userSchema: UserSchema):
        with Session(bind=conn.engine) as session:
            userEntity = UserEntity(name=user.name, password=user.passwd, office=user.office, email=user.email)
            select_query = select(userEntity).filter_by(id=id)
            users = session.execute(select_query).fetchall()
            for user in users:
                for key, value in userSchema.items():
                    setattr(user[0], key, value)

            session.commit()

    def deleteUser(self, id):
        with Session(bind=conn.engine) as session:
            select_query = select(UserEntity).filter_by(id=id)
            users = session.execute(select_query).fetchall()
            for user in users:
                session.delete(user[0])

            session.commit()