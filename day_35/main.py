import secret
import requests
import pprint
parameters = {
    "lat": secret.my_lat,
    "lon": secret.my_lon,
    "units": "metric",
    "cnt": "10",
    "appid": secret.weather_api_key,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
pprint.pprint(weather_data)
print(weather_data)

