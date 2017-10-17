from playhouse import postgres_ext as pg_ext
from models.BaseModel import BaseModel
from models.Players import Player
from models.Teams import Team
from models.Matches import Match


class Scout(BaseModel):

    ID = pg_ext.IntegerField(unique=True, primary_key=True)
    PlayerID = pg_ext.ForeignKeyField(Player)
    MatchWeek = pg_ext.IntegerField()
    TeamID = pg_ext.ForeignKeyField(Team)
    HasPlayed = pg_ext.BooleanField()
    Points = pg_ext.DoubleField()
    AveragePoints = pg_ext.DoubleField()
    Price = pg_ext.DoubleField()
    DeltaPrice = pg_ext.DoubleField()
    MatchID = pg_ext.ForeignKeyField(Match)
    HomeGame = pg_ext.BooleanField()
    Score = pg_ext.DoubleField()
    Plays = pg_ext.ArrayField(pg_ext.IntegerField)
    Year = pg_ext.IntegerField()


