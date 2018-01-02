from sklearn import metrics
import pandas as pd


class EvaluationMetrics:


    def get_best_team_predicted(self, X_test, scores):
        players_per_pos = (1,2,2,3,3,1)
        df = X_test
        df['scores'] = scores.values
        team_dict = dict()
        for year in sorted(df.years.unique()):
            team_dict[year] = dict()
            for rodada in sorted(df.match_week.unique()):
                team_dict[year][rodada] = dict()
                for position in sorted(df.position_id.unique()):
                    team_dict[year][rodada][position] = list()
                    years = df.loc[df.year == year]
                    rodada = years.loc[years.match_week == rodada]
                    top_players = rodada.loc[rodada.position_id == position].sort_values(by='scores', ascending=False)[0:players_per_pos[position]]
                    for players in top_players:
                        element = dict()
                        element['name'] = players.name
                        element['id'] = players.id
                        element['predicted'] = players.predicted
                        team_dict[year][rodada][position].append(element)

        print(team_dict)
        return team_dict

    def get_top_players(self, X_test, scores, num_players):
        df = X_test
        df['scores'] = scores.values
        top_list = list()
        top_players = df.sort_values(by='scores', ascending=False)[0:num_players]
        for players in top_players:
            element = dict()
            element['name'] = players.name
            element['id'] = players.id
            element['scout_id'] = players.index
            element['predicted'] = players.predicted
            top_list.append(element)

        print(top_list)
        return top_list

    def get_top_real_predicted_scores(self, X_test, y_test, predicted, num_players):
        real_top_list = self.get_top_players(X_test, y_test, num_players)
        df = X_test
        df['scores'] = y_test.values
        df['predicted'] = predicted.values
        for element in real_top_list:
            print('Player made: %s points and the model predicted: %s' %(element['predicted'], df.loc[[element['scout_id']]].predicted.values))