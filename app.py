from modules.csv2python import Csv2Python
from modules.pandas2db import Pandas2DB
from connectors.postgree import PostGreConnector, PostGreConnectorSQL
from modules.feature_queries import FeatureQueries
import pandas as pd
import time
from modules.feature_calculator import FeatureCalculator



## Code user to dump the csv files to postgres database
## DELETING ALL TABLES
# # pgcon = PostGreConnector()
# # pgcon.DropAll()

# # Reading csvs into Pandas
# # atletas = Csv2Python.read_players()
# # partidas = Csv2Python.read_matches()
# # times = Csv2Python.read_teams()
# # posicoes = Csv2Python.read_positions()
# scouts = Csv2Python.read_scouts()

# # Convert pandas into sql elements
# pdcon = Pandas2DB()
# pdcon.createtables()
# # print('Tabelas Criadas')
# # Pandas2DB().InsertTeam(times)
# # print('Times inseridos')
# # Pandas2DB().InsertSkill()
# # print('Skills inseridos')
# # Pandas2DB().InsertPosition(posicoes)
# # print('Posições inseridos')
# # Pandas2DB().InsertPlayer(atletas)
# # print('Jogadores inseridos')
# # Pandas2DB().InsertMatch(partidas)
# # print('Partidas inseridas')
# Pandas2DB().InsertScout(scouts)
# print('Scouts inseridos')


pg = PostGreConnectorSQL()
fc = FeatureCalculator()
scout_list = fc.generate_feature_queries(20000, 20100)
fc.parallel_calculation(scout_list)
sl = fc.get_scout_list()
print(sl)
#
# df = pg.execute_query(test.feature_query)
# print(df)
