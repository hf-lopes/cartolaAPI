from data_science_utils.feature_creation.filters import *
from data_science_utils.feature_creation.getters import *
from data_science_utils.feature_creation.aggregators import *
from data_science_utils.feature_creation.team_features import *

def getAveragePlay(df, scout_id, num_rounds, play_name):

    return getStats(df, scout_id, num_rounds, play_name,
                    composeGetters(getAtletaID),
                    filterDf, getColumnAverageLastRounds)



def getAveragePlayHome(df, scout_id, num_rounds, play_name):

    return getStats(df, scout_id, num_rounds, play_name,
                    composeGetters(getAtletaID, getAtHome),
                    filterDf, getColumnAverageLastRounds)


def getAveragePlayAway(df, scout_id, num_rounds, play_name):

    return getStats(df, scout_id, num_rounds, play_name,
                    composeGetters(getAtletaID, getAtAway),
                    filterDf, getColumnAverageLastRounds)


def getStdDevPlay(df, scout_id, num_rounds, play_name):

    return getStats(df, scout_id, num_rounds, play_name,
                    composeGetters(getAtletaID),
                    filterDf, getColumnStdDevLastRounds)



def getStdDevPlayHome(df, scout_id, num_rounds, play_name):

    return getStats(df, scout_id, num_rounds, play_name,
                    composeGetters(getAtletaID, getAtHome),
                    filterDf, getColumnStdDevLastRounds)


def getStdDevPlayAway(df, scout_id, num_rounds, play_name):

    return getStats(df, scout_id, num_rounds, play_name,
                    composeGetters(getAtletaID, getAtAway),
                    filterDf, getColumnStdDevLastRounds)


def cleanSheetChance(df, scout_id, num_rounds):
    return getAveragePlay(df, scout_id, num_rounds, 'SG') / (
        getEnemyGoalsScored(df, scout_id, num_rounds) *
        getTeamGoalsTaken(df, scout_id, num_rounds))


def cleanSheetChanceHome(df, scout_id, num_rounds):
    return getAveragePlayHome(df, scout_id, num_rounds, 'SG') / (
        getEnemyGoalsScoredAway(df, scout_id, num_rounds) *
        getTeamGoalsTakenHome(df, scout_id, num_rounds))

def cleanSheetChanceAway(df, scout_id, num_rounds):
    return getAveragePlayAway(df, scout_id, num_rounds, 'SG') / (
        getEnemyGoalsScoredHome(df, scout_id, num_rounds) *
        getTeamGoalsTakenAway(df, scout_id, num_rounds))

def playerGoalParticipation(df, scout_id, num_rounds):
    return (getAveragePlay(df, scout_id, num_rounds, 'G') * points_dict['G'] +
            getAveragePlay(df, scout_id, num_rounds, 'A') * points_dict['A'] +
            getAveragePlay(df, scout_id, num_rounds, 'FT') * points_dict['FT'] +
            getAveragePlay(df, scout_id, num_rounds, 'FF') * points_dict['FF'] +
            getAveragePlay(df, scout_id, num_rounds, 'FD') * points_dict['FD']) / (
            getTeamGoalsScored(df, scout_id, num_rounds) *
            getEnemyGoalsTaken(df, scout_id, num_rounds))


def playerGoalParticipationHome(df, scout_id, num_rounds):
    return (getAveragePlayHome(df, scout_id, num_rounds, 'G') * points_dict['G'] +
            getAveragePlayHome(df, scout_id, num_rounds, 'A') * points_dict['A'] +
            getAveragePlayHome(df, scout_id, num_rounds, 'FT') * points_dict['FT'] +
            getAveragePlayHome(df, scout_id, num_rounds, 'FF') * points_dict['FF'] +
            getAveragePlayHome(df, scout_id, num_rounds, 'FD') * points_dict['FD']) / (
            getTeamGoalsScoredHome(df, scout_id, num_rounds) *
            getEnemyGoalsTakenAway(df, scout_id, num_rounds))


def playerGoalParticipationAway(df, scout_id, num_rounds):
    return (getAveragePlayAway(df, scout_id, num_rounds, 'G') * points_dict['G'] +
            getAveragePlayAway(df, scout_id, num_rounds, 'A') * points_dict['A'] +
            getAveragePlayAway(df, scout_id, num_rounds, 'FT') * points_dict['FT'] +
            getAveragePlayAway(df, scout_id, num_rounds, 'FF') * points_dict['FF'] +
            getAveragePlayAway(df, scout_id, num_rounds, 'FD') * points_dict['FD']) / (
            getTeamGoalsScoredAway(df, scout_id, num_rounds) *
            getEnemyGoalsTakenHome(df, scout_id, num_rounds))



