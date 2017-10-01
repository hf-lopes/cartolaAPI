import peewee as pw
from models.Players import Player
from models.Teams import Team




class PostGreConnector:

    def __init__(self):
        self.db = pw.PostgresqlDatabase('henriquelopes.db')

    def CreateTable(self):
        self.db.create_tables([Player, Team])