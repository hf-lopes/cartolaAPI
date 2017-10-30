from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.BaseModel import Base
from psycopg2 import IntegrityError
from constants import pg_user, pg_pswd, pg_url, pg_db


class PostGreConnector:

    def __init__(self):
        self.engine = create_engine('postgresql://hlopes:lopes_146@pg-cartola.c3pssepl8cax.us-east-2.rds.amazonaws.com:5432/cartoladb')
        DBsession = sessionmaker()
        DBsession.bind = self.engine
        self.session = DBsession()

    def CreateAllTables(self):
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine

    def DropAll(self):
        Base.metadata.drop_all(self.engine)

    def InsertList(self, data):
        try:
            self.session.add_all(data)
            self.session.commit()
        except IntegrityError as ex:
            print('ID já presente na tabela')
        except Exception as ex:
            print('Erro desconhecido', ex)

    def InsertListManual(self,data):
        for index, d in enumerate(data):
            try:
                print(index*100/len(data))
                self.session.merge(d)
                self.session.commit()
            except Exception as ex:
                self.session.rollback()
                print(ex)

    def InsertElement(self, element):
        self.session.merge(element)
        self.session.commit()