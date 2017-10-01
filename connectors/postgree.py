from playhouse import postgres_ext as pg_ext


class PostGreConnector:

    def __init__(self):
        self.db = pg_ext.PostgresqlExtDatabase('henriquelopes.db')

    def CreateTable(self, Model):
        self.db.create_table(Model)

    def CreateMultipleTables(self, Models):
        self.db.create_tables(Models)
