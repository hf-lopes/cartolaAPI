import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.graphics import tsaplots
import pandas as pd
from matplotlib import gridspec

class FeatureVisualization():

    def __init__(self, df):
        self.df = df

    def feature_distribution_violin(self, col, show=False):
        df = self.df[[col,'target']]
        df.loc[:, 'aux'] = ''
        data = df.dropna(axis=0)
        sns.violinplot(y=col, x='aux', hue='target', split=True, data=data, inner="quartile")
        plt.title('Violin plot of feature '+ col)
        if show:
            plt.show()

    def feature_distribution_histogram(self, col, show=False):
        df = self.df[[col, 'target']]
        df_good = df.loc[df['target'] == 0, col].dropna(axis=0)
        df_bad = df.loc[df['target'] == 1, col].dropna(axis=0)
        plt.hist(df_bad, bins=30, color='r', alpha=0.5, normed=1,label='Fraud')
        plt.hist(df_good, bins=30, color='g', alpha=0.5, normed=1, label='Healthy')
        plt.legend()
        plt.title('Histogram of feature '+ col)
        if show:
            plt.show()

    def feature_correlation(self,col,ax,num_lags, show=False):
        df = self.df[[col,'target']]
        tsaplots.plot_acf(df[df[col].notnull()][col], ax=ax, lags=num_lags)
        if show:
            plt.show()

    def feature_stats(self,col,interval, show=False):
        df = self.df
        df = df.set_index(pd.DatetimeIndex(df['transaction_date']))
        resample = df.resample(interval)[col]
        mean = resample.mean()
        first_quartile = resample.apply(lambda x: x.quantile(0.25))
        third_quartile = resample.apply(lambda x: x.quantile(0.75))
        plt.plot(mean.index, mean)
        mean.plot()
        plt.fill_between(mean.index, first_quartile, third_quartile, alpha='0.5', facecolors='green')
        plt.title('Statistics of feature ' + col)
        if show:
            plt.show()

    def dataset_visualization(self, num_lags=500, interval='1W', features_to_plot=[]):
        for col in self.df.columns:
            if col in features_to_plot:

                fig = plt.figure(figsize=(15, 8))
                gs = gridspec.GridSpec(2, 2)

                ax1 = fig.add_subplot(gs[0, 0])
                self.feature_distribution_violin(col, show=False)

                ax2 = fig.add_subplot(gs[0, 1])
                self.feature_distribution_histogram(col, show=False)

                ax3 = fig.add_subplot(gs[1, 0])
                self.feature_correlation(col=col,ax=ax3,num_lags=num_lags, show=False)

                ax4 = fig.add_subplot(gs[1, 1])
                self.feature_stats(col,interval, show=False)

                plt.show()