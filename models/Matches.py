import peewee as pw
from Teams import Team


class Match(pw.Model):

    ID = pw.IntegerField(unique=True, primary_key=True)
    Rodada = pw.SmallIntegerField()
    HomeTeamID = pw.ForeignKeyField(Team)
    VisitingTeamID = pw.ForeignKeyField(Team)
    HomeScore = pw.IntegerField()
    VisitingScore = pw.IntegerField()
    Result = pw.CharField()

