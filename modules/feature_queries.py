from models.features import Features


class FeatureQueries:

    def average_points(self, scout_id, n_rounds):
        feature_name = 'average_points_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/average_points.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds, scout_id, n_rounds)
        feature = Features(name=feature_name, feature_query=feature_query)
        return feature

    def average_plays(self, scout_id, n_rounds, play_type):
        feature_name = 'average_plays_last_' + str(n_rounds) + '_rounds_' + str(play_type) + '_play'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/average_plays.sql')
        query_file = query_file.read()
        feature_query = query_file.format(play_type, n_rounds, scout_id, n_rounds)
        feature = Features(name=feature_name, feature_query=feature_query)
        return feature

    def team_goals_scored(self, scout_id, n_rounds):
        feature_name = 'team_goals_scored_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/team_goals_scored.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds, scout_id, n_rounds)
        feature = Features(name=feature_name, feature_query=feature_query)
        return feature

    def team_goals_taken(self, scout_id, n_rounds):
        feature_name = 'team_goals_taken_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/team_goals_taken.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds, scout_id, n_rounds)
        feature = Features(name=feature_name, feature_query=feature_query)
        return feature


    def team_points(self, scout_id, n_rounds):
        feature_name = 'team_points_last_' + str(n_rounds) + '_rounds'
        # print('Calculating feature %s' % feature_name)
        query_file = open('queries/team_points.sql')
        query_file = query_file.read()
        feature_query = query_file.format(n_rounds, scout_id, n_rounds)
        feature = Features(name=feature_name, feature_query=feature_query)
        return feature

