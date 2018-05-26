from data_science_utils.feature_creation.filters import *
from data_science_utils.feature_creation.getters import *
from data_science_utils.feature_creation.aggregators import *
from constants import points_dict

def getAverageTeamPlay(df, scout_id, num_rounds, play_name):
    return getStats(df, scout_id, num_rounds, play_name,
                    composeGetters(getClubeID),
                    filterDf, getColumnAverageLastRounds)


def getAverageTeamPlayHome(df, scout_id, num_rounds, play_name):
    return getStats(df, scout_id, num_rounds, play_name,
                    composeGetters(getClubeID, getAtHome),
                    filterDf, getColumnAverageLastRounds)


def getAverageTeamPlayAway(df, scout_id, num_rounds, play_name):
    return getStats(df, scout_id, num_rounds, play_name,
                    composeGetters(getClubeID, getAtAway),
                    filterDf, getColumnAverageLastRounds)


def getStdDevTeamPlay(df, scout_id, num_rounds, play_name):
    return getStats(df, scout_id, num_rounds, play_name,
                    composeGetters(getClubeID),
                    filterDf, getColumnStdDevLastRounds)


def getStdDevTeamPlayHome(df, scout_id, num_rounds, play_name):
    return getStats(df, scout_id, num_rounds, play_name,
                    composeGetters(getClubeID, getAtHome),
                    filterDf, getColumnStdDevLastRounds)


def getStdDevTeamPlayAway(df, scout_id, num_rounds, play_name):
    return getStats(df, scout_id, num_rounds, play_name,
                    composeGetters(getClubeID, getAtAway),
                    filterDf, getColumnStdDevLastRounds)


def getAverageEnemyPlay(df, scout_id, num_rounds, play_name):
    return getStats(df, scout_id, num_rounds, play_name,
                    composeGetters(getEnemyTeam),
                    filterDf, getColumnAverageLastRounds)


def getAverageEnemyPlayHome(df, scout_id, num_rounds, play_name):
    return getStats(df, scout_id, num_rounds, play_name,
                    composeGetters(getEnemyTeam, getAtHome),
                    filterDf, getColumnAverageLastRounds)


def getAverageEnemyPlayAway(df, scout_id, num_rounds, play_name):
    return getStats(df, scout_id, num_rounds, play_name,
                    composeGetters(getEnemyTeam, getAtAway),
                    filterDf, getColumnAverageLastRounds)


def getStdDevEnemyPlay(df, scout_id, num_rounds, play_name):
    return getStats(df, scout_id, num_rounds, play_name,
                    composeGetters(getEnemyTeam),
                    filterDf, getColumnStdDevLastRounds)


def getStdDevEnemyPlayHome(df, scout_id, num_rounds, play_name):
    return getStats(df, scout_id, num_rounds, play_name,
                    composeGetters(getEnemyTeam, getAtHome),
                    filterDf, getColumnStdDevLastRounds)


def getStdDevEnemyPlayAway(df, scout_id, num_rounds, play_name):
    return getStats(df, scout_id, num_rounds, play_name,
                    composeGetters(getEnemyTeam, getAtAway),
                    filterDf, getColumnStdDevLastRounds)


def getTeamGoalsScored(df, scout_id, num_rounds):
    sum_goals_home = getStats(df, scout_id, num_rounds, "home_score",
                              composeGetters(getClubeID, getAtHome),
                              filterDf, getColumnSumLastRounds)

    sum_goals_away = getStats(df, scout_id, num_rounds, "away_score",
                              composeGetters(getClubeID, getAtAway),
                              filterDf, getColumnSumLastRounds)

    count_games = getStats(df, scout_id, num_rounds, "home_score",
                           getClubeID, filterDf, getColumnCountLastRounds)

    return (sum_goals_home + sum_goals_away) / count_games


def getTeamGoalsTaken(df, scout_id, num_rounds):
    sum_goals_home = getStats(df, scout_id, num_rounds, "away_score",
                              composeGetters(getClubeID, getAtHome),
                              filterDf, getColumnSumLastRounds)

    sum_goals_away = getStats(df, scout_id, num_rounds, "home_score",
                              composeGetters(getClubeID, getAtAway),
                              filterDf, getColumnSumLastRounds)

    count_games = getStats(df, scout_id, num_rounds, "home_score",
                           getClubeID, filterDf, getColumnCountLastRounds)

    return (sum_goals_home + sum_goals_away) / count_games


