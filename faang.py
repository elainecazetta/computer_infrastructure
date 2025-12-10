#! usr/bin/env python

# Dates and times
import datetime as dt

# Yahoo Finance data
import yfinance as yf

# Download FAANG stocks data:
df = yf.download(['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG'], period='5d', interval='1h')

# Current date and time
now = dt.datetime.now()

# File name
filename = "data/" + now.strftime("%Y%m%d-%H%M%S") + ".csv"

# Save data as CSV
# Resources: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
df.to_csv(filename)

# Plotting the closing prices for all stocks
df['Close'].plot()