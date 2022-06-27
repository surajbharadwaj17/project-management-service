from abc import ABC
from app.connectors.database import DBConnector

class BaseDAO(ABC):

    def __init__(self, db: DBConnector) -> None:
        super().__init__()
        self.db = db
        self.schema = "project_management_service"


    def execute(self, sql):
        with self.db.engine.begin() as con:
            con.execute(sql)
            

