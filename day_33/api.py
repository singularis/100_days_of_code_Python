import requests
from datetime import datetime

# responce = requests.get(url='http://api.open-notify.org/iss-now.json')
# responce.raise_for_status()
#
# data = responce.json()["iss_position"]
# print(data)

parametrs = {
    "lat": 50.064651,
    "lng": 19.944981,
    "formatted": 0
}

responce = requests.get(url='https://api.sunrise-sunset.org/json', params=parametrs)
responce.raise_for_status()
data = responce.json()
sun = data["results"]["sunrise"]
time_now = datetime.now()
print(sun.split("T")[1].split(":"))