def getEnemyGoalsScored(df, scout_id, num_rounds):
    sum_goals_home = getStats(df, scout_id, num_rounds, "home_score",
                              composeGetters(getEnemyTeam, getAtHome),
                              filterDf, getColumnSumLastRounds)

    sum_goals_away = getStats(df, scout_id, num_rounds, "away_score",
                              composeGetters(getEnemyTeam, getAtAway),
                              filterDf, getColumnSumLastRounds)

    count_games = getStats(df, scout_id, num_rounds, "home_score",
                           getEnemyTeam, filterDf, getColumnCountLastRounds)

    return (sum_goals_home + sum_goals_away) / count_games


def getEnemyGoalsTaken(df, scout_id, num_rounds):
    sum_goals_home = getStats(df, scout_id, num_rounds, "away_score",
                              composeGetters(getEnemyTeam, getAtHome),
                              filterDf, getColumnSumLastRounds)

    sum_goals_away = getStats(df, scout_id, num_rounds, "home_score",
                              composeGetters(getEnemyTeam, getAtAway),
                              filterDf, getColumnSumLastRounds)

    count_games = getStats(df, scout_id, num_rounds, "home_score",
                           getEnemyTeam, filterDf, getColumnCountLastRounds)

    return (sum_goals_home + sum_goals_away) / count_games


def getTeamGoalsScoredHome(df, scout_id, num_rounds):
    return getAverageTeamPlayHome(df, scout_id, num_rounds, "home_score")


def getTeamGoalsScoredAway(df, scout_id, num_rounds):
    return getAverageTeamPlayAway(df, scout_id, num_rounds, "away_score")


def getTeamGoalsTakenHome(df, scout_id, num_rounds):
    return getAverageTeamPlayHome(df, scout_id, num_rounds, "away_score")


def getTeamGoalsTakenAway(df, scout_id, num_rounds):
    return getAverageTeamPlayAway(df, scout_id, num_rounds, "home_score")


def getEnemyGoalsScoredHome(df, scout_id, num_rounds):
    return getAverageEnemyPlayHome(df, scout_id, num_rounds, "home_score")


def getEnemyGoalsScoredAway(df, scout_id, num_rounds):
    return getAverageEnemyPlayAway(df, scout_id, num_rounds, "away_score")


def getEnemyGoalsTakenHome(df, scout_id, num_rounds):
    return getAverageEnemyPlayHome(df, scout_id, num_rounds, "away_score")


def getEnemyGoalsTakenAway(df, scout_id, num_rounds):
    return getAverageEnemyPlayAway(df, scout_id, num_rounds, "home_score")


def getTeamScoredEnemyTakenRatio(df, scout_id, num_rounds):
    return getTeamGoalsScored(df, scout_id, num_rounds) / getEnemyGoalsTaken(
        df, scout_id, num_rounds)


def getTeamScoredEnemyTakenRatioHome(df, scout_id, num_rounds):
    return getTeamGoalsScoredHome(df, scout_id,
                                  num_rounds) / getEnemyGoalsTakenAway(df,
                                                                       scout_id,
                                                                       num_rounds)


def getTeamScoredEnemyTakenRatioAway(df, scout_id, num_rounds):
    return getTeamGoalsScoredAway(df, scout_id,
                                  num_rounds) / getEnemyGoalsTakenHome(df,
                                                                       scout_id,
                                                                       num_rounds)


def getTeamTakenEnemyScoredRatio(df, scout_id, num_rounds):
    return getTeamGoalsTaken(df, scout_id, num_rounds) / getEnemyGoalsScored(
        df, scout_id, num_rounds)


def getTeamTakenEnemyScoredRatioHome(df, scout_id, num_rounds):
    return getTeamGoalsTakenHome(df, scout_id,
                                 num_rounds) / getEnemyGoalsScoredAway(df,
                                                                       scout_id,
                                                                       num_rounds)


def getTeamTakenEnemyScoredRatioAway(df, scout_id, num_rounds):
    return getTeamGoalsTakenAway(df, scout_id,
                                 num_rounds) / getEnemyGoalsScoredHome(df,
                                                                       scout_id,
                                                                       num_rounds)


def getAverageTeamPoints(df, scout_id, num_rounds):
    return getAverageTeamPlay(df, scout_id, num_rounds, "Pontos")


def getAverageTeamPointsHome(df, scout_id, num_rounds):
    return getAverageTeamPlayHome(df, scout_id, num_rounds, "Pontos")


def getAverageTeamPointsAway(df, scout_id, num_rounds):
    return getAverageTeamPlayAway(df, scout_id, num_rounds, "Pontos")


