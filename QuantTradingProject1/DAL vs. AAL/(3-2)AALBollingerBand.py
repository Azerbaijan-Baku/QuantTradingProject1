import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the stock symbol
symbol = 'AAL'

# Fetch the stock data from Yahoo Finance for AAL
data = yf.download(symbol, start="2020-01-01", end="2023-01-01")

# Calculate the 20-day Simple Moving Average (SMA)
data['SMA'] = data['Adj Close'].rolling(window=20).mean()

# Calculate the rolling standard deviation for 20 days
data['std'] = data['Adj Close'].rolling(window=20).std()

# Calculate the upper and lower Bollinger Bands
data['Upper'] = data['SMA'] + (data['std'] * 2)
data['Lower'] = data['SMA'] - (data['std'] * 2)

# Plot the stock prices and Bollinger Bands for AAL
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Adj Close'], label=f'{symbol} Close Price')
plt.plot(data.index, data['SMA'], label=f'{symbol} 20-Day SMA', linestyle='--')
plt.plot(data.index, data['Upper'], label=f'{symbol} Upper Bollinger Band', linestyle='--')
plt.plot(data.index, data['Lower'], label=f'{symbol} Lower Bollinger Band', linestyle='--')

plt.title(f'Bollinger Bands for {symbol}')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
