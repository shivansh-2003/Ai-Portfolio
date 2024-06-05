import requests
import time
import pandas as pd



api_key = 'GU9UK7T99ENBOJ1H'
base_url = 'https://www.alphavantage.co/query'


symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB']  # stock ki symbols hai use fetch karne ke liye


def fetch_stock_data(symbol):
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if 'Time Series (Daily)' in data:
        df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
        df = df.rename(columns=lambda x: x.split(' ')[1])
        df['symbol'] = symbol
        return df
    else:
        return pd.DataFrame()


all_stock_data = pd.DataFrame()


for symbol in symbols:
    stock_data = fetch_stock_data(symbol)
    all_stock_data = all_stock_data._append(stock_data)
    time.sleep(12) # 12 second ka gap diya hai taki jyada request na jaye

    
# dal do data ko csv file me
all_stock_data.to_csv('stock_data.csv', index=False)
print(all_stock_data.head())
