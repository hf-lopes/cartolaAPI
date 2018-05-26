import math

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, \
    explained_variance_score, mean_absolute_error, median_absolute_error, \
    r2_score
from toolz.curried import *

pos_list = ["gol", "lat", "zag", "mei", "ata", "tec"]

def get_top_players(eval_df, target, prediction_col, real=True, position='all', num_of_players=100):
    if real:
        sorted_df = eval_df.sort_values(target, ascending=False)
    else:
        sorted_df = eval_df.sort_values(prediction_col, ascending=False)

    if position != 'all':
        pos_df = sorted_df.loc[sorted_df.Posicao == position]
        sampled_df = pos_df.head(num_of_players)
    else:
        sampled_df = sorted_df.head(num_of_players)
    return _get__eval_metrics(sampled_df[prediction_col], sampled_df[target])


def get_best_team(eval_df, target, prediction_col, rodada, ano, real=True,
                  team_formation=(2, 2, 3, 3)):
    df = eval_df.loc[(eval_df.ano == ano) & (eval_df.Rodada == rodada)]
    return pd.DataFrame(pd.concat(list(
        map(lambda num, pos: get_top_players(df, target, prediction_col, real=real, position=pos, num_of_players=num),
            team_formation, ("zag", "lat", "mei", "ata"))), axis=0).mean()).transpose()


def get_average_metrics(eval_df, target, prediction_col):
    return _get__eval_metrics(eval_df[prediction_col], eval_df[target])


def get_performance_without_outliers(eval_df, target, prediction_col, outlier_prct=0.1, real=True):
    if real:
        eval_df.sort_values(target, ascending=False)
    else:
        eval_df.sort_values(prediction_col, ascending=False)

    df = eval_df.iloc[round(outlier_prct * eval_df.shape[0]):round((1 - outlier_prct) * eval_df.shape[0])]

    return _get__eval_metrics(df[prediction_col], df[target])


def get_average_best_team(eval_df, target, prediction_col, rodada_ini, rodada_final, ano, real=True):
    return pd.DataFrame(pd.concat(list(map(lambda x: get_best_team(eval_df, target, prediction_col, x, ano, real),
                              range(rodada_ini, rodada_final + 1))), axis=0).mean()).transpose()


def extract_metric(obj, metric_name):
    return obj[metric_name]


def evaluate_model(eval_df, target, prediction_col):
    return merge({"top_players": get_top_players(eval_df, target, prediction_col)},
                 {"top_players_predicted": get_top_players(eval_df, target, prediction_col, real=False)},
                 {"without_outliers": get_performance_without_outliers(eval_df, target, prediction_col, 0.1)},
                 {"best_team_avgs": get_average_best_team(eval_df, target, prediction_col, 15, 22, 2017, real=True)},
                 {"best_team_avgs_predicted": get_average_best_team(eval_df, target, prediction_col, 15, 22, 2017,
                                                                    real=False)},
                 {"average_metrics": get_average_metrics(eval_df, target, prediction_col)}
                 )


def _get__eval_metrics(preds1, desired):
    evaluation = pd.DataFrame(index=np.arange(1))
    if preds1.shape[0] == 0 or desired.shape[0] == 0:
        return evaluation
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
