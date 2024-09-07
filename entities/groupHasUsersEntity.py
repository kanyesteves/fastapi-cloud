from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from entities.groupEntity import GroupEntity
from entities.userEntity import UserEntity

class GroupHasUsersBase(DeclarativeBase):
    pass

class GroupHasUsersEntity(GroupHasUsersBase):
    __tablename__ = 'groups_has_users'

    id:       Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    group_id: Mapped[int] = mapped_column(Integer, ForeignKey(GroupEntity.id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    user_id:  Mapped[int] = mapped_column(Integer, ForeignKey(UserEntity.id,  ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    def __repr__(self):
        return f"GroupHasUsersModel(id={self.id}, group_id={self.group_id}, user_id={self.user_id})"
