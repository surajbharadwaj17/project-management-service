# Initialize FastAPI server and define routes

from fastapi import FastAPI
from app import routers


####################
#  DB Handle here
#####################

app = FastAPI(
    title="Project Management Service",
    version="0.0.1"
)


app.include_router(routers.ProjectRoutes(base_dao=ProjectDAO(db=db_handle)).router, prefix="/projects",
                    tags=["Projects API"],
                    responses={HTTP_404_NOT_FOUND : {"description": "Not Found"}},
                    dependencies=[])

                    
