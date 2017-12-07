from connectors.postgree import PostGreConnectorSQL, PostGreConnector
from resources.feature_calculator import FeatureCalculator



## Code user to dump the csv files to postgres database
## DELETING ALL TABLES
pgcon = PostGreConnector()
# # pgcon.DropAll()
pgcon.CreateAllTables()

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


fc = FeatureCalculator()
scout_list = fc.parallel_calculation(20000, 20100)
#
# df = pg.execute_query(test.feature_query)
# print(df)
