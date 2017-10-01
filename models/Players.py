from playhouse import postgres_ext as pg_ext
from Teams import Team
from Positions import Position
from connectors.postgree import PostGreConnector


class Player(pg_ext.Model):

    ID = pg_ext.IntegerField(unique=True, primary_key=True)
    Name = pg_ext.TextField()
    TeamID = pg_ext.ForeignKeyField(Team)
    PosID = pg_ext.ForeignKeyField(Position)


