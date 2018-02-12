from sklearn.metrics import accuracy_score, mean_squared_error, explained_variance_score, mean_absolute_error, median_absolute_error,r2_score
from sklearn.model_selection import train_test_split
import time
import math
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler


class TrainTest():
    def __init__(self, df, auxiliary):
        self.df = df
        self.auxiliary = auxiliary

    def split_dataset(self, seed=47, train_ratio=0.7):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.df.drop(["score"], axis=1),
                                                                                self.df.score,
                                                                                train_size=train_ratio)
        self.X_train.drop(self.auxiliary, axis=1, inplace=True)
        self.X_test.drop(self.auxiliary, axis=1, inplace=True)
        self.train = pd.concat([self.X_train, self.y_train], axis=1)

        self.test = pd.concat([self.X_test, self.y_test], axis=1)

    def get_used_features(self,feature_importance, show=False):
        self.used_features = list()
        self.unused_features = list()
        for i in range(len(feature_importance)):
            feat_importance = feature_importance[i]
            if feat_importance > 0:
                col = self.X_train.columns[i]
                self.used_features.append(col)
            else:
                col = self.X_train.columns[i]
                self.unused_features.append(col)

        if show:
            print('Used features:')
            for col in self.used_features:
                print(col)
            print('\nUnused features:')
            for col in self.unused_features:
                print(col)
            print('\n\n')

    def normalize_data(self):
        ss = StandardScaler()
        self.X_train = ss.fit_transform(self.X_train)
        self.X_test = ss.transform(self.X_test)


    def evaluate_train(self, model_class, model_params):
        self.model = model_class(**model_params)

        self.model.fit(self.X_train, self.y_train)
        desired = self.y_train
        preds1 = self.model.predict(self.X_train)

        evaluation = dict()
        print("Evaluating Train Data: ")
        print("Prediction Std Dev: %s" % str(np.std(preds1)))
        print("Prediction Avg: %s" % str(np.mean(preds1)))
        print("Desired Std Dev: %s" % str(np.std(desired.values)))
        print("Desired Avg: %s" % str(np.mean(desired.values)))
        print("Explained Variance: %s" % str(explained_variance_score(desired.values, preds1)))
        print("Mean Absolute error: %s" % str(mean_absolute_error(desired.values, preds1)))
        print("RMS Error: %s" % str(math.sqrt(mean_squared_error(desired.values, preds1))))
        print("Median Abs Error: %s" % str(median_absolute_error(desired.values, preds1)))
        print("R2 Score: %s" % str(r2_score(desired.values, preds1)))
        evaluation['explained_variance'] = explained_variance_score(desired.values, preds1)
        evaluation['mean_abs_error'] = mean_absolute_error(desired.values, preds1)
        evaluation['root_mean_sqrt_error'] = math.sqrt(mean_squared_error(desired.values, preds1))
        evaluation['median_abs_error'] = median_absolute_error(desired.values, preds1)
        evaluation['r2_score'] = r2_score(desired.values, preds1)

        return self.model, preds1, evaluation

    def evaluate_test(self):
        preds1 = self.model.predict(self.X_test)
        desired = self.y_test
        evaluation = dict()


        print("Evaluating Test Data: ")
        print("Prediction Std Dev: %s" % str(np.std(preds1)))
        print("Prediction Avg: %s" % str(np.mean(preds1)))
        print("Desired Std Dev: %s" % str(np.std(desired.values)))
        print("Desired Avg: %s" % str(np.mean(desired.values)))
        print("Explained Variance: %s" % str(explained_variance_score(desired.values, preds1)))
        print("Mean Absolute error: %s" % str(mean_absolute_error(desired.values, preds1)))
        print("RMS Error: %s" % str(math.sqrt(mean_squared_error(desired.values, preds1))))
        print("Median Abs Error: %s" % str(median_absolute_error(desired.values, preds1)))
        print("R2 Score: %s" % str(r2_score(desired.values, preds1)))
        evaluation['explained_variance'] = explained_variance_score(desired.values, preds1)
        evaluation['mean_abs_error'] = mean_absolute_error(desired.values, preds1)
        evaluation['root_mean_sqrt_error'] = math.sqrt(mean_squared_error(desired.values, preds1))
        evaluation['median_abs_error'] = median_absolute_error(desired.values, preds1)
        evaluation['r2_score'] = r2_score(desired.values, preds1)

        return preds1, evaluation


    def save_model(self, filename):
        # save model to file
        pickle.dump(self.model, open(filename, "wb"))
