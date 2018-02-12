from sklearn import metrics
from sklearn.metrics import accuracy_score, mean_squared_error, explained_variance_score, mean_absolute_error, median_absolute_error,r2_score
import pandas as pd
import numpy as np
import math

class EvaluationMetrics:

    def __init__(self, df, y_train, y_test, train_score, test_score):
        self.df = df
        self.y_test = y_test
        self.test_score = test_score
        self.y_train = y_train
        self.train_score = train_score

        predicted = pd.concat([pd.DataFrame(self.train_score, columns=['preds'], index=self.y_train.index),
                               pd.DataFrame(self.test_score, columns=['preds'], index=self.y_test.index)])
        self.df = pd.concat([self.df, predicted], axis=1, ignore_index=False)

    def return_top_players(self, position='all', match_week='all', year='all', number_of_players = 10, real=True, df=None):
        if df is None:
            df = self.df
        if position != 'all':
            df = df.loc[df.position_id == position]
        if match_week != 'all':
            df = df.loc[df.match_week == match_week]
        if year != 'all':
            df = df.loc[df.year == year]

        if real:
            top_players = df.sort_values(by='score', ascending=False).iloc[0:number_of_players]
        else:
            top_players = df.sort_values(by='preds', ascending=False).iloc[0:number_of_players]

        return top_players[['scout_id', 'match_week', 'player_id', 'team_id', 'position_id', 'score', 'preds', 'name', 'year','has_played']]

    def eval_top(self, position='all',match_week='all', year='all', number_of_players=10, real=True, df=None, show=True):
        if real:
            print("Top %s real performances compared to expected performance for position %s on round %s on year %s"
                  % (str(number_of_players), str(position), str(match_week), str(year)))
        else:
            print("Top %s Predicted players metrics compared to real performance for position %s on round %s on year %s"
                  % (str(number_of_players), str(position), str(match_week), str(year)))
        top_players = self.return_top_players(position=position, match_week=match_week, year=year, number_of_players=number_of_players, real=real, df=df)
        evaluation = self.__eval_metrics(desired=top_players.score.values, preds1=top_players.preds.values, show=show)

        return evaluation

    def get_best_team(self, match_week, year, team_formation=(2,2,3,3), real=True, show=True):
        if real:
            print("Selecting best real performing team for match_week %s on year %s " % (str(match_week), str(year)))
        else:
            print("Selecting best predicted performing team for match_week %s on year %s " % (str(match_week), str(year)))
        top_players = pd.DataFrame()
        for position, number_of_players in enumerate(team_formation):
            top_players = pd.concat([top_players, self.return_top_players(position=position+2, match_week=match_week,
                                                                          year=year, real=real,
                                                                          number_of_players=number_of_players)])

        if top_players.shape[0] == 10:
            evaluation = self.__eval_metrics(desired=top_players.score.values, preds1=top_players.preds.values, show=show)

            return top_players, evaluation

        return 'Missing data', 'Empty'

    def get_performance_without_outliers(self, match_week, year, real=True):
        print("Evaluation performance without the top and bottom 10 %% performing players for round %s on year %s" % (str(match_week), str(year)))
        df = self.df.sort_values(by='score', ascending=False).iloc[int(0.1*self.df.shape[0]):int(0.9*self.df.shape[0])]
        evaluation = self.eval_top(match_week=match_week, year=year, real=real, df=df, number_of_players=df.shape[0])
        return evaluation

    def get_model_average_score(self):
        points_list = []
        for match_week in range(2, 39):
            for year in range(2015, 2018):
                top_players, evaluation = self.get_best_team(match_week=match_week, year=year, real=False, show=False)
                if type(top_players) is not str:
                    points_list.append(evaluation['pred_sum'])

        avg_points = np.sum(points_list) / len(points_list)
        print("Avg model points per round is %s " % str(avg_points))
        return avg_points


    def __eval_metrics(self, desired, preds1, show=True):
        evaluation = dict()
        if show:
            print("Evaluating Data: ")

            print("Predited total points: %s" % str(np.sum(preds1)))
            print("Real total points: %s" % str(np.sum(desired)))
            print("Prediction Std Dev: %s" % str(np.std(preds1)))
            print("Prediction Avg: %s" % str(np.mean(preds1)))
            print("Desired Std Dev: %s" % str(np.std(desired)))
            print("Desired Avg: %s" % str(np.mean(desired)))
            print("Explained Variance: %s" % str(explained_variance_score(desired, preds1)))
            print("Mean Absolute error: %s" % str(mean_absolute_error(desired, preds1)))
            print("RMS Error: %s" % str(math.sqrt(mean_squared_error(desired, preds1))))
            print("Median Abs Error: %s" % str(median_absolute_error(desired, preds1)))
            print("R2 Score: %s" % str(r2_score(desired, preds1)))

            print('\n\n\n')


        evaluation['pred_sum'] = np.sum(preds1)
        evaluation['pred_avg'] = np.mean(preds1)
        evaluation['pred_dev'] = np.std(preds1)
        evaluation['desired_sum'] = np.sum(desired)
        evaluation['desired_avg'] = np.mean(desired)
        evaluation['desired_dev'] = np.std(desired)


        evaluation['explained_variance'] = explained_variance_score(desired, preds1)
        evaluation['mean_abs_error'] = mean_absolute_error(desired, preds1)
        evaluation['root_mean_sqrt_error'] = math.sqrt(mean_squared_error(desired, preds1))
        evaluation['median_abs_error'] = median_absolute_error(desired, preds1)
        evaluation['r2_score'] = r2_score(desired, preds1)
        return evaluation