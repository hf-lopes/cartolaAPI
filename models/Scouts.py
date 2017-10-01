import peewee as pw
from Players import Player
from Teams import Team
from Matches import Match
from Skills import Skill


class Scout(pw.Model):

    ID = pw.IntegerField(unique=True, primary_key=True)
    PlayerID = pw.ForeignKeyField(Player)
    Rodada = pw.IntegerField()
    TeamID = pw.ForeignKeyField(Team)
    HasPlayed = pw.BooleanField()
    GamesPlayed = pw.IntegerField()
    Points = pw.DoubleField()
    AveragePoints = pw.DoubleField()
    Price = pw.DoubleField()
    DeltaPrice = pw.DoubleField()
    MatchID = pw.ForeignKeyField(Match)
    HomeGame = pw.BooleanField()
    Starter = pw.BooleanField()
    Substituted = pw.BooleanField()
    TimePlayed = pw.DoubleField()
    Score = pw.DoubleField()
    PlayType = pw.ForeignKeyField(Skill)

