import peewee as pw
from Teams import Team
from Positions import Position


class Player(pw.Model):

    ID = pw.IntegerField(unique=True, primary_key=True)
    Name = pw.TextField()
    TeamID = pw.ForeignKeyField(Team)
    PosID = pw.ForeignKeyField(Position)

