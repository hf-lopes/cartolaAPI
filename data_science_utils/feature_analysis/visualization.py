import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.graphics import tsaplots
import pandas as pd
from matplotlib import gridspec

class FeatureVisualization:

    def __init__(self, df, auxiliary):
        self.df = df
        self.auxiliary = auxiliary

    def pizza_graph(self, col, show=False):

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = list(self.df[col].value_counts().index)
        sizes = []
        for label in labels:
            sizes.append(self.df.loc[self.df[col] == label].score.mean())

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes,labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        if show:
            plt.show()
    def feature_distribution_violin(self, col, show=False):
        sns.violinplot(y=col, x='score', data=self.df, inner="quartile")
        plt.title('Violin plot of feature '+ col)
        if show:
            plt.show()

    def swarm_feature_plot(self, col, show=False):
        df = self.df.sample(frac=0.15)
        sns.set_style("whitegrid")
        ax = sns.swarmplot(x=col, y='score', data=df)
        ax = sns.boxplot(x=col, y="score", data=df,
                         showcaps=False, boxprops={'facecolor': 'None'},
                         showfliers=False, whiskerprops={'linewidth': 0})

        if show:
            plt.show()

    def feature_correlation(self,col,ax,num_lags, show=False):
        df = self.df[[col,'score']]
        tsaplots.plot_acf(df[df[col].notnull()][col], ax=ax, lags=num_lags)
        ax.set_ylim(bottom=-0.1, top=0.1)
        if show:
            plt.show()

    def feature_stats(self,col, show=False):
        df = self.df
        df = df.groupby(by='match_week', as_index=True)
        mean = df.mean()
        first_quartile = df.apply(lambda x: x.quantile(0.25))
        third_quartile = df.apply(lambda x: x.quantile(0.75))
        plt.plot(mean.index, mean)
        mean.plot()
        plt.fill_between(mean.index, first_quartile, third_quartile, alpha='0.5', facecolors='green')
        plt.title('Statistics of feature ' + col)
        if show:
            plt.show()

    def dataset_visualization(self, num_lags=500, features_to_plot=()):
        for col in self.df.columns:
            if col in features_to_plot:
                if col not in self.auxiliary:
                    if col != 'score':
                        fig = plt.figure(figsize=(15, 8))
                        gs = gridspec.GridSpec(2, 2)

                        ax1 = fig.add_subplot(gs[0, 0])
                        self.feature_distribution_violin(col, show=False)

                        ax2 = fig.add_subplot(gs[0, 1])
                        self.swarm_feature_plot(col, show=False)

                        ax3 = fig.add_subplot(gs[1, 0])
                        self.feature_correlation(col=col,ax=ax3,num_lags=num_lags, show=False)

                        # ax4 = fig.add_subplot(gs[1, 1])
                        # self.feature_stats(col, show=False)

                        plt.show()