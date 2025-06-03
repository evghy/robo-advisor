import os, requests, pandas as pd
from datetime import datetime, timedelta

API_KEY = os.getenv("NEWSAPI_KEY")          # set this once in the terminal
TICKERS = ["AAPL","MSFT","GOOG","AMZN","NVDA",
           "TSLA","META","JPM","V","NFLX"]
YDAY = (datetime.utcnow() - timedelta(days=1)).strftime("%Y-%m-%d")

rows = []
for t in TICKERS:
    url = ("https://newsapi.org/v2/everything?"
           f"q={t}&from={YDAY}&sortBy=publishedAt&pageSize=100&apiKey={API_KEY}")
    for art in requests.get(url).json().get("articles", []):
        rows.append({"ticker": t,
                     "time":   art["publishedAt"][:10],
                     "title":  art["title"]})

news = pd.DataFrame(rows)
os.makedirs("data", exist_ok=True)
news.to_csv("data/news_raw.csv", index=False)
print("saved", news.shape, "rows to data/news_raw.csv")

