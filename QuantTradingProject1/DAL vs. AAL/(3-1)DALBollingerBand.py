import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the stock symbol
symbol = 'DAL'

# Fetch the stock data from Yahoo Finance
data = yf.download(symbol, start="2020-01-01", end="2023-01-01")

# Calculate the 20-day moving average
data['SMA'] = data['Adj Close'].rolling(window=20).mean()

# Calculate the rolling standard deviation for 20 days
data['std'] = data['Adj Close'].rolling(window=20).std()

# Calculate the upper and lower Bollinger Bands
data['Upper'] = data['SMA'] + (data['std'] * 2)
data['Lower'] = data['SMA'] - (data['std'] * 2)

# Plot the stock prices and Bollinger Bands
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Adj Close'], label=symbol + ' Close Price', color='blue')
plt.plot(data.index, data['SMA'], label='20-Day SMA', color='orange', linestyle='--')
plt.plot(data.index, data['Upper'], label='Upper Bollinger Band', color='red', linestyle='--')
plt.plot(data.index, data['Lower'], label='Lower Bollinger Band', color='green', linestyle='--')

plt.title('Bollinger Bands for ' + symbol)
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
