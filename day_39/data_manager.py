import requests


class DataManager:
    def __init__(self, url, header):
        self.header = header
        self.url = url

    def get_data(self):
        response = requests.get(url=self.url, headers=self.header)
        response.raise_for_status()
        return response.json()["prices"]

    def put_iata(self, iata, id):
        payload = {
            "price": {
                "iataCode": iata,
            }
        }
        response = requests.put(url=self.url + "/" + str(id), json=payload, headers=self.header)
        response.raise_for_status()
        return response

    def put_price(self, price, id):
        payload = {
            "price": {
                "lowestPrice": price,
            }
        }
        response = requests.put(url=self.url + "/" + str(id), json=payload, headers=self.header)
        response.raise_for_status()
        return response

