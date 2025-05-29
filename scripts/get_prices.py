import os, yfinance as yf, pandas as pd
from datetime import datetime

TICKERS = ["AAPL","MSFT","GOOG","AMZN","NVDA","TSLA","META","JPM","V","NFLX"]
START, END = "2015-01-01", datetime.today().strftime("%Y-%m-%d")

frames = []
for t in TICKERS:
    s = yf.download(t, start=START, end=END, progress=False)["Close"].copy()
    s.name = t
    frames.append(s)

prices = pd.concat(frames, axis=1).dropna(how="all")
os.makedirs("data", exist_ok=True)
prices.to_csv("data/prices.csv")
print("Saved", prices.shape, "to data/prices.csv")
