from models.features import Features
from connectors.postgree import PostGreConnectorSQL
import pandas



# NEW FEATURES:
# -- Casa ou Visitante (FACIL)
# -- Colocacao no Campeonato (MEDIO)
# -- Posse de Bola (DIFICIL)
# -- Average Price (FACIL)
# -- Has played? ignorar jogadores que nao jogaram (FACIL)
# -- Posicao? Usar como feature ou para dividir o treinamento do dataset
# -- CleanSheets (Média)
# -- Gols feitos e tomados pelo time adversario
# -- Desempenho em casa e fora do time adversario
class FeatureQueries:


    def __init__(self):
        self.pg = PostGreConnectorSQL()

    def average_points(self, scout_id, n_rounds):
        if self.__get_scout_match_week(scout_id) < n_rounds:
            return None
        feature_name = 'average_points_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/average_points.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        if df.shape[0] == 0:
            return None
        return df['feature_value'][0]

    def average_plays(self, scout_id, n_rounds, play_type):
        if self.__get_scout_match_week(scout_id) < n_rounds:
            return None
        feature_name = 'average_plays_last_' + str(n_rounds) + '_rounds_' + str(play_type) + '_play'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/average_plays.sql')
        query_file = query_file.read()
        feature_query = query_file.format(play_type, n_rounds, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        if df.shape[0] == 0:
            return None
        return df['feature_value'][0]

    def team_goals_scored(self, scout_id, n_rounds):
        if self.__get_scout_match_week(scout_id) < n_rounds:
            return None
        feature_name = 'team_goals_scored_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/team_goals_scored.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        if df.shape[0] == 0:
            return None
        return df['feature_value'][0]

    def team_goals_taken(self, scout_id, n_rounds):
        if self.__get_scout_match_week(scout_id) < n_rounds:
            return None
        feature_name = 'team_goals_taken_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/team_goals_taken.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        if df.shape[0] == 0:
            return None
        return df['feature_value'][0]


    def team_points(self, scout_id, n_rounds):
        if self.__get_scout_match_week(scout_id) < n_rounds:
            return None
        feature_name = 'team_points_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/team_points.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        if df.shape[0] == 0:
            return None
        return df['feature_value'][0]

    def __get_scout_match_week(self, scout_id):
        query_file = open('queries/scout.sql')
        query_file = query_file.read()
        feature_query = query_file.format(scout_id)
        df = self.pg.execute_query(feature_query)
        if df.shape[0] == 0:
            return None
        return df['match_week'][0]


