import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker symbols and date range
spy_ticker = "SPY"
tnx_ticker = "^TNX"
start_date = "2000-01-01"
end_date = "2023-10-01"

# Download historical data for SPY and Treasury Yield
spy_data = yf.download(spy_ticker, start=start_date, end=end_date)
tnx_data = yf.download(tnx_ticker, start=start_date, end=end_date)

# Extract the closing prices for both SPY and Treasury Yield
spy_close = spy_data['Close']
tnx_close = tnx_data['Close']

# Calculate the cumulative sum of closing prices for both assets
cumulative_sum_spy = spy_close.cumsum()
cumulative_sum_tnx = tnx_close.cumsum()

# Create a single graph to compare the cumulative sum of closing prices
plt.figure(figsize=(12, 6))

# Plot cumulative sum of closing prices for SPY
plt.plot(cumulative_sum_spy.index, cumulative_sum_spy, label='Cumulative Sum of SPY Closing Prices', color='blue')

# Plot cumulative sum of closing prices for 10-Year Treasury Yield
plt.plot(cumulative_sum_tnx.index, cumulative_sum_tnx, label='Cumulative Sum of 10-Year Treasury Yield Closing Prices', color='green')

plt.title('Cumulative Sum of Closing Prices: SPY vs. 10-Year Treasury Yield (2000-2023)')
plt.xlabel('Date')
plt.ylabel('Cumulative Sum of Closing Prices')
plt.legend()
plt.grid(True)
plt.show()
