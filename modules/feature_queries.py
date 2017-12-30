from models.features import Features
from connectors.postgree import PostGreConnectorSQL
import pandas
from constants import abreviacao


# NEW FEATURES:
# -- Casa ou Visitante (FACIL) -- DONE
# -- Colocacao no Campeonato (MEDIO)
# -- Posse de Bola (DIFICIL)
# -- Average Price (FACIL) -- DONE
# -- Has played? ignorar jogadores que nao jogaram (FACIL)
# -- Posicao? Usar como feature ou para dividir o treinamento do dataset
# -- CleanSheets (Média)
# -- Gols feitos e tomados pelo time adversario -- DONE
# -- Desempenho em casa e fora do time adversario -- DONE

class FeatureQueries:


    def __init__(self, scout_id):
        self.pg = PostGreConnectorSQL()
        self.basic_info = self.get_scout_match_week(scout_id)

    def average_points(self, scout_id, n_rounds):
        feature_name = 'average_points_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/average_points.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)
        return df[feature_name]


    def average_price(self, scout_id, n_rounds):
        feature_name = 'average_price_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/average_price.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]

    def average_plays(self, scout_id, n_rounds, play_type):
        feature_name = 'average_plays_last_' + str(n_rounds) + '_rounds_' + abreviacao[play_type].lower() + '_play'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/average_plays.sql')
        query_file = query_file.read()
        feature_query = query_file.format(play_type, n_rounds, feature_name, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]

    def team_goals_scored(self, scout_id, n_rounds):
        feature_name = 'team_goals_scored_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/team_goals_scored.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]

    def team_goals_taken(self, scout_id, n_rounds):
        feature_name = 'team_goals_taken_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/team_goals_taken.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]


    def team_points(self, scout_id, n_rounds):
        feature_name = 'team_points_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/team_points.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]





    def enemy_goals_scored(self, scout_id, n_rounds):
        feature_name = 'enemy_goals_scored_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/enemy_goals_scored.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]


    def enemy_goals_taken(self, scout_id, n_rounds):
        feature_name = 'enemy_goals_taken_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/enemy_goals_taken.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]


    def enemy_points(self, scout_id, n_rounds):
        feature_name = 'enemy_points_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/enemy_points.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]


    def get_scout_match_week(self, scout_id):
        query_file = open('queries/scout.sql')
        query_file = query_file.read()
        feature_query = query_file.format(scout_id)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df

    def home_away(self, scout_id):
        feature_name = 'home_team'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/home_away.sql')
        query_file = query_file.read()
        feature_query = query_file.format(feature_name, scout_id)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)
        return df[feature_name]

    def get_basic_info(self):
        return self.basic_info


