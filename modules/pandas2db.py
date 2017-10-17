import pandas as pd
import math

from connectors.postgree import PostGreConnector
from constants import abreviacao, pontuacao, descricao

from models.Players import Player
from models.Matches import Match
from models.Plays import Play
from models.Positions import Position
from models.Scouts import Scout
from models.Skills import Skill
from models.Teams import Team


class Pandas2DB():

    def __init__(self):
        self.db_con = PostGreConnector()

    def createtables(self):
        self.db_con.CreateAllTables()


    def InsertPlayer(self, df):
        DB_list = Pandas2DB.Df2Db_Player(df)
        self.db_con.InsertList(DB_list)

    def InsertMatch(self, df):
        DB_list = Pandas2DB.Df2Db_Match(df)
        self.db_con.InsertList(DB_list)

    def InsertPosition(self, df):
        DB_list = Pandas2DB.Df2Db_Position(df)
        self.db_con.InsertList(DB_list)

    def InsertScout(self, df):
        DB_list = Pandas2DB.Df2Db_Scout(df)
        self.db_con.InsertList(DB_list)

    def InsertSkill(self):
        DB_list = Pandas2DB.Df2Db_Skill()
        self.db_con.InsertList(DB_list)

    def InsertTeam(self, df):
        DB_list = Pandas2DB.Df2Db_Team(df)
        self.db_con.InsertList(DB_list)

    @staticmethod
    def Df2Db_Player(df):
        DB_list = []
        for index, row in df.iterrows():
            if not math.isnan(row['Clube']):
                jogador = Player('id' = row['ID'], 'name' = row['Apelido'], 'team_id' = int(row['Clube']), 'pos_id' = int(row['Posicao']),
                            'year' = row['Year'])
                DB_list.append(jogador)
        return DB_list

    @staticmethod
    def Df2Db_Match(df):
        DB_list = []
        for index, row in df.iterrows():
            partida = Match('id' = row['ID'], 'home_team_id' = row['Casa'], 'VisitingTeamID' = row['Visitante'], 'Result' = row['Resultado'],
                       'HomeScore' = row['PlacarCasa'], 'VisitingScore'= row['PlacarVisitante'],
                        'MatchWeek' = row['Rodada'], 'Year' = row['Year'])
            DB_list.append(partida)
        return DB_list

    @staticmethod
    def Df2Db_Position(df):
        DB_list = []
        for index, row in df.iterrows():
            posicao = Position('ID' = row['ID'], 'Name' = row['Nome'], 'NickName' = row['Abreviacao'])
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
            scouts = Scout('ID'= index, 'PlayerID'= row['Atleta'], 'MatchWeek'= row['Rodada'],
                      'TeamID'= row['Clube'], 'HasPlayed'= status, 'Points'= row['Pontos'],
                      'AveragePoints'= row['PontosMedia'], 'Price'= row['Preco'],
                      'DeltaPrice'= row['PrecoVariacao'], 'MatchID'= row['Partida'], 'HomeGame'= row['Mando'],
                      'Score'= row['Nota'], 'Plays'= Play_list,
                      'Year'= row['Year'])
            DB_list.append(scouts)
        return DB_list

    @staticmethod
    def Df2Db_Skill():
        DB_list = []
        for index in range(0, len(abreviacao)):
            skill = Skill('ID' = index, 'Name'= descricao[index], 'NickName'= abreviacao[index], 'Points'= pontuacao[index])
            DB_list.append(skill)
        return DB_list

    @staticmethod
    def Df2Db_Team(df):
        DB_list = []
        for index, row in df.iterrows():
            times = Team('ID'= row['ID'], 'Name'= row['Slug'], 'NickName'= row['Abreviacao'], 'Year'= row['Year'])
            DB_list.append(times)
        return DB_list


