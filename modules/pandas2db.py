import pandas as pd
import math
from models.Players import Player
from models.Matches import Match
from models.Plays import Play
from models.Positions import Position
from models.Scouts import Scout
from models.Skills import Skill
from models.Teams import Team

from connectors.postgree import PostGreConnector
from constants import abreviacao, pontuacao, descricao

class Pandas2DB():

    def __init__(self):
        self.db_con = PostGreConnector()

    def createtables(self):
        self.db_con.CreateMultipleTables([Player, Match, Position, Scout, Skill, Team], True)

    def InsertPlayer(self, df):
        DB_list = Pandas2DB.Df2Db_Player(df)
        for db in DB_list:
            q = Player.insert(db)
            q.execute()
            print('Player %s inserted' % q)

    def InsertMatch(self, df):
        DB_list = Pandas2DB.Df2Db_Match(df)
        for db in DB_list:
            q = Match.insert(db)
            q.execute()
            print('Match %s inserted' % q)

    def InsertPosition(self, df):
        DB_list = Pandas2DB.Df2Db_Position(df)
        for db in DB_list:
            q = Position.insert(db)
            q.execute()
            print('Position %s inserted' % q)

    def InsertScout(self, df):
        DB_list = Pandas2DB.Df2Db_Scout(df)
        for db in DB_list:
            q = Scout.insert(db)
            q.execute()
            print('Scout %s inserted' % q)

    def InsertSkill(self):
        DB_list = Pandas2DB.Df2Db_Skill()
        for db in DB_list:
            q = Skill.insert(db)
            q.execute()
            print('Skill %s inserted' % q)

    def InsertTeam(self, df):
        DB_list = Pandas2DB.Df2Db_Team(df)
        for db in DB_list:
            q = Team.insert(db)
            print('Team %s inserted' % q)
            q.execute()

    @staticmethod
    def Df2Db_Player(df):
        DB_list = []
        for index, row in df.iterrows():
            if not math.isnan(row['Clube']):
                jogador = ({'ID': row['ID'], 'Name': row['Apelido'], 'TeamID': int(row['Clube']), 'PosID': int(row['Posicao']),
                            'Year': row['Year']})
                DB_list.append(jogador)
        return DB_list

    @staticmethod
    def Df2Db_Match(df):
        DB_list = []
        for index, row in df.iterrows():
            partida = ({'ID' : row['ID'], 'HomeTeamID' : row['Casa'], 'VisitingTeamID' : row['Visitante'], 'Result' : row['Resultado'],
                       'HomeScore' : row['PlacarCasa'], 'VisitingScore' : row['PlacarVisitante'],
                        'MatchWeek' : row['Rodada'], 'Year' : row['Year']})
            DB_list.append(partida)
        return DB_list

    @staticmethod
    def Df2Db_Position(df):
        DB_list = []
        for index, row in df.iterrows():
            posicao = {'ID' : row['ID'], 'Name' : row['Nome'], 'NickName' : row['Abreviacao']}
            DB_list.append(posicao)
        return DB_list

    @staticmethod
    def Df2Db_Scout(df):
        DB_list = []
        for index, row in df.iterrows():
            Play_list = []
            for sigla in abreviacao:
                Play_list.append(row[sigla])
            status = True if row['Participou'] == 1 else False
            scouts = {'ID': index, 'PlayerID': row['Atleta'], 'MatchWeek': row['Rodada'],
                      'TeamID': row['Clube'], 'HasPlayed': status, 'Points': row['Pontos'],
                      'AveragePoints': row['PontosMedia'], 'Price': row['Preco'],
                      'DeltaPrice': row['PrecoVariacao'], 'MatchID': row['Partida'], 'HomeGame': row['Mando'],
                      'Score': row['Nota'], 'Plays': Play_list,
                      'Year': row['Year']}
            DB_list.append(scouts)
        return DB_list

    @staticmethod
    def Df2Db_Skill():
        DB_list = []
        for index in range(0, len(abreviacao)):
            scout = {'ID' : index, 'Name': descricao[index], 'NickName': abreviacao[index], 'Points': pontuacao[index]}
            DB_list.append(scout)
        return DB_list

    @staticmethod
    def Df2Db_Team(df):
        DB_list = []
        for index, row in df.iterrows():
            times = {'ID': row['ID'], 'Name': row['Slug'], 'NickName': row['Abreviacao'], 'Year': row['Year']}
            DB_list.append(times)
        return DB_list


