import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import math
import matplotlib.pyplot as plt
import sys
import csv
sys.path.append('../xgboost/python-package')
import xgboost as xgb
from xgboost.sklearn import XGBClassifier
from sklearn import metrics   #Additional scklearn functions
from sklearn.model_selection import GridSearchCV   #Perforing grid search
import time
import pickle
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn import cross_validation
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE, ADASYN, RandomOverSampler
from sklearn.model_selection import ParameterGrid
from sklearn.linear_model import LinearRegression

class Analyser():

    def __init__(self, dataset_name):
        self.df = pd.read_csv('../datasets/'+ dataset_name)
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.preds_train = None
        self.preds_test = None
        self.model = None

    def dataset_info(self):
        print(list(self.df.columns))
        print(self.df.shape)

    def correct_dataset(self):
        auxiliary = ['scout_id', 'match_week', 'player_id', 'team_id', 'position_id',
                     'home_team.1', 'home_team.2', 'home_team.3', 'year', 'name', 'has_played',
                     'team_goals_taken_last_1_rounds.1', 'team_goals_taken_last_5_rounds.1',
                     'team_goals_taken_last_10_rounds.1', 'team_goals_taken_last_20_rounds.1']
        df_home = self.df.loc[self.df.home_team == 1]
        df_away = self.df.loc[self.df.home_team == 0]
        df_away.home_team = -1
        self.df = pd.concat([df_home, df_away])

        df_errado = self.df.loc[self.df.has_played == 0].loc[self.df.score != 0]  ## Droping players that didnt play and had points
        self.df = self.df.drop(df_errado.index)
        self.df = self.df.loc[self.df.has_played == 1]
        self.df.drop(auxiliary, axis=1, inplace=True)
        self.df.drop(['delta_price'], axis=1, inplace=True)


    def correct_dataset_v2(self, df):
        auxiliary = ['scout_id', 'match_week', 'player_id', 'team_id', 'position_id',
                     'home_team.1', 'home_team.2', 'home_team.3', 'year', 'name', 'has_played',
                     'team_goals_taken_last_1_rounds.1', 'team_goals_taken_last_5_rounds.1',
                     'team_goals_taken_last_10_rounds.1', 'team_goals_taken_last_20_rounds.1']
        df_home = df.loc[df.home_team == 1]
        df_away = df.loc[df.home_team == 0]
        df_away.home_team = -1
        df = pd.concat([df_home, df_away])

        df_errado = df.loc[df.has_played == 0].loc[df.score != 0]  ## Droping players that didnt play and had points
        df = df.drop(df_errado.index)
        df = df.loc[df.has_played == 1]
        df.drop(auxiliary, axis=1, inplace=True)
        df.drop(['delta_price'], axis=1, inplace=True)
        return df


    def over_sampling(self):
        self.X_train, self.y_train = RandomOverSampler().fit_sample(self.X_train, self.y_train.values)
        print(self.X_train.shape)

    def fillna(self):
        ## Replacing nulls with column average
        for column in self.df.columns:
            if 'average' in column or 'goals' in column or 'points' in column:
                self.df[column].fillna(0, inplace=True)

    def hot_encode(self):
        pos_categories = ['Goleiro', 'Lateral', 'Zagueiro', 'Meia', 'Atacante', 'Tecnico']
        enc = OneHotEncoder()
        enc.fit(self.df.position_id.reshape(-1, 1))
        position_encoded = enc.transform(self.df.position_id.reshape(-1, 1)).toarray()
        position_encoded = pd.DataFrame(data=position_encoded, index=self.df.index,
                                        columns=pos_categories)  # 1st row as the column names

        df_hot_encoding = pd.concat([self.df, position_encoded], axis=1)

        df_hot_encoding = df_hot_encoding.loc[df_hot_encoding.position_id != 1]  ## Removendo goleiros e tecnicos
        df_hot_encoding = df_hot_encoding.loc[df_hot_encoding.position_id != 6]
        df_hot_encoding = df_hot_encoding.drop(['Goleiro', 'Tecnico'], axis=1)

        keeper_skills = ['dd', 'dp', 'gs']  ## removendo scouts de goleiro
        for col in list(df_hot_encoding.columns):
            for skill in keeper_skills:
                if skill + '_play' in col:
                    df_hot_encoding.drop([col], axis=1, inplace=True)


        self.df = df_hot_encoding


    def gridsearchCV(self):

        params = {}
        params["objective"] = ("reg:linear",)
        params["learning_rate"] = (0.01, 0.05, 0.1)
        params["min_child_weight"] = (1, 3, 5)
        params["subsample"] = (0.5, 0.7, 0.9)
        params["colsample_bytree"] = (0.5, 0.7, 0.9)
        params["silent"] = (0,)
        params["max_depth"] = (3, 4, 5, 6, 7)
        params["n_estimators"] = (500, 1000, 1500)

        clf = GridSearchCV(XGBClassifier(), params, scoring='neg_mean_squared_error', cv=5, verbose=3)
        clf.fit(np.array(self.df.drop(['score'], axis=1)).astype(float), np.array(self.df.score).astype(float), verbose=True)
        clf.fit(np.array(self.df.drop(['score'], axis=1)).astype(float), np.array(self.df.score).astype(float), verbose=True)
        print(sorted(clf.cv_results_.keys()))






    def train_test_split(self, random=True):
        if random:
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.df.drop(['score'], axis=1),
                                                            self.df.score, test_size=0.2, random_state=42)
        else:
            mask = (self.df.year == 2017) & (self.df.match_week > 20)
            test = self.correct_dataset_v2(self.df.loc[mask])
            train = self.correct_dataset_v2(self.df.loc[~mask])

            self.X_train = train.drop(['score'], axis=1)
            self.y_train = train.score
            self.X_test = test.drop(['score'], axis=1)
            self.y_test = test.score

        print(self.X_train.shape, self.X_test.shape)

    def normalize_data(self):
        ss = StandardScaler()
        self.X_train = ss.fit_transform(self.X_train)
        self.X_test = ss.transform(self.X_test)


    def PCA(self):
        pca = PCA(n_components=52)
        self.X_train = pca.fit_transform(self.X_train)
        self.X_test = pca.transform(self.X_test)
        print(sum(pca.explained_variance_ratio_))

    def fit(self, params):
        start_time = time.time()
        clf = XGBClassifier(**params)
        clf.fit(self.X_train, self.y_train.values, verbose=True)

        print("Model Fit took : %s" % time.time() - start_time)


    def train_linear_reg(self):
        clf = LinearRegression()
        clf.fit(self.X_train, self.y_train)
        self.evaluate_linear_reg(clf, False)
        return clf

    def plot_features_hist(self):
        for column in list(self.X_train.columns):
            plt.hist(self.df[column])
            plt.title('Histogram for feature %s' % (column))
            plt.show()

    def evaluate_linear_reg(self, model, test=True):
        if test:
            dataset = self.X_test
            desired = self.y_test
        else:
            dataset = self.X_train
            desired = self.y_train

        preds1 = model.predict(dataset)
        evaluation = dict()

        print(np.std(preds1))
        print(np.mean(preds1))
        print(np.std(desired.values))
        print(np.mean(desired.values))
        print(metrics.explained_variance_score(desired.values, preds1))
        print(metrics.mean_absolute_error(desired.values, preds1))
        print(math.sqrt(metrics.mean_squared_error(desired.values, preds1)))
        print(metrics.median_absolute_error(desired.values, preds1))
        print(metrics.r2_score(desired.values, preds1))
        evaluation['explained_variance'] = metrics.explained_variance_score(desired.values, preds1)
        evaluation['mean_abs_error'] = metrics.mean_absolute_error(desired.values, preds1)
        evaluation['root_mean_sqrt_error'] = math.sqrt(metrics.mean_squared_error(desired.values, preds1))
        evaluation['median_abs_error'] = metrics.median_absolute_error(desired.values, preds1)
        evaluation['r2_score'] = metrics.r2_score(desired.values, preds1)

        self.score_hist(preds1, desired)

        return evaluation
    def train(self, params):

        start_time = time.time()
        plst = list(params.items())

        xgtrain = xgb.DMatrix(self.X_train, label=self.y_train.values)

        model = xgb.train(plst, xgtrain, num_boost_round=params['n_estimators'])
        self.evaluate(model, test=False)
        print("Model train took : %s" % (time.time() - start_time))
        return model

    def cv_train(self, params):

        start_time = time.time()
        plst = list(params.items())

        xgtrain = xgb.DMatrix(self.X_train, label=self.y_train.values)

        cv = xgb.cv(plst, xgtrain, num_boost_round=params['n_estimators'], nfold=5, metrics='rmse',
                       early_stopping_rounds=200)
        print(cv)
        plt.plot(cv['test-rmse-mean'].values, label='test')
        plt.plot(cv['train-rmse-mean'].values, label='train')
        plt.ylabel('Rmse Mean error')
        plt.show()
        model = self.train(params)
        print("Model train took : %s" % (time.time() - start_time))
        return model


    def save_model(self, model):
        # save model to file
        pickle.dump(model, open("xgboost.pickle.dat", "wb"))

    def load_model(self, model_name):
        loaded_model = pickle.load(open(model_name, "rb"))
        return loaded_model

    def evaluate(self, model, test=True):
        if test:
            dataset = self.X_test
            desired = self.y_test
        else:
            dataset = self.X_train
            desired = self.y_train
        xgtest = xgb.DMatrix(dataset)
        preds1 = model.predict(xgtest)
        evaluation = dict()

        print(np.std(preds1))
        print(np.mean(preds1))
        print(np.std(desired.values))
        print(np.mean(desired.values))
        print(metrics.explained_variance_score(desired.values, preds1))
        print(metrics.mean_absolute_error(desired.values, preds1))
        print(math.sqrt(metrics.mean_squared_error(desired.values, preds1)))
        print(metrics.median_absolute_error(desired.values, preds1))
        print(metrics.r2_score(desired.values, preds1))
        evaluation['explained_variance'] = metrics.explained_variance_score(desired.values, preds1)
        evaluation['mean_abs_error'] = metrics.mean_absolute_error(desired.values, preds1)
        evaluation['root_mean_sqrt_error'] = math.sqrt(metrics.mean_squared_error(desired.values, preds1))
        evaluation['median_abs_error'] = metrics.median_absolute_error(desired.values, preds1)
        evaluation['r2_score'] = metrics.r2_score(desired.values, preds1)

        self.score_hist(preds1, desired)

        return evaluation


    def plot_PCA(self):


        var_explain = []
        for i in range(1, self.df.shape[1]):
            print('Calculating PCA %s' % (str(i)))
            pca = PCA(n_components=i)
            x_pca = pca.fit_transform(self.df)
            var_explain.append(np.sum(pca.explained_variance_ratio_))

        plt.plot(var_explain[:])
        plt.xlabel('Number of PCA Components')
        plt.ylabel('Explained Variance Ratio')
        plt.title('PCA')
        plt.yticks(np.arange(.4, 1.05, .05))
        plt.xticks(np.arange(1, self.df.shape[1], 1))
        plt.show()

    def score_hist(self, predicted, desired):
        plt.hist(desired, bins=30, color='g', normed=True)
        plt.hist(predicted, bins=30, color='r', normed=True)
        plt.show()


    def plot_feature_importance(self, model):

        feat_imp = pd.Series(model.get_fscore()).sort_values(ascending=False)
        feat_imp.plot(kind='bar', title='Feature Importances')
        plt.ylabel('Feature Importance Score')
        plt.show()

    def find_corr(self):

        for column in list(self.X_train.columns):
            m = np.corrcoef(self.df[column], self.df.score)
            print('Feature %s has a correlation of %s with the score' % (column, str(m[0, 1])))
        # print(m)

    def optimize_train(self):

        params = {}
        params["objective"] = ("reg:linear",)
        params["learning_rate"] = (0.01,)
        params["min_child_weight"] = (3,)
        params["subsample"] = (0.85,)
        params["colsample_bytree"] = (0.75,)
        params["silent"] = (1,)
        params["max_depth"] = (5,)
        params["n_estimators"] = (5000,)
        params['gamma'] = (0.1,)
        params['reg_alpha'] = (0.1,)
        keys = list(params.keys())
        keys.extend(['explained_variance', 'mean_abs_error','root_mean_sqrt_error', 'median_abs_error','r2_score'])
        with open('eval_depth.csv', 'w') as csvfile:

            writer = csv.DictWriter(csvfile, fieldnames= keys)
            writer.writeheader()
            for param in ParameterGrid(params):
                    model = an.cv_train(param)
                    print(param)
                    evaluation = an.evaluate(model)
                    evaluation.update(param)
                    writer.writerow(evaluation)