def getAverageEnemyPoints(df, scout_id, num_rounds):
    return getAverageEnemyPlay(df, scout_id, num_rounds, "Pontos")


def getAverageEnemyPointsHome(df, scout_id, num_rounds):
    return getAverageEnemyPlayHome(df, scout_id, num_rounds, "Pontos")


def getAverageEnemyPointsAway(df, scout_id, num_rounds):
    return getAverageEnemyPlayAway(df, scout_id, num_rounds, "Pontos")


def getAverageTeamPointsEnemyRatio(df, scout_id, num_rounds):
    return getAverageTeamPoints(df, scout_id,
                                num_rounds) / getAverageEnemyPoints(df,
                                                                    scout_id,
                                                                    num_rounds)


def getAverageTeamPointsEnemyRatioHome(df, scout_id, num_rounds):
    return getAverageTeamPointsHome(df, scout_id,
                                    num_rounds) / getAverageEnemyPointsAway(df,
                                                                            scout_id,
                                                                            num_rounds)


def getAverageTeamPointsEnemyRatioAway(df, scout_id, num_rounds):
    return getAverageTeamPointsAway(df, scout_id,
                                    num_rounds) / getAverageEnemyPointsHome(df,
                                                                            scout_id,
                                                                            num_rounds)


def getStdTeamPoints(df, scout_id, num_rounds):
    return getStdDevTeamPlay(df, scout_id, num_rounds, "Pontos")


def getStdTeamPointsHome(df, scout_id, num_rounds):
    return getStdDevTeamPlayHome(df, scout_id, num_rounds, "Pontos")


def getStdTeamPointsAway(df, scout_id, num_rounds):
    return getStdDevTeamPlayAway(df, scout_id, num_rounds, "Pontos")


def getStdEnemyPoints(df, scout_id, num_rounds):
    return getStdDevEnemyPlay(df, scout_id, num_rounds, "Pontos")


def getStdEnemyPointsHome(df, scout_id, num_rounds):
    return getStdDevEnemyPlayHome(df, scout_id, num_rounds, "Pontos")


def getStdEnemyPointsAway(df, scout_id, num_rounds):
    return getStdDevEnemyPlayAway(df, scout_id, num_rounds, "Pontos")


def getStdTeamPointsEnemyRatio(df, scout_id, num_rounds):
    return (getAverageTeamPoints(df, scout_id, num_rounds) -
            getAverageEnemyPoints(df, scout_id,
                                  num_rounds)) / getStdTeamPoints(df, scout_id,
                                                                  num_rounds)


def getStdTeamPointsEnemyRatioHome(df, scout_id, num_rounds):
    return (getAverageTeamPointsHome(df, scout_id, num_rounds) -
            getAverageEnemyPointsAway(df, scout_id,
                                      num_rounds)) / getStdTeamPointsHome(df,
                                                                          scout_id,
                                                                          num_rounds)


def getStdTeamPointsEnemyRatioAway(df, scout_id, num_rounds):
    return (getAverageTeamPointsAway(df, scout_id, num_rounds) -
            getAverageEnemyPointsHome(df, scout_id,
                                      num_rounds)) / getStdTeamPointsAway(df,
                                                                          scout_id,
                                                                          num_rounds)


def getAverageTeamGamePoints(df, scout_id, num_rounds):
    return getAverageTeamPlay(df, scout_id, num_rounds, "game_points")


def getAverageTeamGamePointsHome(df, scout_id, num_rounds):
    return getAverageTeamPlayHome(df, scout_id, num_rounds, "game_points")


def getAverageTeamGamePointsAway(df, scout_id, num_rounds):
    return getAverageTeamPlayAway(df, scout_id, num_rounds, "game_points")


def getAverageEnemyGamePoints(df, scout_id, num_rounds):
    return getAverageEnemyPlay(df, scout_id, num_rounds, "game_points")


def getAverageEnemyGamePointsHome(df, scout_id, num_rounds):
    return getAverageEnemyPlayHome(df, scout_id, num_rounds, "game_points")


def getAverageEnemyGamePointsAway(df, scout_id, num_rounds):
    return getAverageEnemyPlayAway(df, scout_id, num_rounds, "game_points")


def getAverageTeamGamePointsEnemyRatio(df, scout_id, num_rounds):
    return getAverageTeamPoints(df, scout_id,
                                num_rounds) / getAverageEnemyPoints(df,
                                                                    scout_id,
                                                                    num_rounds)


