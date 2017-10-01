import peewee as pw


class Position(pw.Model):

    ID = pw.SmallIntegerField(unique=True, primary_key=True)
    Name = pw.TextField()
    NickName = pw.TextField()

