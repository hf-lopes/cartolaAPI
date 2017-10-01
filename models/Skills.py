import peewee as pw


class Skill(pw.Model):

    ID = pw.IntegerField(unique=True, primary_key=True)
    Name = pw.TextField()
    NickName = pw.CharField()
    Points = pw.DoubleField()

