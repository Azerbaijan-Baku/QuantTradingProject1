import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the stock symbols
symbols = ['DAL', 'AAL']

# Fetch the stock data from Yahoo Finance for both DAL and AAL
data = yf.download(symbols, start="2020-01-01", end="2023-10-01")

# Extract the adjusted closing prices for both symbols
closing_prices = data['Adj Close']

# Calculate the correlation between the two stock prices
correlation = closing_prices[symbols[0]].corr(closing_prices[symbols[1]])

# Create a scatter plot to visualize the relationship
plt.figure(figsize=(6, 6))
plt.scatter(closing_prices[symbols[0]], closing_prices[symbols[1]], alpha=0.5)
plt.title('Scatter Plot of DAL and AAL Stock Prices')
plt.xlabel('DAL Stock Price')
plt.ylabel('AAL Stock Price')

# Show the correlation coefficient
plt.annotate(f'Correlation: {correlation:.2f}', xy=(0.1, 0.9), xycoords='axes fraction', fontsize=12)

# Show the plot
plt.grid(True)
plt.show()

# Print the calculated correlation coefficient
print(f'Correlation between DAL and AAL stock prices: {correlation:.2f}')

#Correlation = 0.90