
from requests import delete
from sqlalchemy import MetaData

from sqlalchemy import MetaData
from sqlalchemy.sql.expression import insert, select, delete, update
from sqlalchemy.sql.functions import func


class QueryBuilder():
    def __init__(self, metadata : MetaData, schema: str) -> None:
        self.metadata = metadata
        self.schema = schema

    def _table(self, table_name):
        return self.metadata.tables[f"{self.schema}.{table_name}"]

    def _filter(self, table, sql, filters):
        for col,val in filters.items():
            if val is not None:
                sql = sql.where(table.columns[col] == val)
        return sql

    def _insert(self, table_name, data):
        sql = self._table(table_name).insert().values(data).returning(self._table(table_name))
        return sql

    def _select(self, table_name, cols=None, filters=None):
        if cols is None:
            sql = select(self._table(table_name).columns)
        else:
            sql = select(self._table(table_name).columns[col] for col in cols)
        if filters is not None:
            sql = self._filter(self._table(table_name), sql, filters)
        return sql

    def _update(self, table_name, data, filters=None):
        data["updated_utc"] = func.now()
        sql = update(self._table(table_name)).values(data).returning(self._table(table_name))
        if filters is not None:
            sql = self._filter(self._table(table_name), sql, filters)
        return sql

    def _delete(self, table_name, filters=None):
        sql = delete(self._table(table_name)).returning(self._table(table_name))
        if filters is not None:
            sql = self._filter(self._table(table_name), sql, filters)
        return sql
    
