from toolz.curried import *


def getStats(df, scout_id, num_rounds, column_name, getter_fn, filter_fn,
             agg_fn):
    rodada, ano = getRodada(df, scout_id)["Rodada"], getAno(df, scout_id)[
        "ano"]
    filters = getter_fn(df, scout_id)
    df_filtered = filter_fn(df, filters)

    return agg_fn(df_filtered, ano, rodada, column_name, num_rounds)


def composeGetters(*getters):
    def g(df, scout_id):
        return merge(map(lambda x: x(df, scout_id), getters))

    return g


def getter(df, scout_id, column_name):
    return {column_name: df.loc[scout_id][column_name]}


def getAtletaID(df, scout_id):
    return getter(df, scout_id, column_name="AtletaID")


def getClubeID(df, scout_id):
    return getter(df, scout_id, column_name="ClubeID")


def getClubeVisitante(df, scout_id):
    return getter(df, scout_id, column_name="ClubeVisitante")


def getClubeCasa(df, scout_id):
    return getter(df, scout_id, column_name="ClubeCasa")


def getPosicao(df, scout_id):
    return getter(df, scout_id, column_name="Posicao")


def getRodada(df, scout_id):
    return getter(df, scout_id, column_name="Rodada")


def getAno(df, scout_id):
    return getter(df, scout_id, column_name="ano")


def getIsHome(df, scout_id):
    return getter(df, scout_id, column_name="Home")


def getResult(df, scout_id):
    return getter(df, scout_id, column_name="result")


def getWin(df, scout_id):
    return {"game_points": 3}


def getDraw(df, scout_id):
    return {"game_points": 1}


def getLoss(df, scout_id):
    return {"game_points": 0}


def getAtHome(df, scout_id):
    return {"Home": True}


def getAtAway(df, scout_id):
    return {"Home": False}


def getEnemyTeam(df, scout_id):
    return {"ClubeID": getClubeVisitante(df, scout_id)["ClubeVisitante"] if
    getIsHome(df, scout_id)["Home"] else getClubeCasa(df, scout_id)[
        "ClubeCasa"]}
