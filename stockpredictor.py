import pandas as pd
from prophet import Prophet

data = pd.read_csv("stockdata.csv")
data= data[["Date", "Close"]]

data.columns = ["ds", "y"]

prophet = Prophet(daily_seasonality=True) 
prophet.fit(data)

future = prophet.make_future_dataframe(periods=365) # Just makes future data
forecast = prophet.predict(future) # Fills the dataframe rows with predctions

from prophet.plot import plot_plotly
import plotly.offline as py

fig = plot_plotly(prophet, forecast)
py.plot(fig)
