import requests


class DataManager:
    def __init__(self, url, header):
        self.header = header
        self.url = url

    def get_data(self):
        response = requests.get(url=self.url, headers=self.header)
        response.raise_for_status()
        return response.json()["prices"]

    def put_date(self, city, iata, price):
        payload = {
            "prices": {
                "City": city,
                "IATA Code": iata,
                "Lowest Price": price,
            }
        }
        response = requests.get(url=self.url, json=payload, headers=self.header)
        response.raise_for_status()
        return response

