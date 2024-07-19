import pandas as pd
from sqlalchemy import select
from sqlalchemy.orm import Session
from utils.connDB import ConnectDB
from utils.libs import Libs
from entities.userEntity import UserEntity

conn = ConnectDB()

class UserService:
    def __init__(self):
        self.lib = Libs()
        self.all_users = {}

    def getAllUsers(self):
        with Session(bind=conn.engine) as session:
            select_query = select(UserEntity)
            all_users = session.execute(select_query).fetchall()
            all_users = [user[0] for user in all_users]
            self.all_users = [
                {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "office": user.office,
                }
                for user in all_users
            ]
            df = pd.DataFrame(self.all_users)
            return df

    def createUser(self, name, password, email, office, **kwargs):
        with Session(bind=self.conn.engine) as session:
            user = UserEntity(name=name, password=self.lib.set_password(password), email=email, office=office, **kwargs)
            session.add(user)
            session.commit()