from playhouse import postgres_ext as pg_ext
from models.BaseModel import BaseModel


class Skill(BaseModel):

    ID = pg_ext.IntegerField(unique=True, primary_key=True)
    Name = pg_ext.TextField()
    NickName = pg_ext.CharField()
    Points = pg_ext.DoubleField()


