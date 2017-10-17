from playhouse import postgres_ext as pg_ext
from connectors.postgree import PostGreConnector

class BaseModel(pg_ext.Model):
    class Meta:
        database = pg_ext.PostgresqlExtDatabase('henriquelopes', user='postgres')
        primary_key = pg_ext.CompositeKey('ID', 'Year')