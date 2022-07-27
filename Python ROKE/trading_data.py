import requests
import json
import sqlite3
import matplotlib

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

for my_month in months:
    s = f"insert into prices(btcDate) values ({my_month})"
    cur.execute(s)

for low in lows:
    s = f"insert into prices(btcLow) values ({low})"
    cur.execute(s)

for high in highs:
    s = f"insert into prices(btcHigh) values ({high})"
    cur.execute(s)

s = "select btcDate, btcHigh from prices where btcHigh = (select max(btcHigh) from prices)"
cur.execute(s)
rs = cur.fetchall()
print(rs)
s = "select btcDate, btcLow from prices where btcLow = (select min(btcLow) from prices)"
cur.execute(s)
rs = cur.fetchall()
print(rs)
# extract high price per month



#for month in months:
    #insert stuff



connection.close()