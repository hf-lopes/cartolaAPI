import peewee as pw
from Players import Player
from Teams import Team
from Matches import Match
from Skills import Skill


class Play(pw.Model):

    ID = pw.IntegerField(unique=True, primary_key=True)
    MatchID = pw.ForeignKeyField(Match)
    TeamID = pw.ForeignKeyField(Team)
    PlayerID = pw.ForeignKeyField(Player)
    Period = pw.CharField()
    Moment = pw.DoubleField()
    PlayType = pw.ForeignKeyField(Skill)

