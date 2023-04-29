import requests


class DataManager:
    def __init__(self, url, header):
        self.header = header
        self.clear_url = url
        self.url = url + "prices"

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

    def put_user(self, mail):
        payload = {
            "user": {
                "email": mail,
            }
        }
        print(mail)
        response = requests.post(url=self.clear_url + "users", json=payload, headers=self.header)
        response.raise_for_status()
        print(response.url)

    def get_users(self):
        response = requests.get(url=self.clear_url + "users", headers=self.header)
        response.raise_for_status()

        return response.json()["users"]


class NewUser:
    def __init__(self):
        pass

    def get_user(self):
        print("I am here")
        mail_init = input("Input: ")
        main_configr = input("Input again: ")
        if mail_init == main_configr:
            return mail_init
        else:
            self.get_user()
