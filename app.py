from modules.csv2python import Csv2Python
from modules.pandas2db import Pandas2DB
from connectors.postgree import PostGreConnector
import pandas as pd


# pgcon = PostGreConnector()
# pgcon.DropAll()

atletas = Csv2Python.read_players()
partidas = Csv2Python.read_matches()
scouts = Csv2Python.read_scouts()
times = Csv2Python.read_teams()
posicoes = Csv2Python.read_positions()

pdcon = Pandas2DB()
pdcon.createtables()
# print('Tabelas Criadas')
# Pandas2DB().InsertTeam(times)
# print('Times inseridos')
# Pandas2DB().InsertSkill()
# print('Skills inseridos')
# Pandas2DB().InsertPosition(posicoes)
# print('Posições inseridos')
# Pandas2DB().InsertPlayer(atletas)
# print('Jogadores inseridos')
# Pandas2DB().InsertMatch(partidas)
# print('Partidas inseridas')
Pandas2DB().InsertScout(scouts)
print('Scouts inseridos')

