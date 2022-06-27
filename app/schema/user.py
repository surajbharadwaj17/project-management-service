from uuid import UUID
from pydantic import BaseModel, UUID4, Field
from typing import Literal

class User(BaseModel):
    id : UUID4
    name : str
    email_id : str
    role : str
    created_utc : str
    updated_utc : str