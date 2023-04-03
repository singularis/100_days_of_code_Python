import requests

responce = requests.get(url='http://api.open-notify.org/iss-now.json')
responce.raise_for_status()

data = responce.json()["iss_position"]
print(data)