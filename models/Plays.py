from playhouse import postgres_ext as pg_ext
from connectors.postgree import PostGreConnector
from Players import Player
from Teams import Team
from Matches import Match
from Skills import Skill


class Play(pg_ext.Model):

    ID = pg_ext.IntegerField(unique=True, primary_key=True)
    MatchID = pg_ext.ForeignKeyField(Match)
    TeamID = pg_ext.ForeignKeyField(Team)
    PlayerID = pg_ext.ForeignKeyField(Player)
    Period = pg_ext.CharField()
    Moment = pg_ext.DoubleField()
    PlayType = pg_ext.ForeignKeyField(Skill)


