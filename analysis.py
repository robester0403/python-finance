import requests
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
import pandas as pd


load_dotenv(".env")

API_KEY = os.getenv('API_KEY')

company = "IBM"
years = 30

income_statement = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}&apikey={API_KEY}").json()

print(income_statement)
# next step, use pandas to get take JSON object and maake it into a dataframe

# assign to revenues an array of the revenues from the income statement
# use the for loop to itrate over the length of the income statement array  
# revenues = list(reversed([ income_statement[i]['revenue'] for i in range(len(income_statement))]))
# profits = list(reversed([income_statement[i]['grossProfit'] for i in range(len(income_statement))]))

# plt.plot(revenues, label="revenues")
# plt.plot(profits, label="profits")
# plt.title(f"{company} revenues and profits")
# plt.legend(loc="upper left")
# plt.show()

# income_statementcsv = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?datatype=csv&limit={years}&apikey={API_KEY}")

# with open("income_statement.csv", "wb") as f:
#     f.write(income_statementcsv.content)