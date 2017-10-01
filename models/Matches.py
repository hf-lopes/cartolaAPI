from playhouse import postgres_ext as pg_ext
from connectors.postgree import PostGreConnector
from Teams import Team


class Match(pg_ext.Model):

    ID = pg_ext.IntegerField(unique=True, primary_key=True)
    Rodada = pg_ext.SmallIntegerField()
    HomeTeamID = pg_ext.ForeignKeyField(Team)
    VisitingTeamID = pg_ext.ForeignKeyField(Team)
    HomeScore = pg_ext.IntegerField()
    VisitingScore = pg_ext.IntegerField()
    Result = pg_ext.CharField()


