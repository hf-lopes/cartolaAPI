from playhouse.postgres_ext import PostgresqlExtDatabase


class PostGreConnector:

    def __init__(self):
        self.db = PostgresqlExtDatabase('henriquelopes', user='postgres')
        self.db.connect()

    def CreateTable(self, Model, check_exists=True):
        self.db.create_table(Model, check_exists)

    def CreateMultipleTables(self, Models, check_exists=True):
        self.db.create_tables(Models, check_exists)

    def InsertElement(self, Data):
        Data.save()