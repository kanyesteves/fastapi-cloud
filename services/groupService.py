from utils.libs import Libs
from sqlalchemy import select, delete
from utils.connDB import ConnectDB
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker
from entities.groupEntity import GroupEntity
from schemas.groupSchema import GroupSchema, GroupUpdate
from entities.groupHasUsersEntity import GroupHasUsersEntity
from entities.userEntity import UserEntity

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
                    "users": self.getUsersHasGroup(group.id),
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
            group_entity = GroupEntity(name=group.name, permissions=group.permissions)
            session.add(group_entity)
            session.commit()

            last_id = group_entity.id
            for user_id in group.users:
                group_has_user_entity = GroupHasUsersEntity(group_id=last_id, user_id=user_id)
                session.add(group_has_user_entity)
                session.commit()

        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def updateGroup(self, id, groupSchema: GroupUpdate):
        try:
            self.updateUsersHasGroup(id, groupSchema.users)
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

# ----------------- Métodos de relacionamento

    def deleteRelationWithUsers(self, group_id):
        try:
            delete_query = delete(GroupHasUsersEntity).where(
                GroupHasUsersEntity.group_id == group_id
            )
            session.execute(delete_query)

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def updateUsersHasGroup(self, group_id, users_id):
        try:
            select_query = select(GroupHasUsersEntity).filter_by(group_id=group_id)
            group_has_users = session.execute(select_query).fetchall()
            group_has_users = [ group_has_user[0] for group_has_user in group_has_users ]

            existing_user_ids = { relation.user_id for relation in group_has_users }
            new_user_ids = set(users_id)

            users_to_remove = existing_user_ids - new_user_ids
            users_to_add = new_user_ids - existing_user_ids

            if users_to_remove:
                delete_query = delete(GroupHasUsersEntity).where(
                    GroupHasUsersEntity.group_id == group_id,
                    GroupHasUsersEntity.user_id.in_(users_to_remove)
                )
                session.execute(delete_query)

            for user_id in users_to_add:
                new_relation = GroupHasUsersEntity(group_id=group_id, user_id=user_id)
                session.add(new_relation)

            session.commit()
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()


    def getUsersHasGroup(self, group_id):
        try:
            select_query = (
                select(UserEntity)
                .join(GroupHasUsersEntity, UserEntity.id == GroupHasUsersEntity.user_id)
                .filter(GroupHasUsersEntity.group_id == group_id)
            )
            users = session.execute(select_query).fetchall()
            users = [user[0] for user in users]
            users = [
                {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "office": user.office,
                }
                for user in users
            ]
            return users
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()

    def getGroupHasUser(self, user_id):
        try:
            select_query = (
                select(GroupEntity)
                .join(GroupHasUsersEntity, GroupEntity.id == GroupHasUsersEntity.group_id)
                .filter(GroupHasUsersEntity.user_id == user_id)
            )
            group = session.execute(select_query).fetchall()
            return group[0][0]
        except SQLAlchemyError as er:
            session.rollback()
            print(f"ERRO: {er}")
        finally:
            session.close()