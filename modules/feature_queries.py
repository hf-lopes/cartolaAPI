from models.features import Features
from connectors.postgree import PostGreConnectorSQL
import pandas as pd
from constants import abreviacao
from constants import pontuacao, points_dict
# TODO: Casa ou Visitante pegando rodada errada, pegar a proxima rodada
# TODO: Cleanshets usando count
# TODO: Separar desempenho dos times entre casa e fora
# TODO: Verificar dados has played
# NEW FEATURES:
# -- Colocacao no Campeonato (MEDIO)
# -- Posse de Bola (DIFICIL)

class FeatureQueries:


    def __init__(self, scout_id):
        self.pg = PostGreConnectorSQL()
        self.basic_info = self.get_scout_match_week(scout_id)

    def average_points(self, scout_id, n_rounds):
        feature_name = 'average_points_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/average_points.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)
        return df[feature_name]


    def average_price(self, scout_id, n_rounds):
        feature_name = 'average_price_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/average_price.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]

    def stddev_points(self, scout_id, n_rounds):
        feature_name = 'stddev_points_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/stddev_points.sql')
        query_file = query_file.read()
        feature_query = query_file.format(feature_name, scout_id, n_rounds, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)
        return df[feature_name]


    def stddev_price(self, scout_id, n_rounds):
        feature_name = 'stddev_price_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/stddev_price.sql')
        query_file = query_file.read()
        feature_query = query_file.format(feature_name, scout_id, n_rounds, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]

    def team_average_points(self, scout_id, n_rounds):
        feature_name = 'team_average_points_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/team_average_points.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)
        return df[feature_name]


    def team_average_price(self, scout_id, n_rounds):
        feature_name = 'team_average_price_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/team_average_price.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]

    def team_stddev_points(self, scout_id, n_rounds):
        feature_name = 'team_stddev_points_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/team_stddev_points.sql')
        query_file = query_file.read()
        feature_query = query_file.format(feature_name, scout_id, n_rounds, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)
        return df[feature_name]


    def team_stddev_price(self, scout_id, n_rounds):
        feature_name = 'team_stddev_price_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/team_stddev_price.sql')
        query_file = query_file.read()
        feature_query = query_file.format(feature_name, scout_id, n_rounds, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]

    def enemy_average_points(self, scout_id, n_rounds):
        feature_name = 'enemy_average_points_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/enemy_average_points.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)
        return df[feature_name]


    def enemy_average_price(self, scout_id, n_rounds):
        feature_name = 'enemy_average_price_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/enemy_average_price.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]

    def enemy_stddev_points(self, scout_id, n_rounds):
        feature_name = 'enemy_stddev_points_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/enemy_stddev_points.sql')
        query_file = query_file.read()
        feature_query = query_file.format(feature_name, scout_id, n_rounds, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)
        return df[feature_name]


    def enemy_stddev_price(self, scout_id, n_rounds):
        feature_name = 'enemy_stddev_price_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/enemy_stddev_price.sql')
        query_file = query_file.read()
        feature_query = query_file.format(feature_name, scout_id, n_rounds, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]


    def average_plays(self, scout_id, n_rounds, play_type):
        feature_name = 'average_plays_last_' + str(n_rounds) + '_rounds_' + abreviacao[play_type - 1].lower() + '_play'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/average_plays.sql')
        query_file = query_file.read()
        feature_query = query_file.format(play_type, n_rounds, feature_name, scout_id, n_rounds, n_rounds)
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

    def team_goals_scored_home(self, scout_id, n_rounds):
        feature_name = 'team_goals_scored_home_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/team_goals_scored_home.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]

    def team_goals_taken_home(self, scout_id, n_rounds):
        feature_name = 'team_goals_taken_home_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/team_goals_taken_home.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]


    def team_points_home(self, scout_id, n_rounds):
        feature_name = 'team_points_home_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/team_points_home.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]

    def team_goals_scored_away(self, scout_id, n_rounds):
        feature_name = 'team_goals_scored_away_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/team_goals_scored_away.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]

    def team_goals_taken_away(self, scout_id, n_rounds):
        feature_name = 'team_goals_taken_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/team_goals_taken.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]

    def team_points_away(self, scout_id, n_rounds):
        feature_name = 'team_points_away_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/team_points_away.sql')
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

    def enemy_goals_scored_home(self, scout_id, n_rounds):
        feature_name = 'enemy_goals_scored_home_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/enemy_goals_scored_home.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]


    def enemy_goals_taken_home(self, scout_id, n_rounds):
        feature_name = 'enemy_goals_taken_home_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/enemy_goals_taken_home.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]


    def enemy_points_home(self, scout_id, n_rounds):
        feature_name = 'enemy_points_home_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/enemy_points_home.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]

    def enemy_goals_scored_away(self, scout_id, n_rounds):
        feature_name = 'enemy_goals_scored_away_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/enemy_goals_scored_away.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]


    def enemy_goals_taken_away(self, scout_id, n_rounds):
        feature_name = 'enemy_goals_taken_away_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/enemy_goals_taken_away.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds,feature_name, scout_id, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]


    def enemy_points_away(self, scout_id, n_rounds):
        feature_name = 'enemy_points_away_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/enemy_points_away.sql')
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

    def average_plays_team(self, scout_id, n_rounds, play_type):
        feature_name = 'average_plays_team_last_' + str(n_rounds) + '_rounds_' + abreviacao[play_type - 1].lower() + '_play'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/average_plays_team.sql')
        query_file = query_file.read()
        feature_query = query_file.format(play_type, n_rounds, feature_name, scout_id, n_rounds, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]

    def average_plays_enemy_team(self, scout_id, n_rounds, play_type):
        feature_name = 'average_plays_enemy_team_last_' + str(n_rounds) + '_rounds_' + abreviacao[play_type - 1].lower() + '_play'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/average_plays_enemy_team.sql')
        query_file = query_file.read()
        feature_query = query_file.format(play_type, n_rounds, feature_name, scout_id, n_rounds, n_rounds)
        df = self.pg.execute_query(feature_query)
        df.set_index('scout_id', inplace=True)

        return df[feature_name]

    def team_points_enemy_points_ratio(self, scout_id, n_rounds):
        feature_name = "team_points_enemy_points_ratio_last_" + str(n_rounds) + '_rounds'
        df_enemy = self.enemy_points(scout_id=scout_id, n_rounds=n_rounds)
        df_team = self.team_points(scout_id=scout_id, n_rounds=n_rounds)
        df_team[feature_name] = df_team * df_enemy
        return df_team[feature_name]

    def team_goals_scored_enemy_goals_taken_ratio(self, scout_id, n_rounds):
        feature_name = "team_goals_scored_enemy_goals_taken_ratio_last_" + str(n_rounds) + '_rounds'
        df_enemy = self.enemy_goals_taken(scout_id=scout_id, n_rounds=n_rounds)
        df_team = self.team_goals_scored(scout_id=scout_id, n_rounds=n_rounds)
        df_team[feature_name] = df_team * df_enemy
        return df_team[feature_name]

    def team_goals_taken_enemy_goals_scored_ratio(self, scout_id, n_rounds):
        feature_name = "team_goals_taken_enemy_goals_scored_ratio_last_" + str(n_rounds) + '_rounds'
        df_enemy = self.enemy_goals_scored(scout_id=scout_id, n_rounds=n_rounds)
        df_team = self.team_goals_taken(scout_id=scout_id, n_rounds=n_rounds)
        df_team[feature_name] = df_team * df_enemy
        return df_team[feature_name]

    def team_goals_taken_enemy_goals_scored_ratio_home_away(self, scout_id, n_rounds):
        feature_name = "team_goals_taken_enemy_goals_scored_ratio_home_away_last" + str(n_rounds) + '_rounds'
        df_enemy_away = self.enemy_goals_scored_away(scout_id=scout_id, n_rounds=n_rounds)
        df_team_away = self.team_goals_taken_away(scout_id=scout_id, n_rounds=n_rounds)

        df_enemy_home = self.enemy_goals_scored_home(scout_id=scout_id, n_rounds=n_rounds)
        df_team_home = self.team_goals_taken_home(scout_id=scout_id, n_rounds=n_rounds)

        df_team_home = df_team_home.loc[df_enemy_away.index]

        df_team_home[feature_name] = df_team_home * df_enemy_away

        df_team_away = df_team_away.loc[df_enemy_home.index]

        df_team_away[feature_name] = df_team_away * df_enemy_home

        final_df = pd.concat([df_team_home[feature_name], df_team_away[feature_name]], axis=0)
        return final_df

    def team_goals_scored_enemy_goals_taken_ratio_home_away(self, scout_id, n_rounds):
        feature_name = "team_goals_scored_enemy_goals_taken_ratio_home_away_last_" + str(n_rounds) + '_rounds'
        df_enemy_away = self.enemy_goals_taken_away(scout_id=scout_id, n_rounds=n_rounds)
        df_team_away = self.team_goals_scored_away(scout_id=scout_id, n_rounds=n_rounds)

        df_enemy_home = self.enemy_goals_taken_home(scout_id=scout_id, n_rounds=n_rounds)
        df_team_home = self.team_goals_scored_home(scout_id=scout_id, n_rounds=n_rounds)


        df_team_home = df_team_home.loc[df_enemy_away.index]

        df_team_home[feature_name] = df_team_home * df_enemy_away

        df_team_away = df_team_away.loc[df_enemy_home.index]

        df_team_away[feature_name] = df_team_away * df_enemy_home

        final_df = pd.concat([df_team_home[feature_name], df_team_away[feature_name]], axis=0)
        return final_df


    def team_price_enemy_price_ratio(self, scout_id, n_rounds):
        feature_name = "team_price_enemy_price_ratio_last_" + str(n_rounds) + '_rounds'
        df_enemy = self.enemy_average_price(scout_id=scout_id, n_rounds=n_rounds)
        df_team = self.team_average_price(scout_id=scout_id, n_rounds=n_rounds)
        df_team[feature_name] = df_team / df_enemy
        return df_team[feature_name]

    def team_points_enemy_player_points_ratio(self, scout_id, n_rounds):
        feature_name = "team_points_enemy_player_points_ratio_last_" + str(n_rounds) + '_rounds'
        df_enemy = self.enemy_average_points(scout_id=scout_id, n_rounds=n_rounds)
        df_team = self.team_average_points(scout_id=scout_id, n_rounds=n_rounds)
        df_team[feature_name] = df_team / df_enemy
        return df_team[feature_name]

    def num_std_dev_team_points_enemy_points(self, scout_id, n_rounds):
        feature_name = "num_std_dev_team_points_enemy_points_last_" + str(n_rounds) + '_rounds'
        df_enemy = self.enemy_average_points(scout_id=scout_id, n_rounds=n_rounds)
        df_team = self.team_average_points(scout_id=scout_id, n_rounds=n_rounds)
        df_stddev = self.team_stddev_points(scout_id=scout_id, n_rounds=n_rounds)
        df_team[feature_name] = (df_team - df_enemy) / df_stddev
        return df_team[feature_name]

    def team_points_enemy_points_ratio_home_away(self, scout_id, n_rounds):
        feature_name = "team_points_enemy_points_ratio_home_away_last_" + str(n_rounds) + '_rounds'
        df_enemy_away = self.enemy_points_away(scout_id=scout_id, n_rounds=n_rounds)
        df_team_away = self.team_points_away(scout_id=scout_id, n_rounds=n_rounds)

        df_enemy_home = self.enemy_points_home(scout_id=scout_id, n_rounds=n_rounds)
        df_team_home = self.team_points_home(scout_id=scout_id, n_rounds=n_rounds)


        df_team_home = df_team_home.loc[df_enemy_away.index]

        df_team_home[feature_name] = df_team_home * df_enemy_away

        df_team_away = df_team_away.loc[df_enemy_home.index]

        df_team_away[feature_name] = df_team_away * df_enemy_home

        final_df = pd.concat([df_team_home[feature_name], df_team_away[feature_name]], axis=0)
        return final_df


    def player_goal_participation(self, scout_id, n_rounds):
        feature_name = "player_goal_participation_last_" + str(n_rounds) + '_rounds'
        df_goals = self.average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('G')) * points_dict['G']
        df_assists = self.average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('A')) * points_dict['A']
        df_ft = self.average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FT')) * points_dict['FT']
        df_ff = self.average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FF')) * points_dict['FF']
        df_fd = self.average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FD')) * points_dict['FD']

        df_points = df_goals + df_assists + df_ft + df_ff + df_fd

        df_enemy = self.enemy_goals_taken(scout_id=scout_id, n_rounds=n_rounds)
        df_team = self.team_goals_scored(scout_id=scout_id, n_rounds=n_rounds)


        df_team[feature_name] = (df_points * df_team * df_enemy)
        return df_team[feature_name]

    def clean_sheet_chance(self, scout_id, n_rounds):
        feature_name = "player_goal_participation_last_" + str(n_rounds) + '_rounds'

        ## TODO: find team goalkeepers avgs to input here
        ## TODO: only calculate this for defenders
        df_sg = self.average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('SG')) * points_dict['SG']

        df_points = df_sg

        df_enemy = self.enemy_goals_scored(scout_id=scout_id, n_rounds=n_rounds)
        df_team = self.team_goals_taken(scout_id=scout_id, n_rounds=n_rounds)


        df_team[feature_name] = df_points / (df_team * df_enemy)
        return df_team[feature_name]

    def player_goal_participation_team_ratio(self, scout_id, n_rounds):
        feature_name = "player_goal_participation_team_ratio_last_" + str(n_rounds) + '_rounds'
        df_goals = self.average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('G')) * points_dict['G']
        df_assists = self.average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('A')) * points_dict['A']
        df_ft = self.average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FT')) * points_dict['FT']
        df_ff = self.average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FF')) * points_dict['FF']
        df_fd = self.average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FD')) * points_dict['FD']


        df_goals_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('G')) * points_dict['G']
        df_assists_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('A')) * points_dict['A']
        df_ft_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FT')) * points_dict['FT']
        df_ff_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FF')) * points_dict['FF']
        df_fd_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FD')) * points_dict['FD']

        df_points = df_goals + df_assists + df_ft + df_ff + df_fd

        df_points_team = df_goals_team + df_assists_team + df_ft_team + df_ff_team + df_fd_team


        df_points[feature_name] = (df_points / df_points_team)
        return df_points[feature_name]

    def team_offense_enemy_defense(self, scout_id, n_rounds):
        feature_name = "team_offense_enemy_defense_last_" + str(n_rounds) + '_rounds'

        df_goals_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('G')) * points_dict['G']
        df_assists_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('A')) * points_dict['A']
        df_ft_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FT')) * points_dict['FT']
        df_ff_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FF')) * points_dict['FF']
        df_fd_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FD')) * points_dict['FD']
        df_i_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('I')) * points_dict['I']
        df_pp_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('PP')) * points_dict['PP']

        df_rb_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('RB')) * points_dict['RB']
        df_sg_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('SG')) * points_dict['SG']
        df_dd_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('DD')) * points_dict['DD']
        df_dp_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('DP')) * points_dict['DP']


        df_points_team = df_goals_team + df_assists_team + df_ft_team + df_ff_team + df_fd_team + df_i_team + df_pp_team


        df_points_enemy = df_rb_enemy + df_sg_enemy + df_dd_enemy + df_dp_enemy

        df_points_team[feature_name] = (df_points_team / df_points_enemy)
        return df_points_team[feature_name]

    def team_defense_enemy_offense(self, scout_id, n_rounds):
        feature_name = "team_defense_enemy_offense_last_" + str(n_rounds) + '_rounds'

        df_goals_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('G')) * points_dict['G']
        df_assists_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('A')) * points_dict['A']
        df_ft_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FT')) * points_dict['FT']
        df_ff_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FF')) * points_dict['FF']
        df_fd_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FD')) * points_dict['FD']
        df_i_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('I')) * points_dict['I']
        df_pp_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('PP')) * points_dict['PP']

        df_rb_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('RB')) * points_dict['RB']
        df_sg_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('SG')) * points_dict['SG']
        df_dd_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('DD')) * points_dict['DD']
        df_dp_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('DP')) * points_dict['DP']


        df_points_enemy = df_goals_enemy + df_assists_enemy + df_ft_enemy + df_ff_enemy + df_fd_enemy + df_i_enemy + df_pp_enemy


        df_points_team = df_rb_team + df_sg_team + df_dd_team + df_dp_team

        df_points_team[feature_name] = (df_points_team / df_points_enemy)
        return df_points_team[feature_name]

    def team_defense_enemy_goals(self, scout_id, n_rounds):
        feature_name = "team_defense_enemy_goals_last_" + str(n_rounds) + '_rounds'

        df_rb_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('RB')) * points_dict['RB']
        df_sg_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('SG')) * points_dict['SG']
        df_dd_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('DD')) * points_dict['DD']
        df_dp_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('DP')) * points_dict['DP']

        df_points_team = df_rb_team + df_sg_team + df_dd_team + df_dp_team

        df_enemy = self.enemy_goals_scored(scout_id=scout_id, n_rounds=n_rounds)
        df_team = self.team_goals_taken(scout_id=scout_id, n_rounds=n_rounds)

        df_team[feature_name] = df_points_team / (df_team * df_enemy)
        return df_team[feature_name]

    def team_rb_enemy_pe(self, scout_id, n_rounds):
        feature_name = "team_rb_enemy_pe_last_" + str(n_rounds) + '_rounds'

        df_pe_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('PE')) * points_dict['PE']

        df_rb_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('RB')) * points_dict['RB']

        df_rb_player = self.average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('RB')) * points_dict['RB']

        df_rb_team[feature_name] = (df_rb_team * df_rb_player * df_pe_enemy)
        return df_rb_team[feature_name]

    def player_pe_enemy_rb(self, scout_id, n_rounds):
        feature_name = "team_rb_enemy_pe_last_" + str(n_rounds) + '_rounds'

        df_rb_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('RB')) * points_dict['RB']

        df_pe_player = self.average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('PE')) * points_dict['PE']

        df_pe_player[feature_name] = (df_pe_player * df_rb_enemy)
        return df_pe_player[feature_name]

    def player_fs_enemy_fc(self, scout_id, n_rounds):
        feature_name = "team_rb_enemy_pe_last_" + str(n_rounds) + '_rounds'

        df_fc_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('FC')) * points_dict['FC']

        df_fs_player = self.average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('FS')) * points_dict['FS']

        df_fs_player[feature_name] = (df_fs_player * df_fc_enemy)
        return df_fs_player[feature_name]

    def enemy_fs_player_fc_ca_cv(self, scout_id, n_rounds):
        feature_name = "team_rb_enemy_pe_last_" + str(n_rounds) + '_rounds'

        df_fs_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('FS')) * points_dict['FS']

        df_fc_player = self.average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('FC')) * points_dict['FC']
        df_ca_player = self.average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('CA')) * points_dict['CA']
        df_cv_player = self.average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('CV')) * points_dict['CV']

        df_bad = df_fc_player + df_ca_player + df_cv_player
        df_bad[feature_name] = (df_bad * df_fs_enemy)
        return df_bad[feature_name]

    def team_offense_enemy_fauls(self, scout_id, n_rounds):
        feature_name = "team_offense_enemy_fauls_last_" + str(n_rounds) + '_rounds'


        df_goals_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('G')) * points_dict['G']
        df_assists_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('A')) * points_dict['A']
        df_ft_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FT')) * points_dict['FT']
        df_ff_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FF')) * points_dict['FF']
        df_fd_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FD')) * points_dict['FD']
        df_i_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('I')) * points_dict['I']
        df_pp_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('PP')) * points_dict['PP']

        df_fc_player = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('FC')) * points_dict['FC']
        df_ca_player = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('CA')) * points_dict['CA']
        df_cv_player = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('CV')) * points_dict['CV']

        df_points_team = df_goals_team + df_assists_team + df_ft_team + df_ff_team + df_fd_team + df_i_team + df_pp_team

        df_bad = df_fc_player + df_ca_player + df_cv_player
        df_points_team[feature_name] = (df_bad * df_points_team)
        return df_points_team[feature_name]

    def team_fauls_enemy_offense(self, scout_id, n_rounds):
        feature_name = "team_fauls_enemy_offense_last_" + str(n_rounds) + '_rounds'


        df_goals_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('G')) * points_dict['G']
        df_assists_enemy= self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('A')) * points_dict['A']
        df_ft_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FT')) * points_dict['FT']
        df_ff_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FF')) * points_dict['FF']
        df_fd_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FD')) * points_dict['FD']
        df_i_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('I')) * points_dict['I']
        df_pp_enemy = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('PP')) * points_dict['PP']

        df_fc_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('FC')) * points_dict['FC']
        df_ca_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('CA')) * points_dict['CA']
        df_cv_team = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('CV')) * points_dict['CV']

        df_points_enemy = df_goals_enemy + df_assists_enemy + df_ft_enemy + df_ff_enemy + df_fd_enemy + df_i_enemy + df_pp_enemy

        df_bad = df_fc_team + df_ca_team + df_cv_team
        df_points_enemy[feature_name] = (df_bad * df_points_enemy)
        return df_points_enemy[feature_name]


    def team_goal_chance(self, scout_id, n_rounds):
        feature_name = "team_goal_chance_last_" + str(n_rounds) + '_rounds'
        df_goals = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('G')) * points_dict['G']
        df_assists = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('A')) * points_dict['A']
        df_ft = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FT')) * points_dict['FT']
        df_ff = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FF')) * points_dict['FF']
        df_fd = self.average_plays_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FD')) * points_dict['FD']

        df_points = df_goals + df_assists + df_ft + df_ff + df_fd

        df_enemy = self.enemy_goals_taken(scout_id=scout_id, n_rounds=n_rounds)
        df_team = self.team_goals_scored(scout_id=scout_id, n_rounds=n_rounds)


        df_team[feature_name] = (df_points * df_team * df_enemy)
        return df_team[feature_name]

    def enemy_goal_chance(self, scout_id, n_rounds):
        feature_name = "enemy_goal_chance_last_" + str(n_rounds) + '_rounds'
        df_goals = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type=abreviacao.index('G')) * points_dict['G']
        df_assists = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('A')) * points_dict['A']
        df_ft = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FT')) * points_dict['FT']
        df_ff = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FF')) * points_dict['FF']
        df_fd = self.average_plays_enemy_team(scout_id=scout_id, n_rounds=n_rounds, play_type = abreviacao.index('FD')) * points_dict['FD']

        df_points = df_goals + df_assists + df_ft + df_ff + df_fd

        df_enemy = self.enemy_goals_scored(scout_id=scout_id, n_rounds=n_rounds)
        df_team = self.team_goals_taken(scout_id=scout_id, n_rounds=n_rounds)


        df_team[feature_name] = (df_points * df_team * df_enemy)
        return df_team[feature_name]

    def get_basic_info(self):
        return self.basic_info


