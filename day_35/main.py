import secret
import requests
import pprint
import smtplib

ALERT_LEVEL = 700
parameters = {
    "lat": secret.my_lat,
    "lon": secret.my_lon,
    "units": "metric",
    "cnt": "10",
    "appid": secret.weather_api_key,
}


def send_mail(receiver, text):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=secret.email, password=secret.password)
        connection.sendmail(from_addr=secret.email, to_addrs=receiver, msg=f"Subject:Dante alert!\n\n{text}")


response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]
for weather_slice in weather_data:
    weather_point = weather_slice["weather"][0]
    weather_code = weather_point["id"]
    weather_time = weather_slice["dt_txt"]
    weather_description = weather_point["description"]
    if weather_code < ALERT_LEVEL:
        send_mail(secret.receiver, f"Expected {weather_description} at {weather_time}.")
        break
