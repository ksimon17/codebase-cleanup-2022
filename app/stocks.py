print("STOCKS REPORT...")

import os
from dotenv import load_dotenv #are these necessary now?
from pandas import read_csv

from app.utils import to_usd
from app.alphavantage_service import fetch_stocks_data
load_dotenv() #are these necessary now?

#ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"

# ORIGINAL LOGIC
# url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"

# df = read_csv(url)
# #print(df.columns)
# #breakpoint()

# latest = df.iloc[0]

# REFACTORED LOGIC 
latest = fetch_stocks_data(symbol)


print(symbol)
print(latest["timestamp"])
print(latest["close"])
print(to_usd(latest["close"]))
