from playhouse import postgres_ext as pg_ext
from connectors.postgree import PostGreConnector
from Players import Player
from Teams import Team
from Matches import Match
from Skills import Skill


class Scout(pg_ext.Model):

    ID = pg_ext.IntegerField(unique=True, primary_key=True)
    PlayerID = pg_ext.ForeignKeyField(Player)
    Rodada = pg_ext.IntegerField()
    TeamID = pg_ext.ForeignKeyField(Team)
    HasPlayed = pg_ext.BooleanField()
    GamesPlayed = pg_ext.IntegerField()
    Points = pg_ext.DoubleField()
    AveragePoints = pg_ext.DoubleField()
    Price = pg_ext.DoubleField()
    DeltaPrice = pg_ext.DoubleField()
    MatchID = pg_ext.ForeignKeyField(Match)
    HomeGame = pg_ext.BooleanField()
    Starter = pg_ext.BooleanField()
    Substituted = pg_ext.BooleanField()
    TimePlayed = pg_ext.DoubleField()
    Score = pg_ext.DoubleField()
    Plays = pg_ext.ArrayField(Skill)


