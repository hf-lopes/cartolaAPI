from sklearn.preprocessing import OneHotEncoder
import pandas as pd

class DatasetProcessing():
    def __init__(self, df, auxiliary):
        self.df = df
        self.auxiliary = auxiliary

    def count_null(self):
        for column in self.df.columns:
            if column not in self.auxiliary:
                if self.df[column].isnull().sum() > 0:
                    print('{0:.<50}{1}'.format(column, self.df[column].isnull().sum()))

    def drop_zero_var(self):
        zero_var = self.df.var() == 0
        zero_var_cols = zero_var.index[zero_var]
        print('ZERO VARIANCE FEATURES:\n')
        for col in zero_var_cols:
            if col not in self.auxiliary:
                self.df.drop(col, axis=1, inplace=True)
                print(col)


    def drop_null(self, max_null_ratio=0.4):
        removed_features = self.df.loc[:, self.df.isnull().sum() / len(self.df) > max_null_ratio]

        print('\n\nREMOVED FEATURES WITH MORE THAN 40% NULL\n')
        for col in removed_features.columns:
            if col not in self.auxiliary:
                self.df.drop(col, axis=1, inplace=True)
                print(col)

        print('\n\nNULL COUNT IN REMAINING FEATURES\n')
        for col in self.df.columns:
            if col not in self.auxiliary:
                if self.df[col].isnull().sum() > 0:
                    print('{0:.<50}{1}'.format(col, self.df[col].isnull().sum()))



    def fill_null(self, value, feature_list = []):
        print('\n\nFEATURES FILLED WITH ' + str(value) + '\n')
        for col in feature_list:
            if value != 'mean':
                self.df.loc[self.df[col].isnull(), col] = value
            else:
                self.df.loc[self.df[col].isnull(), col] = self.df[col].mean()

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
        return self.df



    def correct_dataset(self):
        self.df.loc[self.df.home_team == 0, 'home_team'] = -1
        self.df = self.df.loc[self.df.has_played == 1]
        return self.df