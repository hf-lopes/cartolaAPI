import pandas
from constants import ROOT_DIR


class Csv2Python:

    @staticmethod
    def read_csv(file_name):
        return pandas.read_csv(ROOT_DIR + '/' + file_name)

    @staticmethod
    def read_multiple_csv(file_name_list, yearly = True):
        df_list = []
        year = 2014
        for file in file_name_list:
            df = pandas.read_csv(ROOT_DIR + '/' + file)
            if yearly:
                df.loc[:, 'Year'] = year
            else:
                df.loc[:, 'Year'] = 2014
            year += 1
            df_list.append(df)
        df = pandas.concat(df_list)
        if 'ID' in df:
            print('Eliminando Duplicados')
            df = df.drop_duplicates('ID', keep='last')
            # print(df)
        return df

    @staticmethod
    def read_players():
        atletas = Csv2Python.read_multiple_csv(['db/2014/Atletas.csv', 'db/2015/Atletas.csv', 'db/2016/Atletas.csv'])
        atletas = Csv2Python.merge_columns(atletas, 'Clube', 'ClubeID')
        atletas = Csv2Python.merge_columns(atletas, 'Posicao', 'PosicaoID')
        return atletas

    @staticmethod
    def read_teams():
        clubes = Csv2Python.read_multiple_csv(['db/2014/Clubes.csv', 'db/2015/Clubes.csv', 'db/2016/Clubes.csv'])
        return clubes

    @staticmethod
    # Descontinued after 2014
    def read_plays():
        jogadas = Csv2Python.read_multiple_csv(['db/2014/Lances.csv'])
        return jogadas

    @staticmethod
    def read_matches():
        partidas = Csv2Python.read_multiple_csv(['db/2014/Partidas.csv', 'db/2015/Partidas.csv', 'db/2016/Partidas.csv'])
        partidas = Csv2Python.merge_columns(partidas, 'Visitante', 'VisitanteID')
        partidas = Csv2Python.merge_columns(partidas, 'Casa', 'CasaID')
        return partidas

    @staticmethod
    def read_positions():
        pos = Csv2Python.read_multiple_csv(['db/2014/Posicoes.csv', 'db/2015/Posicoes.csv', 'db/2016/Posicoes.csv'], False)
        return pos

    @staticmethod
    def read_scouts():
        scouts = Csv2Python.read_multiple_csv(['db/2014/Scouts.csv', 'db/2015/Scouts.csv', 'db/2016/Scouts.csv'])
        scouts = Csv2Python.merge_columns(scouts, 'Clube', 'ClubeID')
        scouts = Csv2Python.merge_columns(scouts, 'Atleta', 'AtletaID')
        return scouts

    @staticmethod
    def merge_columns(df, col1, col2):
        df[col1] = df[col1].fillna(df[col2])
        del df[col2]
        return df