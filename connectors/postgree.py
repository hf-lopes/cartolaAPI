from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import expression
from sqlalchemy.orm import sessionmaker
>>>>>>> be3b189b311b09069cd2afc2ec4bc9ffe89d8c3f


class PostGreConnector:

    def __init__(self):
        engine = create_engine('postgresql://' + pg_user + ':' + pg_pswd + ' @' + pg_url + '/' + pg_db)
        self.Base = declarative_base()
        self.Base.metadata.bind = engine
        DBsession = sessionmaker()
        DBsession.bind = engine
        self.session = DBsession()

    def CreateTable(self, Model, check_exists=True):
        self.db.create_table(Model, check_exists)

    def CreateMultipleTables(self, Models, check_exists=True):
        self.db.create_tables(Models, check_exists)

    def InsertElement(self, Data):
        Data.save()