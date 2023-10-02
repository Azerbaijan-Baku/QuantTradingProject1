import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbols
symbols = ['DAL', 'AAL']

# Fetch the stock data from Yahoo Finance starting from January 1, 2000, to October 1, 2023
data = yf.download(symbols, start="2013-01-01", end="2023-01-01")

# Extract the adjusted closing prices for each stock
closing_prices = data['Adj Close']

# Index the closing prices to start at 100 on January 1, 2000
indexed_prices = (closing_prices / closing_prices.iloc[0] * 100)

# Plot the indexed closing prices
plt.figure(figsize=(10, 6))
for symbol in symbols:
    plt.plot(indexed_prices.index, indexed_prices[symbol], label=symbol)

plt.title('Indexed Comparison of Delta Airlines and American Airlines (Since Jan 1, 2013)')
plt.xlabel('Date')
plt.ylabel('Indexed Price (Start at 100)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
