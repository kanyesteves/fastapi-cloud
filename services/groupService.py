import json
from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from utils.connDB import ConnectDB
from utils.libs import Libs
from schemas.groupSchema import GroupSchema, GroupUpdate
from entities.groupEntity import GroupEntity
from schemas.userSchema import UserPublic

conn = ConnectDB()
Session = sessionmaker(bind=conn.engine)
session = Session()

class GroupService:
    def __init__(self):
        self.lib = Libs()

    def getAllGroups(self):
        try:
            select_query = select(GroupEntity)
            all_groups = session.execute(select_query).fetchall()
            all_groups = [group[0] for group in all_groups]
            all_groups = [
                {
                    "id": group.id,
                    "name": group.name,
                    "users": group.users,
                    "permissions": group.permissions,
                }
                for group in all_groups
            ]
            return all_groups
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()
        
    def getGroupById(self, id):
        try:
            select_query = select(GroupEntity).filter_by(id=id)
            group = session.execute(select_query).fetchall()
            return group[0][0]
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def createGroup(self, group: GroupSchema):
        try:
            group = self.schemaForDict(group)
            group_entity = GroupEntity(name=group.name, users=group.users, permissions=group.permissions)
            session.add(group_entity)
            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def updateGroup(self, id, groupSchema: GroupUpdate):
        try:
            select_query = select(GroupEntity).filter_by(id=id)
            groups = session.execute(select_query).fetchall()
            for group in groups:
                for key, value in groupSchema.dict(exclude_unset=True).items():
                    setattr(group[0], key, value)

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def deleteGroup(self, id):
        try:
            select_query = select(GroupEntity).filter_by(id=id)
            groups = session.execute(select_query).fetchall()
            for group in groups:
                session.delete(group[0])

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def schemaForDict(self, group: GroupSchema):
        if group.users and isinstance(group.users, list):
            group.users = [
                user.dict() if isinstance(user, UserPublic) else user
                for user in group.users
            ]

        return group