def getAverageTeamGamePointsEnemyRatioHome(df, scout_id, num_rounds):
    return getAverageTeamGamePointsHome(df, scout_id,
                                        num_rounds) / getAverageEnemyGamePointsAway(
        df, scout_id, num_rounds)


def getAverageTeamGamePointsEnemyRatioAway(df, scout_id, num_rounds):
    return getAverageTeamGamePointsAway(df, scout_id,
                                        num_rounds) / getAverageEnemyGamePointsHome(
        df, scout_id, num_rounds)


def getStdTeamGamePoints(df, scout_id, num_rounds):
    return getStdDevTeamPlay(df, scout_id, num_rounds, "game_points")


def getStdTeamGamePointsHome(df, scout_id, num_rounds):
    return getStdDevTeamPlayHome(df, scout_id, num_rounds, "game_points")


def getStdTeamGamePointsAway(df, scout_id, num_rounds):
    return getStdDevTeamPlayAway(df, scout_id, num_rounds, "game_points")


def getStdEnemyGamePoints(df, scout_id, num_rounds):
    return getStdDevEnemyPlay(df, scout_id, num_rounds, "game_points")


def getStdEnemyGamePointsHome(df, scout_id, num_rounds):
    return getStdDevEnemyPlayHome(df, scout_id, num_rounds, "game_points")


def getStdEnemyGamePointsAway(df, scout_id, num_rounds):
    return getStdDevEnemyPlayAway(df, scout_id, num_rounds, "game_points")


def getStdTeamGamePointsEnemyRatio(df, scout_id, num_rounds):
    return (getAverageTeamGamePoints(df, scout_id, num_rounds) -
            getAverageEnemyGamePoints(df, scout_id,
                                      num_rounds)) / getStdTeamGamePoints(df,
                                                                          scout_id,
                                                                          num_rounds)


def getStdTeamGamePointsEnemyRatioHome(df, scout_id, num_rounds):
    return (getAverageTeamGamePointsHome(df, scout_id, num_rounds) -
            getAverageEnemyGamePointsAway(df, scout_id,
                                          num_rounds)) / getStdTeamGamePointsHome(
        df, scout_id, num_rounds)


def getStdTeamGamePointsEnemyRatioAway(df, scout_id, num_rounds):
    return (getAverageTeamGamePointsAway(df, scout_id, num_rounds) -
            getAverageEnemyGamePointsHome(df, scout_id,
                                          num_rounds)) / getStdTeamGamePointsAway(
        df, scout_id, num_rounds)


def getAverageTeamPrice(df, scout_id, num_rounds):
    return getAverageTeamPlay(df, scout_id, num_rounds, "Preco")


def getAverageEnemyPrice(df, scout_id, num_rounds):
    return getAverageEnemyPlay(df, scout_id, num_rounds, "Preco")


def getStdTeamPrice(df, scout_id, num_rounds):
    return getStdDevTeamPlay(df, scout_id, num_rounds, "Preco")


def getStdEnemyPrice(df, scout_id, num_rounds):
    return getStdDevEnemyPlay(df, scout_id, num_rounds, "Preco")


def getAverageTeamEnemyPriceRatio(df, scout_id, num_rounds):
    return getAverageTeamPrice(df, scout_id,
                               num_rounds) / getAverageEnemyPrice(df, scout_id,
                                                                  num_rounds)

def getAverageTeamOffenseEnemyDefenseRatio(df, scout_id, num_rounds):
    return (getAverageTeamPlay(df, scout_id, num_rounds, 'G') * points_dict['G'] +
            getAverageTeamPlay(df, scout_id, num_rounds, 'A') * points_dict['A'] +
            getAverageTeamPlay(df, scout_id, num_rounds, 'FT') * points_dict['FT'] +
            getAverageTeamPlay(df, scout_id, num_rounds, 'FF') * points_dict['FF'] +
            getAverageTeamPlay(df, scout_id, num_rounds, 'FD') * points_dict['FD'] +
            getAverageTeamPlay(df, scout_id, num_rounds, 'I') * points_dict['I'] +
            getAverageTeamPlay(df, scout_id, num_rounds, 'PP') * points_dict['PP']) / \
            (getAverageEnemyPlay(df, scout_id, num_rounds, 'RB') * points_dict['RB'] +
             getAverageEnemyPlay(df, scout_id, num_rounds, 'SG') * points_dict['SG'] +
             getAverageEnemyPlay(df, scout_id, num_rounds, 'DD') * points_dict['DD'] +
             getAverageEnemyPlay(df, scout_id, num_rounds, 'DP') * points_dict['DP'] +
             getAverageEnemyPlay(df, scout_id, num_rounds, 'FC') * points_dict['FC'] +
             getAverageEnemyPlay(df, scout_id, num_rounds, 'CA') * points_dict['CA'] +
             getAverageEnemyPlay(df, scout_id, num_rounds, 'CV') * points_dict['CV'])

