from playhouse import postgres_ext as pg_ext
from models.BaseModel import BaseModel
from models.Players import Player
from models.Teams import Team
from models.Matches import Match
from models.Skills import Skill


class Play(BaseModel):

    ID = pg_ext.IntegerField(unique=True, primary_key=True)
    MatchID = pg_ext.ForeignKeyField(Match)
    TeamID = pg_ext.ForeignKeyField(Team)
    PlayerID = pg_ext.ForeignKeyField(Player)
    Period = pg_ext.CharField()
    Moment = pg_ext.DoubleField()
    PlayType = pg_ext.ForeignKeyField(Skill)
    Year = pg_ext.IntegerField()


