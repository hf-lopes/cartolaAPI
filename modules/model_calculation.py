from connectors.postgree import PostGreConnectorSQL
import pandas
import numpy as np
class ModelCalculation:

    def __init__(self, feature_hash):
        self.hash = feature_hash
        self.pg = PostGreConnectorSQL()

    def __get_data(self):
        query_file = open('queries/calculated_features.sql')
        query_file = query_file.read()
        query = query_file.format(self.hash)
        df = self.pg.execute_query(query)
        return np.array(df['feature_array']), np.array(df['points'])

    def NN(self, params = None):
        features, score = self.__get_data()
        print(score)