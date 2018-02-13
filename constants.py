import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

abreviacao = ['RB', 'FC', 'GC', 'CA', 'CV', 'SG', 'DD', 'DP', 'GS',
              'FS', 'PE', 'A', 'FT', 'FD', 'FF', 'G', 'I', 'PP']
descricao = ['Robadas de Bola', 'Faltas Cometidas', 'Gol Contra', 'Cartao Amarelo',
             'Cartao Vermelho', 'Jogo sem sofrer gol', 'Defesa Dificil', 'Defesa de Penalti',
             'Gol Sofrido', 'Falta Sofrida', 'Passe Errado', 'Assistencia',
             'Finalizacao na Trave', 'Finalizacao defendida', 'Finalizao pra Fora', 'Gol',
             'Impedimento', 'Penalti Perdido']
pontuacao = [1.7, -0.5, -6.0, -2.0, -5.0, 5.0, 3.00, 7.00, -2.0,
             0.5, -0.3, 5.0, 3.5, 1.0, 0.7, 8.0, -0.5, -3.5]

points_dict = {
    "RB": 1.7,
    "FC": -0.5,
    "GC": -6.0,
    "CA": -2.0,
    "CV": -5.0,
    "SG": 5.0,
    "DD": 3.0,
    "DP": 7.0,
    "GS": -2.0,
    "FS": 0.5,
    "PE": -0.3,
    "A": 5.0,
    "FT": 3.5,
    "FD": 1.0,
    "FF": 0.7,
    "G": 8.0,
    "I": -0.5,
    "PP": -3.5,
}
pg_user = 'hlopes'
pg_pswd = 'lopes_146'
pg_db = 'cartoladb'
pg_url = 'pg-cartola.c3pssepl8cax.us-east-2.rds.amazonaws.com'
pg_port = '5432'


## https://github.com/wgenial/cartrolandofc/blob/master/nova-api.md
## Endpoints da API do Cartola

cartola_endpoint = dict()
cartola_endpoint['mercado'] = 'https://api.cartolafc.globo.com/mercado/status'
cartola_endpoint['escalados_destaques'] = 'https://api.cartolafc.globo.com/mercado/destaques'
cartola_endpoint['patrocinadores'] = 'https://api.cartolafc.globo.com/patrocinadores'
cartola_endpoint['rodadas'] = 'https://api.cartolafc.globo.com/rodadas'
cartola_endpoint['partidas'] = 'https://api.cartolafc.globo.com/partidas'
cartola_endpoint['partidas_rodada'] = 'https://api.cartolafc.globo.com/partidas/[rodada]'
cartola_endpoint['clubes'] = 'https://api.cartolafc.globo.com/clubes'
cartola_endpoint['atletas_mercado'] = 'https://api.cartolafc.globo.com/atletas/mercado'
cartola_endpoint['atletas_pontuados'] = 'https://api.cartolafc.globo.com/atletas/pontuados'
cartola_endpoint['pontos_destaques'] = 'https://api.cartolafc.globo.com/pos-rodada/destaques'
cartola_endpoint['times'] = 'https://api.cartolafc.globo.com/times' # ?q=[nome do time]
cartola_endpoint['time_slug'] = 'https://api.cartolafc.globo.com/time/slug' # /[slug do time] # /[slug do time]/[rodada]
cartola_endpoint['ligas'] = 'https://api.cartolafc.globo.com/ligas' # ?q=[nome da liga]
cartola_endpoint['liga_usuario'] = 'https://api.cartolafc.globo.com/auth/liga' # /[slug da liga]
cartola_endpoint['time_usuario'] = 'https://api.cartolafc.globo.com/auth/time'
cartola_endpoint['time_usuario_info'] = 'https://api.cartolafc.globo.com/auth/time/info'
cartola_endpoint['ligas_usuario'] = 'https://api.cartolafc.globo.com/auth/ligas'
cartola_endpoint['esquemas'] = 'https://api.cartolafc.globo.com/esquemas'
cartola_endpoint['time_post'] = 'https://api.cartolafc.globo.com/auth/time/salvar'

NUM_PARALLEL_CONNECTIONS = 10