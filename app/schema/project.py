from pydantic import BaseModel, UUID4, Field
from typing import Literal, Union, List

class Project(BaseModel):
    id : UUID4
    name : str
    status : Literal["in progress","created","completed","cancelled","paused"]
    owner_id : UUID4
    created_utc : str
    updated_utc : str

class ProjectRegister(BaseModel):
    name: str
    status: str = Field("created", const=True)
    owner_id : UUID4

class ProjectResponse(BaseModel):
    data : Union[Project, List[Project]]
