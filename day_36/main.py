import secret
import requests
import pprint
from datetime import datetime, timedelta
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
DEVIATION = 1

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
previous_values = float(data[str(datetime_object-timedelta(hours=24))]['2. high'])
deviation = abs(last_values-previous_values)/max(last_values, previous_values)*100
if abs(last_values-previous_values) > DEVIATION:
    print(f"Gong dev is {deviation}")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

