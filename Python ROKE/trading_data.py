import requests
import json
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

months = []
highs = []
lows = []

API_KEY = "PKUWFJ12UTSINTPK"
url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol=BTC&market=GBP&apikey={API_KEY}"

s = requests.get(url)
j = s.content.decode("utf-8")
myjson = json.loads(j)
print(myjson)

for month in myjson["Time Series (Digital Currency Monthly)"]:
    months.append(str(month))

print(months)

for m in months:
    print(m)
    print("high:")
    month = myjson["Time Series (Digital Currency Monthly)"][m]["2a. high (GBP)"]
    highs.append(month)
    print(month)
    print()
    print("low:")
    month = myjson["Time Series (Digital Currency Monthly)"][m]["3a. low (GBP)"]
    lows.append(month)
    print(month)
    print()

connection = sqlite3.connect("trading_data.db")
cur = connection.cursor()

s = "create table if not exists prices (btcDate text, btcHigh real, btcLow real)"
cur.execute(s)

alldata = zip(months, highs, lows)
cur.executemany("insert into prices values (?, ?, ?)", alldata)

s = "select btcDate, btcHigh from prices where btcHigh = (select max(btcHigh) from prices)"
cur.execute(s)
rs = cur.fetchall()
print(f"The high price was {rs[0][1]} on {rs[0][0]}")
s = "select btcDate, btcLow from prices where btcLow = (select min(btcLow) from prices)"
cur.execute(s)
rs = cur.fetchall()
print(f"The low price was {rs[0][1]} on {rs[0][0]}")

# extract high price per month

s = "select btcDate, btcHigh from prices"
cur.execute(s)
graphdata = cur.fetchall()
graphdata.reverse()

graphmonths = []
graphvalues = []

for t in graphdata:
    graphmonths.append(t[0])
    graphvalues.append(t[1])

plt.plot(graphmonths, graphvalues)
plt.figure()
plt.xlabel("Months")
plt.ylabel("Price (GBP)")
plt.title("Monthly high Bitcoin price (GDP) over time")
plt.show()

#for month in months:
    #insert stuff



connection.close()
