from modules.csv2python import Csv2Python

atletas = Csv2Python.read_csv('db/2014/Atletas.csv')
clubes = Csv2Python.read_csv('db/2014/Clubes.csv')
lances = Csv2Python.read_csv('db/2014/Lances.csv')
partidas = Csv2Python.read_csv('db/2014/Partidas.csv')
posicoes = Csv2Python.read_csv('db/2014/Posicoes.csv')
scouts = Csv2Python.read_csv('db/2014/Scouts.csv')
print(list(scouts))
