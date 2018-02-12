from modules.csv2python import Csv2Python
from modules.pandas2db import Pandas2DB
from connectors.postgree import PostGreConnector, PostGreConnectorSQL
from modules.feature_queries import FeatureQueries
import pandas as pd
import time
from resources.feature_calculator import FeatureCalculator




## Code user to dump the csv files to postgres database
## DELETING ALL TABLES
# pgcon = PostGreConnector()
# # pgcon.DropAll()
# pgcon.CreateAllTables()

# Reading csvs into Pandas
# atletas = Csv2Python.read_players()
# partidas = Csv2Python.read_matches()
# times = Csv2Python.read_teams()
# posicoes = Csv2Python.read_positions()
# scouts = Csv2Python.read_scouts()
# print(scouts.columns)



# Convert pandas into sql elements
# pdcon = Pandas2DB()
# pdcon.createtables()
# print('Tabelas Criadas')


# Pandas2DB().InsertTeam(times)
# print('Times inseridos')


# Pandas2DB().InsertSkill()
# print('Skills inseridos')
# Pandas2DB().InsertPosition(posicoes)
# print('Posicoes inseridos')


# Pandas2DB().InsertPlayer(atletas)
# print('Jogadores inseridos')
# Pandas2DB().InsertMatch(partidas)
# print('Partidas inseridas')
# Pandas2DB().InsertScout(scouts)
# print('Scouts inseridos')

#
pg = PostGreConnectorSQL()
fc = FeatureCalculator()
fc.parallel_calculation(19356, 253493)

# df = pg.execute_query(test.feature_query)
# print(df)
# mc = ModelCalculation('245529727693709252570461385261081329471')
# mc.NN()

