from connectors.postgree import PostGreConnectorSQL
from modules.feature_queries import FeatureQueries
from constants import NUM_PARALLEL_CONNECTIONS
import threading
import time
import math


class FeatureCalculator:

    def __init__(self):
        self.scouts = []

    def generate_feature_queries(self, init_id, last_id):
        scout_features = []
        for scout_id in range(init_id, last_id):
            start_time = time.time()
            feature_list = []
            for n_rounds in range(1, 38, 3):
                feature_list.append(FeatureQueries().average_points(scout_id=scout_id, n_rounds=n_rounds))

                feature_list.append(FeatureQueries().team_points(scout_id=scout_id, n_rounds=n_rounds))

                feature_list.append(FeatureQueries().team_goals_scored(scout_id=scout_id, n_rounds=n_rounds))

                feature_list.append(FeatureQueries().team_goals_taken(scout_id=scout_id, n_rounds=n_rounds))

                for n_plays in range(1, 19):
                    feature_list.append(
                        FeatureQueries().average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type=n_plays))
            print('Calculated %s features, took %s, %s completed' % (len(feature_list),
                                                                     "{0:.2}s".format(time.time() - start_time),
                                                                     str((scout_id - init_id) * 100 / (last_id - init_id)) + '%'))
            scout_features.append(feature_list)
        print('Generated queries for %s scouts' % str(len(scout_features)))
        return scout_features

    def calculate_features(self, query_list):
        feature_list = []
        pg = PostGreConnectorSQL()
        print('Starting query %s' % len(query_list))
        for index, feature in enumerate(query_list):
            df = pg.execute_query(feature.feature_query)
            # print('Query executed, %s %% completed' % str(index * 100 / len(query_list)))
            feature_list.append(df['feature_value'][0])
            # print(feature.name, df['feature_value'][0])

        return feature_list

    def calculate_list_features(self, scout_list):
        for index, scouts in enumerate(scout_list):
            start_time = time.time()
            print('***************\n'
                  '%s %% of scouts calculated, took %s\n'
                  '***********************' % (str(index*100/len(scout_list)), "{0:.2}s".format(time.time() - start_time)))
            self.scouts.append(self.calculate_features(scouts))

    def parallel_calculation(self, scout_list):
        l = len(scout_list)
        print('Initializing Threads')
        for i in range(NUM_PARALLEL_CONNECTIONS):
            print(0 + i * math.floor(l / NUM_PARALLEL_CONNECTIONS),
                  min(l + 1, int((i + 1) * math.floor(l / NUM_PARALLEL_CONNECTIONS))))
            t = threading.Thread(name='t' + str(i),
                                 target=self.calculate_list_features,
                                 args=(scout_list[0 + i * math.floor(l / NUM_PARALLEL_CONNECTIONS):
                                        min(l + 1, int((i + 1) * math.floor(l / NUM_PARALLEL_CONNECTIONS)))],)
                                 )
            t.start()
            print('Thread %s Running' % t.name)
        t.join()

    def get_scout_list(self):
        return self.scouts