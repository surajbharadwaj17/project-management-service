from classy_fastapi import Routable, post, get, delete, put
from app.connectors.database.dao.base import BaseDAO
from app.connectors.database.dao.project import ProjectDAO, Project as PN
from app import schema
import typing


class ProjectRoutes(Routable):
    def __init__(self, base_dao:BaseDAO) -> None:
        #super().__init__()
        self.base_dao: ProjectDAO = typing.cast(ProjectDAO, base_dao)
        Routable.__init__(self)

    @post("", response_model=schema.ProjectResponse)
    async def register_project(self, project: schema.ProjectRegister):
        project.status = "created"
        return self.base_dao.create_project(PN(**project.dict()))