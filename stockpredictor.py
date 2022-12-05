import pandas as pd
from prophet import Prophet
import pandas_datareader as web
import datetime as dt

stock_ticker = "AAPL"
start = dt.datetime(2020,1,1 )
end = dt.datetime.now()

data = web.DataReader(stock_ticker, "yahoo", start, end)
data['Date'] = data.index
data= data[["Date", "Close"]]

data.columns = ["ds", "y"]
print(data.head())

prophet = Prophet(daily_seasonality=True) 
prophet.fit(data)

future = prophet.make_future_dataframe(periods=365) # Just makes future data
forecast = prophet.predict(future) # Fills the dataframe rows with predctions

from prophet.plot import plot_plotly
import plotly.offline as py

fig = plot_plotly(prophet, forecast)
py.plot(fig)
