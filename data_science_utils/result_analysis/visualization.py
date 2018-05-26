import numpy as np
import matplotlib.pyplot as plt
from xgboost import plot_importance
import pandas as pd

import math

import numpy as np
from sklearn.metrics import mean_squared_error, \
    explained_variance_score, mean_absolute_error, median_absolute_error, \
    r2_score
from toolz.curried import *


def feature_importance(model):
    plot_importance(model)
    fig = plt.gcf()
    fig.set_size_inches(20, 20)
    plt.show()

def get_top_players(eval_df, target, prediction_col, real=True,
                    position='all', num_of_players=100):
    if real:
        eval_df.sort_values(target, ascending=False)
    else:
        eval_df.sort_values(prediction_col, ascending=False)

    if position != 'all':
        pos_df = eval_df.loc[eval_df.Posicao == position]
        sampled_df = pos_df.head(num_of_players)
    else:
        sampled_df = eval_df.head(num_of_players)

    return sampled_df


def get_best_team(eval_df, target, prediction_col, rodada, ano, real=True,
                  team_formation=(2, 2, 3, 3)):
    df = eval_df.loc[(eval_df.ano == ano) & (eval_df.Rodada == rodada)]
    return pd.concat(list(map(
        get_top_players(df, target, prediction_col, real=real, position=_,
                        num_of_players=_), team_formation,
        (2, 3, 4, 5))))

def get_performance_without_outliers(eval_df, target, prediction_col,
                                     outlier_prct=0.1, real=True):
    if real:
        eval_df.sort_values(target, ascending=False)
    else:
        eval_df.sort_values(prediction_col, ascending=False)

    df = eval_df.iloc[
         round(outlier_prct * eval_df.shape[0]):round(
             (1 - outlier_prct) * eval_df.shape[0])]

    return df.head(50)
