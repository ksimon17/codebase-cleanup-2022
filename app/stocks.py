print("STOCKS REPORT...")

import os
#from dotenv import load_dotenv #are these necessary now?
from pandas import read_csv

from app.utils import to_usd
from app.alphavantage_service import fetch_stocks_data
#load_dotenv() #are these necessary now?



symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"
# REFACTORED LOGIC 
latest = fetch_stocks_data(symbol)


print(symbol)
print(latest["timestamp"])
print(latest["close"])
print(to_usd(latest["close"]))