def getAverageTeamOffenseEnemyDefenseRatioHome(df, scout_id, num_rounds):
    return (getAverageTeamPlayHome(df, scout_id, num_rounds, 'G') * points_dict['G'] +
            getAverageTeamPlayHome(df, scout_id, num_rounds, 'A') * points_dict['A'] +
            getAverageTeamPlayHome(df, scout_id, num_rounds, 'FT') * points_dict['FT'] +
            getAverageTeamPlayHome(df, scout_id, num_rounds, 'FF') * points_dict['FF'] +
            getAverageTeamPlayHome(df, scout_id, num_rounds, 'FD') * points_dict['FD'] +
            getAverageTeamPlayHome(df, scout_id, num_rounds, 'I') * points_dict['I'] +
            getAverageTeamPlayHome(df, scout_id, num_rounds, 'PP') * points_dict['PP']) / \
            (getAverageEnemyPlayAway(df, scout_id, num_rounds, 'RB') * points_dict['RB'] +
             getAverageEnemyPlayAway(df, scout_id, num_rounds, 'SG') * points_dict['SG'] +
             getAverageEnemyPlayAway(df, scout_id, num_rounds, 'DD') * points_dict['DD'] +
             getAverageEnemyPlayAway(df, scout_id, num_rounds, 'DP') * points_dict['DP'] +
             getAverageEnemyPlayAway(df, scout_id, num_rounds, 'FC') * points_dict['FC'] +
             getAverageEnemyPlayAway(df, scout_id, num_rounds, 'CA') * points_dict['CA'] +
             getAverageEnemyPlayAway(df, scout_id, num_rounds, 'CV') * points_dict['CV'])

def getAverageTeamOffenseEnemyDefenseRatioAway(df, scout_id, num_rounds):
    return (getAverageTeamPlayAway(df, scout_id, num_rounds, 'G') * points_dict['G'] +
            getAverageTeamPlayAway(df, scout_id, num_rounds, 'A') * points_dict['A'] +
            getAverageTeamPlayAway(df, scout_id, num_rounds, 'FT') * points_dict['FT'] +
            getAverageTeamPlayAway(df, scout_id, num_rounds, 'FF') * points_dict['FF'] +
            getAverageTeamPlayAway(df, scout_id, num_rounds, 'FD') * points_dict['FD'] +
            getAverageTeamPlayAway(df, scout_id, num_rounds, 'I') * points_dict['I'] +
            getAverageTeamPlayAway(df, scout_id, num_rounds, 'PP') * points_dict['PP']) / \
            (getAverageEnemyPlayHome(df, scout_id, num_rounds, 'RB') * points_dict['RB'] +
             getAverageEnemyPlayHome(df, scout_id, num_rounds, 'SG') * points_dict['SG'] +
             getAverageEnemyPlayHome(df, scout_id, num_rounds, 'DD') * points_dict['DD'] +
             getAverageEnemyPlayHome(df, scout_id, num_rounds, 'DP') * points_dict['DP'] +
             getAverageEnemyPlayHome(df, scout_id, num_rounds, 'FC') * points_dict['FC'] +
             getAverageEnemyPlayHome(df, scout_id, num_rounds, 'CA') * points_dict['CA'] +
             getAverageEnemyPlayHome(df, scout_id, num_rounds, 'CV') * points_dict['CV'])

