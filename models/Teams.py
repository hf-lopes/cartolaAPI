import peewee as pw


class Team(pw.Model):

    ID = pw.IntegerField(unique=True, primary_key=True)
    Name = pw.TextField()
    NickName = pw.TextField()

