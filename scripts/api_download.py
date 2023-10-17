# pip install yfinance
import yfinance as yf

import requests
from datetime import datetime
import pandas as pd

# Define a start date and End Date
start = '2021-01-01'
#setting today date as End Date
end = datetime.today().strftime('%Y-%m-%d')

# get historical market data
Apple_stock_price = yf.download(tickers="AAPL", start= start , end = end)

print(Apple_stock_price)

