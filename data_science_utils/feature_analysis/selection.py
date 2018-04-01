import numpy as np
import operator
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
from sklearn.feature_selection import RFE, RFECV
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt


class FeatureSelection:
    def __init__(self, df, auxiliary):
        self.df = df
        self.X = df.drop(['score'], axis=1)
        self.X.drop(auxiliary, axis=1, inplace=True)
        self.y = df.score
        self.selected_features = list(self.X.columns)

    ## Feature Ranking
    # -- Here features are measured individually to find the most important features by several metrics
    # -- Filters: pre-processing feature selection

    def rank_correlation(self, selection_rate=1):
        corr = {}
        for column in list(self.selected_features):
            m = np.corrcoef(self.X[column], self.y)
            corr[column] = abs(m[0, 1])
        sorted_corr = sorted(corr.items(), key=operator.itemgetter(1), reverse=True)
        top_columns = []
        print('Feature Correlation with Target:')
        for key, value in sorted_corr:
            top_columns.append(key)
            print('{0:.<50}{1}'.format(key, str(value)))

        self.selected_features = top_columns[0:int(selection_rate * len(top_columns))]

    def one_feat_classifier(self, selection_rate=1, threshold=0.5):
        clas_train_score = dict()
        clas_test_score = dict()

        for column in self.selected_features:
            train = self.X[column]
            train = train.values.reshape(-1, 1)
            kf = KFold(n_splits=10)
            train_score = 0
            test_score = 0
            for train_index, test_index in kf.split(train):
                X_train, X_test = train[train_index], train[test_index]
                y_train, y_test = self.y.iloc[train_index], self.y.iloc[test_index]
                clas = RandomForestRegressor(n_estimators=10)
                clas.fit(X_train, y_train)
                train_predict = clas.predict(X_train)
                test_predict = clas.predict(X_test)
                train_score += mean_squared_error(train_predict, y_train)
                test_score += mean_squared_error(test_predict, y_test)

            clas_train_score[column] = train_score / kf.get_n_splits(train)
            clas_test_score[column] = test_score / kf.get_n_splits(train)

        sorted_test_score = sorted(clas_test_score.items(), key=operator.itemgetter(1), reverse=False)
        top_columns = []
        print('Single feature root mean square for test and train:')
        for key, value in sorted_test_score:
            top_columns.append(key)
            print('{0:.<50}{1}       {2}'.format(key, str(value), str(clas_train_score[key])))

        self.selected_features = top_columns[0:int(selection_rate * len(top_columns))]

    def corr_heatmap(self):
        # correlation map
        f, ax = plt.subplots(figsize=(30, 30))
        sns.heatmap(self.X.corr(), linewidths=.1, ax=ax)
        plt.show()

    ## Feature Subset Selection
    # -- Here we try to find the best set of features to model our dataset
    # -- Wrapers: feature selection using model score as parameter
    # -- Embedded: during trainig feature selection (already done by xgboost)
    def RFE(self, num_features=5, replace=False):
        model = LinearRegression()
        rfe = RFE(model, num_features)
        rfe = rfe.fit(self.X, self.y)
        col = self.selected_features
        ranking_dict = {}
        for index, importance in enumerate(rfe.ranking_):
            ranking_dict[col[index]] = importance
        sorted_ranking = sorted(ranking_dict.items(), key=operator.itemgetter(1))
        best_feats = []
        print('Feature subset ranking: ')
        for key, value in sorted_ranking:
            print('{0:.<50}{1}'.format(key, str(value)))
            if value == 1:
                best_feats.append(key)

        if replace:
            self.selected_features = best_feats

    def RFECV(self, replace=False, scoring='accuracy'):
        model = LinearRegression()
        rfe = RFECV(model, cv=5, scoring=scoring)
        rfe = rfe.fit(self.X, self.y)
        num_features = rfe.n_features_
        col = self.selected_features
        ranking_dict = {}
        print("The optimal number of features is: %s " % str(num_features))
        for index, importance in enumerate(rfe.ranking_):
            ranking_dict[col[index]] = importance
        sorted_ranking = sorted(ranking_dict.items(), key=operator.itemgetter(1))
        best_feats = []
        print('Feature subset ranking: ')
        for key, value in sorted_ranking:
            print('{0:.<50}{1}'.format(key, str(value)))
            if value == 1:
                best_feats.append(key)

        if replace:
            self.selected_features = best_feats

        # Plot number of features VS. cross-validation scores
        plt.figure()
        plt.grid(b=True)
        plt.xlabel("Number of features selected")
        plt.yticks(np.arange(.2, 1.05, .05))
        plt.xticks(np.arange(1, len(rfe.grid_scores_), 1))
        plt.ylabel("Cross validation score of number of selected features")
        plt.plot(range(1, len(rfe.grid_scores_) + 1), rfe.grid_scores_)
        plt.show()

    ## Dimensionality Reduction
    # -- Here we reduce the dimensionality by combining features and changing the search space

    def PCA(self, n_components=50):
        sc = StandardScaler()
        scaled_data = sc.fit_transform(self.X)
        pca = PCA(n_components=n_components)
        self.X = pca.fit_transform(scaled_data)
        print(sum(pca.explained_variance_ratio_))

    def plot_PCA(self):
        var_explain = []
        sc = StandardScaler()
        scaled_data = sc.fit_transform(self.X)
        for i in range(1, self.X.shape[1]):
            pca = PCA(n_components=i)
            x_pca = pca.fit_transform(scaled_data)
            var_explain.append(np.sum(pca.explained_variance_ratio_))

        plt.figure(figsize=(15, 10))
        plt.grid(b=True)
        plt.plot(var_explain[:])
        plt.xlabel('Number of PCA Components')
        plt.ylabel('Explained Variance Ratio')
        plt.title('Explained Variance by number of components')
        plt.yticks(np.arange(.4, 1.05, .05))
        plt.xticks(np.arange(1, self.X.shape[1], 1))
        plt.show()

