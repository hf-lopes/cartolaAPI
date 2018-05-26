from data_science_utils.feature_creation.filters import *
from data_science_utils.feature_creation.getters import *
from data_science_utils.feature_creation.aggregators import *

def getAveragePositionPoints(df, scout_id, num_rounds):
    return getStats(df, scout_id, num_rounds, "Pontos",
                    composeGetters(getPosicao),
                    filterDf, getColumnAverageLastRounds)

def getAveragePositionPointsHome(df, scout_id, num_rounds):
    return getStats(df, scout_id, num_rounds, "Pontos",
                    composeGetters(getPosicao, getAtHome),
                    filterDf, getColumnAverageLastRounds)


def getAveragePositionPointsAway(df, scout_id, num_rounds):
    return getStats(df, scout_id, num_rounds, "Pontos",
                    composeGetters(getPosicao, getAtAway),
                    filterDf, getColumnAverageLastRounds)


def getStdPositionPoints(df, scout_id, num_rounds):
    return getStats(df, scout_id, num_rounds, "Pontos",
                    composeGetters(getPosicao),
                    filterDf, getColumnStdDevLastRounds)


def getStdPositionPointsHome(df, scout_id, num_rounds):
    return getStats(df, scout_id, num_rounds, "Pontos",
                    composeGetters(getPosicao, getAtHome),
                    filterDf, getColumnStdDevLastRounds)


def getStdPositionPointsAway(df, scout_id, num_rounds):
    return getStats(df, scout_id, num_rounds, "Pontos",
                    composeGetters(getPosicao, getAtAway),
                    filterDf, getColumnStdDevLastRounds)


def getAveragePositionPointsWin(df, scout_id, num_rounds):
    return getStats(df, scout_id, num_rounds, "Pontos",
                    composeGetters(getPosicao, getWin),
                    filterDf, getColumnAverageLastRounds)


def getAveragePositionPointsDraw(df, scout_id, num_rounds):
    return getStats(df, scout_id, num_rounds, "Pontos",
                    composeGetters(getPosicao, getDraw),
                    filterDf, getColumnAverageLastRounds)


def getAveragePositionPointsLoss(df, scout_id, num_rounds):
    return getStats(df, scout_id, num_rounds, "Pontos",
                    composeGetters(getPosicao, getLoss),
                    filterDf, getColumnAverageLastRounds)
