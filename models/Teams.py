from playhouse import postgres_ext as pg_ext
from connectors.postgree import PostGreConnector

class Team(pg_ext.Model):

    ID = pg_ext.IntegerField(unique=True, primary_key=True)
    Name = pg_ext.TextField()
    NickName = pg_ext.TextField()


