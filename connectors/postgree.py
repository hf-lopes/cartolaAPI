from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.BaseModel import Base
from models.Players import Player
from models.Positions import Position
from models.Matches import Match
from models.Skills import Skill
from models.Teams import Team
from models.Scouts import Scout
from psycopg2 import IntegrityError
from constants import pg_user, pg_pswd, pg_url, pg_db, pg_port, NUM_PARALLEL_CONNECTIONS
import threading
import math
import time
import pandas
import psycopg2


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

    def QueryScout(self, scout_id):
        scout = self.session.query(Scout).filter(Scout.id == scout_id).one()
        return scout



class PostGreConnectorSQL():

    def __init__(self):
        start_connect = time.time()
        try:
            self.con = psycopg2.connect("dbname=" + pg_db +
                                        " user=" + pg_user +
                                        " host=" + pg_url +
                                        " port=" + pg_port +
                                        " password=" + pg_pswd)
            self.cursor = self.con.cursor()
            print("Connected %s", time.time() - start_connect)

        except psycopg2.ProgrammingError:
            print("Query malformed")
            raise Exception

        except psycopg2.DatabaseError as ex:
            print("DatabaseError: %s", ex)
            raise Exception

        except Exception as ex:
            print("Internal Error: %s", ex)
            raise Exception

    def execute_query(self, query):

        start_fetch = time.time()

        # print("[INPUT] %s" % query)

        try:
            df = pandas.read_sql_query(query, self.con)
            print("[OUTPUT] Number of rows: %s Number of columns: %s Time: %s" %
                             (df.shape[0], df.shape[1], "{0:.2}s".format(time.time() - start_fetch)))
            return df
        except psycopg2.ProgrammingError:
            print("Query malformed")

        except psycopg2.DatabaseError as ex:
            print("DatabaseError: %s", ex)

        except Exception as ex:
            print("Internal Error: %s", ex)

