import pandas as pd
import math
import numpy
from connectors.postgree import PostGreConnector
from constants import abreviacao, pontuacao, descricao

from models.Players import Player
from models.Matches import Match
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
        # self.db_con.InsertList(DB_list)
        self.db_con.InsertListParallel(DB_list, 10)

    def InsertMatch(self, df):
        DB_list = Pandas2DB.Df2Db_Match(df)
        # self.db_con.InsertList(DB_list)
        self.db_con.InsertListParallel(DB_list, 10)

    def InsertPosition(self, df):
        DB_list = Pandas2DB.Df2Db_Position(df)
        # self.db_con.InsertList(DB_list)
        self.db_con.InsertListParallel(DB_list, 1)

    def InsertScout(self, df):
        DB_list = Pandas2DB.Df2Db_Scout(df)
        # self.db_con.InsertList(DB_list)
        self.db_con.InsertListParallel(DB_list, 30)

    def InsertSkill(self):
        DB_list = Pandas2DB.Df2Db_Skill()
        # self.db_con.InsertList(DB_list)
        self.db_con.InsertListParallel(DB_list, 1)

    def InsertTeam(self, df):
        DB_list = Pandas2DB.Df2Db_Team(df)
        # self.db_con.InsertList(DB_list)
        self.db_con.InsertListParallel(DB_list, 1)

    @staticmethod
    def Df2Db_Player(df):
        DB_list = []
        for index, row in df.iterrows():
            if not math.isnan(row['Clube']):
                jogador = Player(player_id = int(row['ID']), name = row['Apelido'], team_id = int(row['Clube']), position_id = int(row['Posicao']),
                            year = row['Year'])
                DB_list.append(jogador)
            else:
                print('Player has no TeamID')
        return DB_list

    @staticmethod
    def Df2Db_Match(df):
        DB_list = []
        for index, row in df.iterrows():
            partida = Match(id = row['ID'] - 179872, home_team_id = int(row['Casa']), visiting_team_id = int(row['Visitante']), result = row['Resultado'],
                       home_score = int(row['PlacarCasa']), visiting_score= int(row['PlacarVisitante']),
                        match_week = row['Rodada'], year = row['Year'])
            DB_list.append(partida)
        return DB_list

    @staticmethod
    def Df2Db_Position(df):
        DB_list = []
        for index, row in df.iterrows():
            posicao = Position(id = row['ID'], name = row['Nome'], nickname = row['Abreviacao'])
            DB_list.append(posicao)
        return DB_list

    @staticmethod
    def Df2Db_Scout(df):
        DB_list = []
        for index, row in df.iterrows():
            Play_list = []
            for sigla in abreviacao:
                Play_list.append(int(row[sigla]))
            if not math.isnan(row['ClubeID']):
                scouts = Scout(player_id= int(row['AtletaID']), match_week = int(row['Rodada']),
                          team_id= row['ClubeID'], has_played= bool(row['Participou']), points= float(row['Pontos']),
                          average_points= float(row['PontosMedia']), price= float(row['Preco']),
                          delta_price= float(row['PrecoVariacao']), plays= Play_list,
                          year= int(row['Year']))
                DB_list.append(scouts)
        return DB_list

    @staticmethod
    def Df2Db_Skill():
        DB_list = []
        for index in range(0, len(abreviacao)):
            skill = Skill(id = index, name= descricao[index], nickname= abreviacao[index], points= pontuacao[index])
            DB_list.append(skill)
        return DB_list

    @staticmethod
    def Df2Db_Team(df):
        DB_list = []
        for index, row in df.iterrows():
            times = Team(id= row['ID'], name= row['Slug'], nickname= row['Abreviacao'], year= row['Year'])
            DB_list.append(times)
        return DB_list


