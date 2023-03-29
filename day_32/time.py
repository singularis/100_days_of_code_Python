import pandas as pd
from random import choice
import smtplib
from secret import email, password, receiver
import datetime


def send_mail(text):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=receiver, msg=f"Subject:Ping-pong\n\n{text}")


def read_date():
    data = pd.read_csv("./quotes.txt")
    return data.values.flatten().tolist()


if __name__ == "__main__":
    quotes = read_date()
    now = datetime.datetime.now()
    rand_quote = choice(quotes)
    if now.strftime("%A") == 'Wednesday':
        send_mail(rand_quote)

