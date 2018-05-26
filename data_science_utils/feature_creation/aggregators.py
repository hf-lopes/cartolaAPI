from data_science_utils.feature_creation.filters import *

def getColumnAverageLastRounds(df, ano, rodada, column_name, num_rounds):
    return filterDfLastRounds(df, rodada, ano, num_rounds)[column_name].mean()

def getColumnStdDevLastRounds(df, ano, rodada, column_name, num_rounds):
    return filterDfLastRounds(df, rodada, ano, num_rounds)[column_name].std()

def getColumnSumLastRounds(df, ano, rodada, column_name, num_rounds):
    return filterDfLastRounds(df, rodada, ano, num_rounds)[column_name].sum()

def getColumnCountLastRounds(df, ano, rodada, column_name, num_rounds):
    return filterDfLastRounds(df, rodada, ano, num_rounds)[column_name].count()
