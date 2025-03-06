from datetime import datetime
from dotenv import load_dotenv
import os
import pytz
import requests

import pandas as pd 

localpath = os.getenv('LOCAL_PATH')

#USD,AUD,JPY etc..
from_currency = 'USD'
to_currency   = 'AUD'
api_key       = os.getenv('API_KEY')

try:
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()

    df = pd.DataFrame.from_dict(data['Realtime Currency Exchange Rate'], orient='index', columns=['value'])

    # Reset index to move the index into a column
    df = df.reset_index()

    # Rename columns
    df.columns = ['headers', 'value']

    #save to local to test other transformations
    df.to_pickle(f'df.pkl')    

    print("Success")
except:
    print("ERROR with API call, data not returned")



