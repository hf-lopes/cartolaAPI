from toolz.curried import *
from data_science_utils.feature_creation.getters import *

def filterDfLastRounds(df, rodada, ano, num_rounds):
    return df.loc[(((df.ano == ano) & (df.Rodada < rodada) & (df.Rodada >= rodada - num_rounds))
                                                | ((df.ano == ano - 1) & (df.Rodada >= 38 + rodada - num_rounds)))]

def filterDf(df, data):
    filters = list(zip(list(data.keys()), list(data.values())))
    b = list(map(lambda y: (df[y[0]] == y[1]), filters))
    return df.loc[reduce(lambda x, y: x & y, b)]
