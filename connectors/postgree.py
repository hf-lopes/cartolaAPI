from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.BaseModel import Base
from psycopg2 import IntegrityError
from constants import pg_user, pg_pswd, pg_url, pg_db
import threading
import math


class PostGreConnector:

    def __init__(self):
        self.engine = create_engine('postgresql://hlopes:lopes_146@pg-cartola.c3pssepl8cax.us-east-2.rds.amazonaws.com:5432/cartoladb', pool_size = 40)
        DBsession = sessionmaker()
        DBsession.bind = self.engine
        self.session = DBsession()

    def CreateAllTables(self):
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine

    def DropAll(self):
        Base.metadata.drop_all(self.engine)

    def InsertList(self, data):
        print('Starting thread %s ' % threading.current_thread().name)
        try:
            DBsession = sessionmaker()
            DBsession.bind = self.engine
            session = DBsession()
            session.add_all(data)
            session.commit()
            session.close()
        except Exception as ex:
            session.rollback()
            session.close()
            print('Erro desconhecido', ex)


    def InsertListParallel(self, data, no_threads):
        l = len(data)
        print('Initializing Threads')
        for i in range(no_threads):
            print(0+i* math.floor(l/no_threads), min(l + 1, int((i + 1) * math.floor(l / no_threads))))
            t = threading.Thread(name='t' + str(i),
                                 target=self.InsertList, args=(data[0+i* math.floor(l/no_threads):
                                 min(l + 1, int((i + 1) * math.floor(l / no_threads)))],)
                                 )
            t.start()
            print('Thread %s Running' % t.name)
        t.join()

    def InsertListManual(self,data):
        for index, d in enumerate(data):
            print('%s : ' % threading.current_thread().name, index * 100 / len(data))
            self.InsertElement(d)


    def InsertElement(self, element):
        try:
            DBsession = sessionmaker()
            DBsession.bind = self.engine
            session = DBsession()
            session.merge(element)
            session.commit()
        except Exception as ex:
            session.rollback()
            print(ex)
