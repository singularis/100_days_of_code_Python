import requests
from datetime import datetime
import smtplib
from secret import email, password
import threading

MY_LAT = 50.064651
MY_LONG = 19.944981
WAIT_TIME_SECONDS = 10

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
def get_pos():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_longitude, iss_latitude

def send_mail(receiver, text):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=receiver, msg=f"Subject:Ping-pong\n\n{text}")
        print(f"Send payload{text}")


def get_sun():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return sunset, sunrise


time_now = datetime.now()


ticker = threading.Event()
while not ticker.wait(WAIT_TIME_SECONDS):
    if get_sun()[0] >= time_now.hour:
        iss_longitude, iss_longitude = get_pos()
        if (MY_LAT - 5 > iss_longitude and iss_longitude < MY_LAT + 5) and (
                MY_LAT - 5 > iss_longitude and iss_longitude < MY_LAT + 5):
            send_mail(email, "Check status")