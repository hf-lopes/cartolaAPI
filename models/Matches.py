from playhouse import postgres_ext as pg_ext
from models.BaseModel import BaseModel
from models.Teams import Team


class Match(BaseModel):

    ID = pg_ext.IntegerField(unique=True, primary_key=True)
    MatchWeek = pg_ext.SmallIntegerField()
    HomeTeamID = pg_ext.ForeignKeyField(Team, related_name="home_team")
    VisitingTeamID = pg_ext.ForeignKeyField(Team, related_name="away_team")
    HomeScore = pg_ext.IntegerField()
    VisitingScore = pg_ext.IntegerField()
    Result = pg_ext.CharField()
    Year = pg_ext.IntegerField()


