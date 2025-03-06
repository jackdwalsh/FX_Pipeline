from datetime import datetime
from dotenv import load_dotenv
import os
import pytz
import requests

#USD,AUD,JPY etc..
from_currency = 'USD'
to_currency   = 'AUD'
api_key       = os.getenv('API_KEY')

url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={api_key}'
r = requests.get(url)
data = r.json()

print(data)

for key,value in data['Realtime Currency Exchange Rate'].items():
    print(key,value)
    
#L1PGZ06KNN5L1GC5