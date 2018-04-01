import numpy as np
import matplotlib.pyplot as plt
from xgboost import plot_importance
import pandas as pd


class ResultsVisualization:
    def __init__(self, y_test, test_score, y_train, train_score, model):
        self.y_test = y_test
        self.test_score = test_score
        self.y_train = y_train
        self.train_score = train_score
        self.model = model

    def feature_importance(self):
        plot_importance(self.model)
        fig = plt.gcf()
        fig.set_size_inches(20, 20)
        plt.show()

    def train_test_curves(self):
        results = self.model.evals_result()
        epochs = len(results['validation_0']['auc'])
        x_axis = range(0, epochs)
        fig, ax = plt.subplots()
        ax.plot(x_axis, results['validation_0']['auc'], label='Train')
        ax.plot(x_axis, results['validation_1']['auc'], label='Test')
        ax.legend()
        plt.ylabel('AUC')
        plt.title('XGBoost AUC')
        plt.show()

    def score_hist(self):
        plt.hist(self.y_train, bins=30, color='g', normed=True, label='Desired', alpha=0.5)
        plt.hist(self.train_score, bins=30, color='r', normed=True, label='Predicted', alpha=0.5)
        plt.title('Train score histogram')
        plt.show()
        plt.hist(self.y_test, bins=30, color='g', normed=True, label='Desired', alpha=0.5)
        plt.hist(self.test_score, bins=30, color='r', normed=True, label='Predicted', alpha=0.5)
        plt.title('Test score histogram')
        plt.show()