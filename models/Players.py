from playhouse import postgres_ext as pg_ext
from models.BaseModel import BaseModel
from models.Teams import Team
from models.Positions import Position


class Player(BaseModel):

    ID = pg_ext.IntegerField(unique=True, primary_key=True)
    Name = pg_ext.TextField()
    TeamID = pg_ext.ForeignKeyField(Team)
    PosID = pg_ext.ForeignKeyField(Position)
    Year = pg_ext.IntegerField()


