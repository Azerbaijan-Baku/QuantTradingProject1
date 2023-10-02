import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbols
symbols = ['DAL', 'AAL']

# Fetch the stock data from Yahoo Finance
data = yf.download(symbols, start="2013-01-01", end="2023-01-01")

# Extract the closing prices for each stock
closing_prices = data['Adj Close']

# Plot the closing prices
plt.figure(figsize=(10, 6))
for symbol in symbols:
    plt.plot(closing_prices.index, closing_prices[symbol], label=symbol)

plt.title('Delta Airlines and American Airlines Closing Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
