from dataclasses import dataclass, asdict
from lib2to3.pytree import Base

from .base import BaseDAO
from app.connectors.database.database import DBConnector
from app.utils.db import QueryBuilder

@dataclass
class User:
    id : str = None
    name : str = None
    email_id : str = None
    role : str = None
    created_utc : str = None
    updated_utc : str = None

    def to_dict(self):
        return {key:val for key,val in asdict(self).items() if val}


class UserDAO(BaseDAO):
    table_name : str = "t_users"

    def __init__(self, db: DBConnector) -> None:
        super().__init__(db)
        self.queryUtil = QueryBuilder(metadata=self.db.metadata, schema=self.db.schema)

    def create_user(self, user: User):
        sql = self.queryUtil._insert(self.table_name, data=user.to_dict())

    def select_user(self, user_id):
        sql = self.queryUtil._select(self.table_name, filters={"id":user_id})

    def select_users(self):
        sql = self.queryUtil._select(self.table_name)

    def update_user(self, data, user_id):
        sql = self.queryUtil._update(self.table_name, data, filters={"id":user_id})

    def delete_user(self, user_id):
        sql = self.queryUtil._delete(self.table_name, filters={"id":user_id})

        


