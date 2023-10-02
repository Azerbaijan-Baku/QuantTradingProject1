import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the stock symbols
symbols = ['DAL', 'AAL']

# Fetch the stock data from Yahoo Finance for both DAL and AAL
data = yf.download(symbols, start="2020-01-01", end="2023-09-30")

# Extract the adjusted closing prices for both symbols
closing_prices = data['Adj Close']

# Calculate the indexed prices for both symbols
indexed_prices = (closing_prices / closing_prices.iloc[0] * 100)

# Calculate the ratio of indexed prices (DAL/AAL)
indexed_ratio = indexed_prices[symbols[0]] / indexed_prices[symbols[1]]

# Plot the indexed ratio
plt.figure(figsize=(12, 6))
plt.plot(indexed_ratio.index, indexed_ratio, label='Indexed Ratio (DAL/AAL)', color='blue')

plt.title('Indexed Ratio of DAL to AAL')
plt.xlabel('Date')
plt.ylabel('Indexed Ratio')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
