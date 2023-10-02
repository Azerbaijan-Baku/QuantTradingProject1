import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the stock symbols
symbols = ['DAL', 'AAL']

# Create empty dictionaries to store cumulative returns
cumulative_returns = {}

# Fetch the stock data from Yahoo Finance for both DAL and AAL
for symbol in symbols:
    data = yf.download(symbol, start="2020-01-01", end="2023-09-30")
    
    # Calculate daily returns
    data['Daily Returns'] = data['Adj Close'].pct_change()

    # Calculate the cumulative returns from the beginning of 2020
    data['Cumulative Returns'] = (1 + data['Daily Returns']).cumprod() - 1

    cumulative_returns[symbol] = data['Cumulative Returns']

# Plot the cumulative returns for both DAL and AAL in one graph
plt.figure(figsize=(12, 6))
for symbol in symbols:
    plt.plot(cumulative_returns[symbol].index, cumulative_returns[symbol] * 100, label=f'{symbol} Cumulative Returns')

plt.title('Cumulative Returns Comparison for DAL and AAL')
plt.xlabel('Date')
plt.ylabel('Cumulative Return (%)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
