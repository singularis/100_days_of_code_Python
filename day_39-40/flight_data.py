import requests


class IATAmanager:
    def __init__(self, url, header):
        self.header = header
        self.url = url

    def get_codes(self, city):
        payload = {
            "term": city,
            "locale": "en-US",
            "limit": 10,
            "active_only": True,
            "location_types": "airport",
        }
        header = {
            "apikey": self.header,
            "accept": "application/json"
        }
        url = self.url +"locations/query"
        response = requests.get(url, params=payload, headers=header)
        response.raise_for_status()
        return response.json()["locations"][0]

