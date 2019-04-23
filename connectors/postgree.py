from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
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
from multiprocessing import Queue


class PostGreConnector:

    def __init__(self):
        self.engine = create_engine('postgresql://******:*****@pg-cartola.c3pssepl8cax.us-east-2.rds.amazonaws.com:5432/cartoladb', pool_size = 40)
        DBsession = sessionmaker()
        DBsession.bind = self.engine
        self.session = DBsession()
        self.q = Queue()

    def CreateAllTables(self):
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine

    def DropAll(self):
        Base.metadata.drop_all(self.engine)

    def InsertList(self, data):
        time.sleep(2)
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
            t = threading.Thread(name='t' + str(i),
                                 target=self.InsertListManual)
            t.start()
            print('Thread %s Running' % t.name)
        for d in data:
            self.q.put(d)
        t.join()

    def InsertListManual(self):
        time.sleep(2)
        while not self.q.empty():
            element = self.q.get()
            self.InsertElement(element)

    def QueryTeamAvgs(self, rodada, play, num_of_rounds, year):
        return self._get_db_session().query(func.avg(Scout.plays[play])\
                                            .label(play + '_last_' + str(num_of_rounds) + '_rounds'), Team.id)\
                                        .join(Team)\
                                        .filter(Scout.match_week < rodada,
                                                Scout.match_week >= rodada - num_of_rounds,
                                                Scout.year == year)\
                                        .group_by(Team.id).all()

    def QueryTeamGoals(self, rodada, num_of_rounds, year):
        return self._get_db_session().query(Team.id, func.avg(Match.home_score)
                                            .label('avg_home_score_last_' + str(num_of_rounds) + '_rounds'))\
            .join(Match, Match.home_team_id == Team.id)\
            .filter(Match.match_week < rodada,
                    Match.match_week >= rodada - num_of_rounds,
                    Match.year == year)

    def QueryTeamPlayer(self, q):
        return self._get_db_session().\
            query(q.c.Player_id, Team.id).\
            join(Team, Team.id == q.c.team_id).\
            first().\
            subquery()

    def QueryPlayerScout(self, scout_id):
        return self._get_db_session().\
            query(Scout.id, Player.player_id, Player.year, Player.team_id).\
            join(Player).\
            filter(Scout.id == scout_id).\
            subquery()

    def QueryTeamScout(self, scout_id):
        q = self._get_db_session().query(Scout.id).join(Player).filter(Scout.id == scout_id,
                                                                    Scout.player_id == Player.player_id,
                                                                    Scout.year == Player.year)
    def QuerySql(self, object, query_str):
        return self._get_db_session().query(object).filter(query_str).all()

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

    def _get_db_session(self):
        DBsession = sessionmaker()
        DBsession.bind = self.engine
        return DBsession()

    # def InsertOrUpdate(self, object, element, compare_fn):
    #     try:
    #         DBsession = sessionmaker()
    #         DBsession.bind = self.engine
    #         session = DBsession()
    #         q = session.query(object).filter(compare_fn(object, element))
    #         session.merge(element)
    #         session.commit()
    #     except Exception as ex:
    #         session.rollback()
    #         print(ex)
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

