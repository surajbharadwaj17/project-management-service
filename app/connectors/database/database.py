from dataclasses import dataclass
from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine import Engine
from app.connectors.database import tables

@dataclass
class DBConfig():
    db : str
    host : str
    port : str
    user : str
    pwd : str

    @property
    def db_string(self):
        db_string = f"postgresql://{self.user}:{self.pwd}@{self.host}:{self.port}/{self.db}"
        return db_string

class DBConnector():
    engine : Engine
    metadata : MetaData
    schema :str = "project_management_service"

    def __init__(self, config: DBConfig) -> None:
        self.config = config

    def get_engine(self, echo=False):
        return create_engine(self.config.db_string, echo=echo)

    def connect(self):
        self.engine = self.get_engine(echo=False)
        # Initialize tables
        self._init_tables(engine=self.engine)
        self.metadata.reflect(bind=self.engine, schema=self.schema)

    def _init_tables(self, engine):
        tables.Base.metadata.create_all(bind=engine)

    

