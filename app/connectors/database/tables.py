from lib2to3.pytree import Base
from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, text
from sqlalchemy.dialects.postgresql import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.functions import func

meta = MetaData(schema="project_management_service")
Base = declarative_base(metadata=meta)

# Users table
class TableUsers(Base):
    __tablename__ = "t_users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"), nullable=False)
    name = Column(String)
    email_id = Column(String)
    role = Column(String)
    created_utc = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_utc = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

# Projects table
class TableProjects(Base):
    __tablename__ = "t_projects"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"), nullable=False)
    name = Column(String, nullable=False)
    status = Column(String)
    owner_id = Column(UUID(as_uuid=True), ForeignKey(TableUsers.id), nullable=False)
    created_utc = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_utc = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


    