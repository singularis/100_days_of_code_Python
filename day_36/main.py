import smtplib

import secret
import requests
import html
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
DEVIATION = 1


def send_notification(change: float, text: str) -> None:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        sign = f'grown' if deviation > 0 else f'failed'
        connection.login(user=secret.email, password=secret.password)
        print(text)
        connection.sendmail(from_addr=secret.email, to_addrs=secret.receiver, msg=f"Subject:{COMPANY_NAME} price "
                                                                                  f"chained to {round(change, 2)} {sign} !\n\n{text.encode()}")


def get_news():
    parameters_news = {
        "q": COMPANY_NAME,
        "from": "2023-04-19",
        "sortBy": "publishedAt",
        "apiKey": secret.news_api_key,
    }

    url = 'https://newsapi.org/v2/everything'
    r = requests.get(url, params=parameters_news)
    r.raise_for_status()
    data_news = r.json()["articles"][:3]
    news_compact = ""
    for news in data_news:
        news_compact += html.unescape(f"Headline: {news['title']} Brief: {news['description']}")
        news_compact += """
        
        """
    return news_compact


parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": secret.alphavantage_api_key,
}

url = 'https://www.alphavantage.co/query'
r = requests.get(url, params=parameters)
r.raise_for_status()
data = r.json()['Time Series (60min)']
last_datapoint = list(data.keys())[0]
last_values = float(data[last_datapoint]['2. high'])
datetime_object = datetime.strptime(last_datapoint, '%Y-%m-%d %H:%M:%S')
previous_time = str(datetime_object - timedelta(hours=24))
previous_values = float(data[previous_time]['2. high'])
deviation = (last_values - previous_values) / previous_values * 100
if abs(last_values - previous_values) > DEVIATION:
    print("ping")
    news = get_news()
    send_notification(deviation, news)