def getAverageEnemyOffenseTeamDefenseRatio(df, scout_id, num_rounds):
    return (getAverageEnemyPlay(df, scout_id, num_rounds, 'G') * points_dict['G'] +
            getAverageEnemyPlay(df, scout_id, num_rounds, 'A') * points_dict['A'] +
            getAverageEnemyPlay(df, scout_id, num_rounds, 'FT') * points_dict['FT'] +
            getAverageEnemyPlay(df, scout_id, num_rounds, 'FF') * points_dict['FF'] +
            getAverageEnemyPlay(df, scout_id, num_rounds, 'FD') * points_dict['FD'] +
            getAverageEnemyPlay(df, scout_id, num_rounds, 'I') * points_dict['I'] +
            getAverageEnemyPlay(df, scout_id, num_rounds, 'PP') * points_dict['PP']) / \
            (getAverageTeamPlay(df, scout_id, num_rounds, 'RB') * points_dict['RB'] +
             getAverageTeamPlay(df, scout_id, num_rounds, 'SG') * points_dict['SG'] +
             getAverageTeamPlay(df, scout_id, num_rounds, 'DD') * points_dict['DD'] +
             getAverageTeamPlay(df, scout_id, num_rounds, 'DP') * points_dict['DP'] +
             getAverageTeamPlay(df, scout_id, num_rounds, 'FC') * points_dict['FC'] +
             getAverageTeamPlay(df, scout_id, num_rounds, 'CA') * points_dict['CA'] +
             getAverageTeamPlay(df, scout_id, num_rounds, 'CV') * points_dict['CV'])

def getAverageEnemyOffenseTeamDefenseRatioHome(df, scout_id, num_rounds):
    return (getAverageEnemyPlayAway(df, scout_id, num_rounds, 'G') * points_dict['G'] +
            getAverageEnemyPlayAway(df, scout_id, num_rounds, 'A') * points_dict['A'] +
            getAverageEnemyPlayAway(df, scout_id, num_rounds, 'FT') * points_dict['FT'] +
            getAverageEnemyPlayAway(df, scout_id, num_rounds, 'FF') * points_dict['FF'] +
            getAverageEnemyPlayAway(df, scout_id, num_rounds, 'FD') * points_dict['FD'] +
            getAverageEnemyPlayAway(df, scout_id, num_rounds, 'I') * points_dict['I'] +
            getAverageEnemyPlayAway(df, scout_id, num_rounds, 'PP') * points_dict['PP']) / \
            (getAverageTeamPlayHome(df, scout_id, num_rounds, 'RB') * points_dict['RB'] +
             getAverageTeamPlayHome(df, scout_id, num_rounds, 'SG') * points_dict['SG'] +
             getAverageTeamPlayHome(df, scout_id, num_rounds, 'DD') * points_dict['DD'] +
             getAverageTeamPlayHome(df, scout_id, num_rounds, 'DP') * points_dict['DP'] +
             getAverageTeamPlayHome(df, scout_id, num_rounds, 'FC') * points_dict['FC'] +
             getAverageTeamPlayHome(df, scout_id, num_rounds, 'CA') * points_dict['CA'] +
             getAverageTeamPlayHome(df, scout_id, num_rounds, 'CV') * points_dict['CV'])

def getAverageEnemyffenseTeamDefenseRatioAway(df, scout_id, num_rounds):
    return (getAverageEnemyPlayHome(df, scout_id, num_rounds, 'G') * points_dict['G'] +
            getAverageEnemyPlayHome(df, scout_id, num_rounds, 'A') * points_dict['A'] +
            getAverageEnemyPlayHome(df, scout_id, num_rounds, 'FT') * points_dict['FT'] +
            getAverageEnemyPlayHome(df, scout_id, num_rounds, 'FF') * points_dict['FF'] +
            getAverageEnemyPlayHome(df, scout_id, num_rounds, 'FD') * points_dict['FD'] +
            getAverageEnemyPlayHome(df, scout_id, num_rounds, 'I') * points_dict['I'] +
            getAverageEnemyPlayHome(df, scout_id, num_rounds, 'PP') * points_dict['PP']) / \
            (getAverageTeamPlayAway(df, scout_id, num_rounds, 'RB') * points_dict['RB'] +
             getAverageTeamPlayAway(df, scout_id, num_rounds, 'SG') * points_dict['SG'] +
             getAverageTeamPlayAway(df, scout_id, num_rounds, 'DD') * points_dict['DD'] +
             getAverageTeamPlayAway(df, scout_id, num_rounds, 'DP') * points_dict['DP'] +
             getAverageTeamPlayAway(df, scout_id, num_rounds, 'FC') * points_dict['FC'] +
             getAverageTeamPlayAway(df, scout_id, num_rounds, 'CA') * points_dict['CA'] +
             getAverageTeamPlayAway(df, scout_id, num_rounds, 'CV') * points_dict['CV'])

def getStdTeamEnemyPriceRatio(df, scout_id, num_rounds):
    return (getAverageTeamPrice(df, scout_id, num_rounds) -
            getAverageEnemyPrice(df, scout_id, num_rounds)) / getStdTeamPrice(
        df, scout_id, num_rounds)


