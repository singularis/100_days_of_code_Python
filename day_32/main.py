import pandas as pd
from datetime import datetime
import os
import random
import smtplib
from secret import email, password


def send_mail(receiver, text):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=receiver, msg=f"Subject:Ping-pong\n\n{text}")


def read_date():
    data = pd.read_csv("./birthdays.csv")
    return data.values.tolist()


def payload_body(name):
    random_file = random.choice(os.listdir("./letter_templates"))
    with open("./letter_templates/" + random_file) as f:
        payload = f.read()
        payload_to_send = payload.replace('[NAME]', name)
        return payload_to_send


if __name__ == "__main__":
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    dates_list = read_date()
    for date in dates_list:
        if date[-2] == currentMonth and date[-1] == currentDay:
            mail_body = payload_body(date[0])
            send_mail(date[1], mail_body)
