from lib2to3.pytree import Base
from sqlalchemy import Column, ForeignKey, Integer, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Users table
class TableUsers(Base):
    __tablename__ = "t_users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"), nullable=False)
    name = Column(String)
    email_id = Column(String)

# Projects table
class TableProjects(Base):
    __tablename__ = "t_projects"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"), nullable=False)
    name = Column(String, nullable=False)
    status = Column(String)
    owner_id = Column(UUID(as_uuid=True), ForeignKey(TableUsers.id), nullable=False)


    