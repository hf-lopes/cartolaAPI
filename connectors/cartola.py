import json
import requests
from constants import cartola_endpoint


class CartolaConnector:

    def read_api(self, endpoint, params=None):
        url = cartola_endpoint[endpoint]
        if params is not None:
            url = cartola_endpoint + params
        response = requests(url)
        print(response, type(response))
        return response

    def read_atletas_rodada_atual(self):
        endpoint = 'atletas_mercado'
        response = self.read_api(endpoint)
        return response

    def read_scout_rodada_anterior(self):
        endpoint = 'atletas_pontuados'
        response = self.read_api(endpoint)
        return response

    def read_partidas_rodada_atual(self):
        endpoint = 'partidas'
        response = self.read_api(endpoint)
        return response

    def read_partidas_rodada(self, rodada):
        endpoint = 'partidas'
        params = '/' + str(rodada)
        response = self.read_api(endpoint, params)
        return response

    def read_status_rodada_atual(self):
        endpoint = 'mercado'
        response = self.read_api(endpoint)
        return response


