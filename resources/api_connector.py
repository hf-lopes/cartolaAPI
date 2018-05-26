import requests
import json
from constants import cartola_endpoint
import datetime as dt
from models.Scouts import Scout
from models.Matches import Match
from models.Players import Player
from models.Teams import Team
from sqlalchemy import update
import toolz as fp
## TODO: add player.status_id to db
## TODO: add match.clube_visitante / clube_casa_posicao to db
## TODO: add match.aproveitamento_mandante/aproveitamento_visitante to db
def _get_endpoint(endpoint_name, *kwargs):
    return (cartola_endpoint[endpoint_name] % kwargs)

def _get_dict_into_date(date_dict):
    dia, mes, ano = date_dict['dia'], date_dict['mes'], date_dict['ano']
    hora, minuto = date_dict['hora'], date_dict['minuto']
    date_str = '-'.join(list(map(lambda x: str(x), [ano,mes,dia])))
    time_str = ':'.join(list(map(lambda x: str(x), [hora, minuto])))
    return dt.datetime.strptime(date_str + ' ' + time_str, "%Y-%m-%d %H:%M")

def get_data_from_endpoint(endpoint_name, *kwargs):
    url = _get_endpoint(endpoint_name, *kwargs)
    r = requests.get(url)
    print("Sucessfull request to %s returned status %s" % (url, r.status_code))
    data = json.loads(r.text)
    return data

def get_market_info():
    mercado = get_data_from_endpoint('mercado')
    mercado['data_fechamento'] = _get_dict_into_date(mercado['fechamento'])
    return fp.merge(mercado, {'data_fechamento': _get_dict_into_date(mercado['fechamento'])})

def get_player_info():
    return get_data_from_endpoint('atletas_mercado')['atletas']

def get_matches_info(rodada):
    return get_data_from_endpoint('partidas', rodada)['partidas']

def get_teams_info():
    return get_data_from_endpoint('clubes').values

def get_match_week_info(rodada):
    market = get_market_info()

    print("Rodada %s fechara as %s" % (market['rodada_atual'], market['data_fechamento']))


    players = map(map_cartola_to_players, get_player_info())
    scouts = map(map_cartola_to_scouts, get_player_info())
    matches = map(map_cartola_to_matches(rodada=rodada), get_matches_info(rodada=rodada))
    teams = map(map_cartola_to_teams, get_teams_info())

def insert_or_update(obj):

def map_cartola_to_scouts(player):
    return Scout(player_id = player['atleta_id'],
          team_id = player['clube_id'],
          match_week = player['rodada_id'],
          has_played = False,
          points = player['pontos_num'],
          average_points = player['media_num'],
          price = player['preco_num'],
          delta_price = player['variacao_num'],
          plays = [],
          year = '2018')

def map_cartola_to_players(player):
    return Player(id=player['atleta_id'],
        name=player['apelido'],
        player_id = player['atleta_id'],
        team_id = player['clube_id'],
        position_id = player['posicao_id'],
        year = 2018)

@fp.curry
def map_cartola_to_matches(match, rodada):
    return Match(id=match['partida_id'],
                 match_week=rodada,
                 home_team_id=match['clube_casa_id'],
                 visiting_team_id=match['clube_visitante_id'],
                 home_score=match['placar_oficial_mandante'],
                 visiting_score=match['placar_oficial_visitante'],
                 result=match['clube_casa_id'],
                 year=match['clube_casa_id'])

def map_cartola_to_teams(team):
    return Team(id=team['id'],
        name=team['nome'],
        nickname=team['abreviacao'],
        year=2018)