# an = Analyser('calculated_features_final19356_253493_147567893553946290238604574175400014296.csv')
an = Analyser('calculated_features_final19356_253493_251249627637655191393512133460459281226.csv')

## Data Correction
an.fillna()
# an.hot_encode()
an.train_test_split(random=False)
an.correct_dataset()
an.dataset_info()
an.find_corr()
an.plot_features_hist()
# an.over_sampling()
## DATA Adaptation
an.normalize_data()
# an.plot_PCA() ## 30 dimensions has variance of 0.95
an.PCA()


# an.optimize_train()

# params = {}
# params["objective"] = "reg:linear"
# params["learning_rate"] = 0.05
# params["min_child_weight"] = 3
# params["subsample"] = 0.85
# params["colsample_bytree"] = 0.75
# params["silent"] = 0
# params["max_depth"] = 4
# params["n_estimators"] = 500
# params['gamma'] = 0.1
# params['reg_alpha'] = 0.1
# params['reg_lambda'] = 1
# params['scale_pos_weight'] = 1
# model = an.train(params)

# model = an.train_linear_reg()

# model = an.load_model("xgboost.pickle.dat")
# an.evaluate(model, True)
# an.evaluate_linear_reg(model, test=True)

# an.plot_feature_importance(model)
# params = {}
# params["objective"] = "reg:linear"
# params["learning_rate"] = 0.01
# params["min_child_weight"] = 3
# params["subsample"] = 0.7
# params["colsample_bytree"] = 0.7
# params["silent"] = 0
# params["max_depth"] = 4
# params["n_estimators"] = 1000

# model = an.train(params)
# model = an.fit(params)
# an.save_model(model)

# an.fit(params)
# an.gridsearchCV()

