import pandas
from constants import ROOT_DIR


class Csv2Python:

    @staticmethod
    def read_csv(file_name, delimiter = ','):
        return pandas.read_csv(ROOT_DIR + '/' + file_name, delimiter=delimiter)

    @staticmethod
    def read_multiple_csv(file_name_list, yearly = True, remove_repeated=True):
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
        if remove_repeated and 'ID' in df:
            print('Eliminando Duplicados')
            df = df.drop_duplicates('ID', keep='last')
        return df

    @staticmethod
    def read_players():
        # atletas = Csv2Python.read_multiple_csv(['db/2014/Atletas.csv', 'db/2015/Atletas.csv', 'db/2016/Atletas.csv'], remove_repeated=False)
        atletas = Csv2Python.read_csv('db/2017/Atletas.csv')
        return atletas

    @staticmethod
    def read_teams():
        clubes = Csv2Python.read_multiple_csv(['db/2014/Clubes.csv', 'db/2015/Clubes.csv', 'db/2016/Clubes.csv'])
        clubes = Csv2Python.read_csv('db/2017/Clubes.csv', delimiter=';')
        return clubes

    @staticmethod
    # Descontinued after 2014
    def read_plays():
        jogadas = Csv2Python.read_multiple_csv(['db/2014/Lances.csv'])
        return jogadas

    @staticmethod
    def read_matches():
        partidas = Csv2Python.read_multiple_csv(['db/2014/Partidas.csv', 'db/2015/Partidas.csv', 'db/2016/Partidas.csv'])

        partidas = Csv2Python.read_csv('db/2017/Partidas.csv')
        partidas = partidas.drop(['date'], axis=1)
        partidas['home_score'] = partidas.score.str.split(' ').str[0]
        partidas['away_score'] = partidas.score.str.split(' ').str[2]
        home_win =  partidas.loc[partidas['home_score'] > partidas['away_score']]
        empate = partidas.loc[partidas['home_score'] == partidas['away_score']]
        away_win = partidas.loc[partidas['home_score'] < partidas['away_score']]
        home_win['result'] = 'Casa'
        empate['result'] = 'Empate'
        away_win['result'] = 'Visitante'
        partidas = pandas.concat([home_win, empate, away_win], axis=0)
        print(partidas)
        return partidas

    @staticmethod
    def read_positions():
        pos = Csv2Python.read_multiple_csv(['db/2014/Posicoes.csv', 'db/2015/Posicoes.csv', 'db/2016/Posicoes.csv'], False)
        return pos

    @staticmethod
    def read_scouts():
        # scouts = Csv2Python.read_multiple_csv(['db/2014/Scouts.csv', 'db/2015/Scouts.csv', 'db/2016/Scouts.csv'])
        # scouts = Csv2Python.read_csv('db/2017/Scouts.csv')
        # scouts.drop(['atletas.apelido', 'atletas.foto', 'atletas.nome'], axis=1)
        # scouts['jogou'] = False
        # for atleta in scouts.atletas_atleta_id.unique():
        #     aux = scouts.loc[scouts.atletas_atleta_id == atleta]
        #     i = 0
        #     for index, row in aux.iterrows():
        #         if i + 1 < aux.shape[0] and aux.iloc[i + 1]['atletas.jogos_num'] == aux.iloc[i]['atletas.jogos_num'] + 1:
        #             print('JOGOU', row['ID'])
        #             scouts.loc[scouts.ID == row['ID']]['jogou'] = True
        #         i += 1
        #
        # scouts.fillna(0, inplace=True)
        # scouts.to_csv('db/2017/Scouts_corrigidos.csv')
        # return scouts
        print('uau')
        df = Csv2Python.read_csv('db/2017/Scouts.csv')
        df_final = pandas.DataFrame()
        for round_ in range(1,39):
            suffixes = ('_curr', '_prev')

            cols_scouts = ['RB', 'FC', 'GC', 'CA', 'CV', 'SG', 'DD', 'DP', 'GS',
                          'FS', 'PE', 'A', 'FT', 'FD', 'FF', 'G', 'I', 'PP']

            cols_current = [col + suffixes[0] for col in cols_scouts]
            cols_prev = [col + suffixes[1] for col in cols_scouts]

            df_round = df[df['Rodada'] == round_]
            if round_ == 1:
                df_players = df_round
                df_players['Participou'] = False
            else:
                df_round_prev = df[df['Rodada'] < round_].groupby('AtletaID', as_index=False)[cols_scouts].max()
                df_jogos = df[df['Rodada'] < round_].groupby('AtletaID', as_index=False)['Jogos'].max()
                df_players = df_round.merge(df_round_prev, how='left', on=['AtletaID'], suffixes=suffixes)
                df_players = df_players.merge(df_jogos, how='left', on=['AtletaID'], suffixes=suffixes)
                # if is the first round of a player, the scouts of previous rounds will be NaNs. Thus, set them to zero
                df_players.fillna(value=0, inplace=True)
                print(df.columns)
                # compute the scouts
                df_players[cols_current] = df_players[cols_current].values - df_players[cols_prev].values
                df_players['Participou'] = df_players['Jogos_curr'].values - df_players['Jogos_prev'].values
                # update the columns
                df_players.drop(['Jogos_prev'], axis=1, inplace=True)
                df_players.drop(labels=cols_prev, axis=1, inplace=True)
                df_players = df_players.rename(columns=dict(zip(cols_current, cols_scouts)))
                df_players = df_players.rename(columns=dict(zip('Jogos_curr', 'Jogos')))
                df_players.SG = df_players.SG.clip_lower(0)

            print(df_final)
            df_final = pandas.concat([df_final, df_players])
        df_final['Year'] = 2017
        return df_final


    @staticmethod
    def merge_columns(df, col1, col2):
        df[col1] = df[col1].fillna(df[col2])
        del df[col2]
        return df