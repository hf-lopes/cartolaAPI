from modules.csv2python import Csv2Python
from modules.pandas2db import Pandas2DB
import pandas as pd



atletas = Csv2Python.read_players()
partidas = Csv2Python.read_matches()
scouts = Csv2Python.read_scouts()
times = Csv2Python.read_teams()
posicoes = Csv2Python.read_positions()


Pandas2DB().createtables()
Pandas2DB().InsertTeam(times)
Pandas2DB().InsertSkill()
Pandas2DB().InsertPosition(posicoes)
Pandas2DB().InsertPlayer(atletas)
Pandas2DB().InsertMatch(partidas)
Pandas2DB().InsertScout(scouts)

