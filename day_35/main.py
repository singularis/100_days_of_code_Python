import secret
import requests
import pprint
ALERT_LEVEL = 700
parameters = {
    "lat": secret.my_lat,
    "lon": secret.my_lon,
    "units": "metric",
    "cnt": "10",
    "appid": secret.weather_api_key,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]
pprint.pprint(weather_data)
for weather_slice in weather_data:
    weather_point = weather_slice["weather"][0]
    weather_code = weather_point["id"]
    weather_time = weather_slice["dt_txt"]
    weather_description = weather_point["description"]
    if weather_code < ALERT_LEVEL:
        print(weather_time)


