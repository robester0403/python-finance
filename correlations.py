import pandas_datareader as web
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

# seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
# pandas-datareader is a Python package that allows you to get data from various Internet sources into a pandas DataFrame. It is a very useful tool for data analysis and data science.
# works with dataframes

# timeframe for analysis
start = dt.datetime(2008,1,1)
end = dt.datetime.now()

tickers = ["FB", "GS", "NVDA", "MSFT", "TSLA", "AAPL", "CCL", "BA"]
colnames = []

# The pandas-datareader module is specifically designed to interface with some of the world's most popular financial data APIs, and import their data into an easily digestible pandas

for ticker in tickers:
  data = web.DataReader(ticker, "yahoo", start, end)
  # below is for if no dataframe exists
  if len(colnames) == 0:
    # We use COPY because we don't want just a reference to the data, we want a copy of the data
    # Combined is the object we are creating and manipluating
    combined = data[ ['Adj Close'] ].copy()
    colnames.append(ticker)
    combined.columns = colnames
  else:
    # for if you have a dataframe
    combined = combined.join(data['Adj Close'])
    colnames.append(ticker)
    combined.columns = colnames


for ticker in tickers:
  plt.plot(combined[ticker], label=ticker)

plt.legend(loc="upper left")
plt.title("Adjusted Close Price of Stocks")
plt.show()