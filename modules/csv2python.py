import pandas
from constants import ROOT_DIR


class Csv2Python:

    @staticmethod
    def read_csv(file_name):
        return pandas.read_csv(ROOT_DIR + '/' + file_name)
