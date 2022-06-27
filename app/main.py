# Initialize FastAPI server and define routes

from fastapi import FastAPI
from starlette.status import *
from app import routers
from app.connectors.database.dao.base import BaseDAO
from app.connectors.database.dao.project import ProjectDAO
from app.connectors.database.dao.user import UserDAO
from app.connectors.database.database import DBConnector, DBConfig


db_handle = DBConnector(config=DBConfig(
    db="project_management_service",
    host="localhost",
    port="5432",
    user="jbharaso",
    pwd="123"
))


app = FastAPI(
    title="Project Management Service",
    version="0.0.1"
)

db_handle = DBConnector(config=DBConfig(
    db="project_management_service",
    host="localhost",
    port="5432",
    user="jbharaso",
    pwd="123")).connect()

app.include_router(routers.ProjectRoutes(base_dao=ProjectDAO(db=db_handle)).router, prefix="/projects",
                    tags=["Projects API"],
                    responses={HTTP_404_NOT_FOUND : {"description": "Not Found"}},
                    dependencies=[])

app.include_router(routers.UserRoutes(base_dao=UserDAO(db=db_handle)).router, prefix="/users",
                    tags=["Users API"],
                    responses={HTTP_404_NOT_FOUND : {"description": "Not Found"}},
                    dependencies=[])
