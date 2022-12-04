import pandas_datareader as web
import datetime as dt

start = dt.datetime(2020,1,1 )
end = dt.datetime.now()

data = web.DataReader("AAPL", "yahoo", start, end)

data.to_csv("stockdata.csv")
