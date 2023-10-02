import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the stock symbols
symbols = ['DAL', 'AAL']

# Fetch the stock data from Yahoo Finance for both DAL and AAL
data = yf.download(symbols, start="2020-01-01", end="2023-09-30")

# Extract the adjusted closing prices for both symbols
closing_prices = data['Adj Close']

# Calculate the price ratio (DAL/AAL)
price_ratio = closing_prices[symbols[0]] / closing_prices[symbols[1]]

# Calculate the 60-day moving average
price_ratio_ma = price_ratio.rolling(window=60).mean()

# Interpolate the missing data points in the moving average
price_ratio_ma = price_ratio_ma.interpolate()

# Plot the price ratio with the 60-day moving average
plt.figure(figsize=(12, 6))
plt.plot(price_ratio.index, price_ratio, label='Price Ratio (DAL/AAL)', color='blue', alpha=0.7)
plt.plot(price_ratio_ma.index, price_ratio_ma, label='60-Day Moving Average', color='red')

plt.title('Price Ratio (DAL/AAL) with 60-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price Ratio')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
