import sqlite3
import pandas as pd

conn = sqlite3.connect("mydb.db")

# allows us to query the database
cur = conn.cursor()

#
cur.execute("""
CREATE TABLE IF NOT EXISTS stocks (
  ssn INTEGER PRIMARY KEY,
  name varchar(255) NOT NULL,
  ticker varchar(20) NOT NULL
)""")

# cur.execute("""
# INSERT INTO stocks (ssn,name,ticker) VALUES
# (1, "Apple Inc", "AAPL"),
# (2, "Microsoft", "MSFT"),
# (3, "Tesla", "TSLA"),
# (4, "Nvidia", "NVDA"),
# (5, "Facebook", "FB")
# """)

conn.commit()

# have to specify the connection you want to run the query on
sql = pd.read_sql_query("Select * FROM stocks", conn)
df = pd.DataFrame(sql, columns=["ssn", "name", "ticker"])


new_df = pd.DataFrame({
  "ssn": [6,7,8],
  "name": ["Google", "Amazon", "Intel"],
  "ticker": ["GOOG", "AMZN", "INTC"]
})

new_df.to_sql("stocks", conn, if_exists="append", index=False)

print(df)
