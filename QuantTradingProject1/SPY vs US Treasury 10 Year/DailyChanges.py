import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker symbols and date range
spy_ticker = "SPY"
tnx_ticker = "^TNX"
start_date = "2000-01-01"
end_date = "2023-10-01"

# Download historical data
spy_data = yf.download(spy_ticker, start=start_date, end=end_date)
tnx_data = yf.download(tnx_ticker, start=start_date, end=end_date)

# Calculate daily returns for SPY and Treasury Yield
spy_returns = spy_data['Close'].pct_change()
tnx_returns = tnx_data['Close'].pct_change()

# Create a single graph to compare daily returns
plt.figure(figsize=(12, 6))

# Plot daily returns for SPY
plt.plot(spy_returns.index, spy_returns, label='SPY Daily Returns', color='blue')

# Plot daily returns for 10-Year Treasury Yield (scaled for visibility)
plt.plot(tnx_returns.index, tnx_returns * 1000, label='10-Year Treasury Yield Daily Returns (scaled)', color='green')

plt.title('Daily Returns Comparison: SPY vs. 10-Year Treasury Yield (2000-2023)')
plt.xlabel('Date')
plt.ylabel('Daily Returns')
plt.legend()
plt.grid(True)
plt.show()
