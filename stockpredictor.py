import pandas as pd
from prophet import Prophet
import pandas_datareader as web
import datetime as dt
import streamlit as st

stock_ticker = st.text_input("Enter ticker", "AAPL")
if stock_ticker == "":
    stock_ticker = "AAPL"
start = dt.datetime(2020,1,1 )
end = dt.datetime.now()
period = st.slider("Days to predict", 30, 730, 365, 1)

data = web.DataReader(stock_ticker, "yahoo", start, end)
data['Date'] = data.index
data= data[["Date", "Close"]]

data.columns = ["ds", "y"]
print(data.head())

prophet = Prophet(daily_seasonality=True) 
prophet.fit(data)

future = prophet.make_future_dataframe(periods=period) # Just makes future data
forecast = prophet.predict(future) # Fills the dataframe rows with predctions
st.title(f"Stock Predictor for {stock_ticker}")
st.subheader("Forecast")
st.line_chart(forecast['trend'])
# from prophet.plot import plot_plotly
# import plotly.offline as py

# fig = plot_plotly(prophet, forecast)
# py.plot(fig)
