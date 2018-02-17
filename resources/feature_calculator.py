from connectors.postgree import PostGreConnectorSQL, PostGreConnector
from modules.feature_queries import FeatureQueries
from models.Descriptors import Descriptors
from constants import NUM_PARALLEL_CONNECTIONS
import threading
import time
import math
import random
import pandas as pd
import numpy as np
from multiprocessing import Queue
from constants import abreviacao


class FeatureCalculator:

    def __init__(self):
        self.pg = PostGreConnector()
        self.q = Queue()
        self.hash = None
        self.df = pd.DataFrame()
        self.consume = 0


    def generate_feature_queries(self):
        time.sleep(2)
        while not self.q.empty():

            df_scout = pd.DataFrame()
            start_fetch = time.time()
            interval = self.q.get()
            values = list()
            for value in range(interval[0], interval[1]):
                values.append(value)

            scout_id = tuple(values)
            print(scout_id)
            fq = FeatureQueries(scout_id)
            start_time = time.time()

            df_scout = pd.concat([df_scout, fq.get_basic_info()], axis=1)

            if df_scout.shape[0] == 0:
                print('No scout for this ID')
                continue
            for n_rounds in [1, 10, 20, 30]:


                df_scout = pd.concat([df_scout, fq.average_points(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.average_price(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.stddev_points(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.stddev_price(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.team_average_points(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.team_average_price(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.enemy_average_points(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.enemy_average_price(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.team_goals_scored(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.team_goals_taken(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.team_points(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.enemy_goals_scored(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.enemy_goals_taken(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.enemy_points(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.home_away(scout_id=scout_id)], axis=1)

                df_scout = pd.concat([df_scout, fq.team_points_enemy_points_ratio(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.team_goals_scored_enemy_goals_taken_ratio(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.team_goals_taken_enemy_goals_scored_ratio(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.team_goals_taken_enemy_goals_scored_ratio_home_away(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.team_goals_scored_enemy_goals_taken_ratio_home_away(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.team_price_enemy_price_ratio(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.team_points_enemy_points_ratio(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.num_std_dev_team_points_enemy_points(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                # df_scout = pd.concat([df_scout, fq.team_points_enemy_points_ratio_home_away(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.clean_sheet_chance(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.player_goal_participation_team_ratio(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.team_offense_enemy_defense(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.team_defense_enemy_offense(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.team_defense_enemy_goals(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.team_rb_enemy_pe(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.player_pe_enemy_rb(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.player_fs_enemy_fc(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.enemy_fs_player_fc_ca_cv(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.team_offense_enemy_fauls(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.team_fauls_enemy_offense(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.team_goal_chance(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                df_scout = pd.concat([df_scout, fq.enemy_goal_chance(scout_id=scout_id, n_rounds=n_rounds)], axis=1)

                for n_plays in range(1, 19):
                    df_scout = pd.concat([df_scout, fq.average_plays(scout_id=scout_id, n_rounds=n_rounds, play_type=n_plays)], axis=1)

            # print(df_scout)
            self.df = pd.concat([self.df, df_scout], axis=0)
            self.consume += 1
            self.df.to_csv('datasets/calculated_features_partial_' + str(self.consume) + '_' + self.hash + '.csv')
            print('Took %s ms to calculate all features for scout_id %s' % (1000*(time.time() - start_fetch), scout_id))
            # print('Queue has %s elements' % (self.q.qsize()))

    def parallel_calculation(self, init_id, last_id, description='default'):
        print('initializing queue')


        self.hash = str(random.getrandbits(128))
        print('Initializing Threads')
        for i in range(NUM_PARALLEL_CONNECTIONS):
            t = threading.Thread(name='t' + str(i),
                                 target=self.generate_feature_queries)
            t.start()
            print('Thread %s Running' % t.name)


        for scout_id in range(init_id, last_id + 1, 5000):
            self.q.put([scout_id, scout_id + 5000])
        t.join()
        self.df.to_csv('datasets/calculated_features_final_' + description + '_' + str(init_id) + '_' + str(last_id) + '_' + self.hash + '.csv')
        # self.pg.InsertList(self.descriptor_list)

