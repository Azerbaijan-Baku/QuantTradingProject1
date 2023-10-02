import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the stock symbol
symbol = 'DAL'

# Fetch the stock data from Yahoo Finance for DAL
data = yf.download(symbol, start="2020-01-01", end="2023-01-01")

# Calculate daily returns
data['Daily Returns'] = data['Adj Close'].pct_change()

# Calculate cumulative returns as a percentage change from the starting point
data['Cumulative Returns'] = (1 + data['Daily Returns']).cumprod() - 1

# Calculate the starting point for the cumulative return calculation
start_price = data['Adj Close'].iloc[0]

# Calculate the cumulative return as a percentage change from the starting point
data['Cumulative Returns'] = ((data['Adj Close'] / start_price) - 1) * 100

# Plot the cumulative return for DAL
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Cumulative Returns'], label=f'{symbol} Cumulative Returns', color='blue')

plt.title(f'Cumulative Returns for {symbol}')
plt.xlabel('Date')
plt.ylabel('Cumulative Return (%)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
