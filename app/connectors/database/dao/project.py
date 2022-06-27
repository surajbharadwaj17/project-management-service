from dataclasses import dataclass, asdict

from .base import BaseDAO
from app.connectors.database.database import DBConnector
from app.utils.db import QueryBuilder

@dataclass
class Project:
    id: str = None
    name: str = None
    email_id : str = None

    def to_dict(self):
        return {key:val for key,val in asdict(self).items() if val}


class ProjectDAO(BaseDAO):
    table_name : str = "t_projects"

    def __init__(self, db: DBConnector) -> None:
        super().__init__(db)
        self.queryUtil = QueryBuilder(metadata=self.db.metadata, schema=self.db.schema)
        
    def create_project(self, project: Project):
        sql = self.queryUtil._insert(self.table_name, data=project.to_dict())
        print(sql)

    def select_project(self, project_id):
        sql = self.queryUtil._select(self.table_name, filters={"id":project_id})
        print(sql)

    def select_projects(self):
        sql = self.queryUtil._select(self.table_name)
        print(sql)

    def update_project(self, data, project_id):
        sql = self.queryUtil._update(self.table_name, data, filters={"id":project_id})
        print(sql)

    def delete_project(self, project_id):
        sql = self.queryUtil._delete(self.table_name, filters={"id":project_id})
        print(sql)

        