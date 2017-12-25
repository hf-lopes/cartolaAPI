from connectors.postgree import PostGreConnectorSQL, PostGreConnector
from modules.feature_queries import FeatureQueries
from models.Descriptors import Descriptors
from constants import NUM_PARALLEL_CONNECTIONS
import threading
import time
import math
import random


class FeatureCalculator:

    def __init__(self):
        self.descriptor_list = []
        self.pg = PostGreConnector()


    def generate_feature_queries(self, init_id, last_id, hash):
        fq = FeatureQueries()
        start_fetch = time.time()
        print('Starting calculation of %s scouts' % str(last_id - init_id))
        for scout_id in range(init_id, last_id):
            start_time = time.time()
            feature_list = []
            for n_rounds in range(1, 38, 5):
                feature_list.append(fq.average_points(scout_id=scout_id, n_rounds=n_rounds))

                feature_list.append(fq.team_points(scout_id=scout_id, n_rounds=n_rounds))

                feature_list.append(fq.team_goals_scored(scout_id=scout_id, n_rounds=n_rounds))

                feature_list.append(fq.team_goals_taken(scout_id=scout_id, n_rounds=n_rounds))

                for n_plays in range(1, 19):
                    feature_list.append(
                        fq.average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type=n_plays))
            print('Calculated %s features, took %s, %s completed' % (len(feature_list),
                                                                     "{0:.2}s".format(time.time() - start_time),
                                                                     str((scout_id - init_id) * 100 / (last_id - init_id)) + '%'))
            self.descriptor_list.append(Descriptors(hash=hash, scout_id=scout_id, feature_array=feature_list))
        print('Generated queries for %s scouts' % str(len(self.descriptor_list)))

    def parallel_calculation(self, init_id, last_id):
        l = last_id - init_id
        hash = str(random.getrandbits(128))
        print('Initializing Threads')
        for i in range(NUM_PARALLEL_CONNECTIONS):
            print(0 + i * math.floor(l / NUM_PARALLEL_CONNECTIONS),
                  min(l + 1, int((i + 1) * math.floor(l / NUM_PARALLEL_CONNECTIONS))))
            t = threading.Thread(name='t' + str(i),
                                 target=self.generate_feature_queries,
                                 args=(init_id + i * math.floor(l / NUM_PARALLEL_CONNECTIONS),
                                        min(last_id + 1, init_id + int((i + 1) * math.floor(l / NUM_PARALLEL_CONNECTIONS))), hash))
            t.start()
            print('Thread %s Running' % t.name)
        t.join()
        self.pg.InsertList(self.descriptor_list)

