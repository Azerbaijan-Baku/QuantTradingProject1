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

# Create a single graph with dual y-axes for comparison
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot SPY closing prices on the left y-axis
ax1.plot(spy_data.index, spy_data['Close'], label='SPY Close Price', color='blue')
ax1.set_xlabel('Date')
ax1.set_ylabel('SPY Price', color='blue')
ax1.legend(loc='upper left')
ax1.grid(True)

# Create a secondary y-axis for 10-Year Treasury Yield on the right
ax2 = ax1.twinx()
ax2.plot(tnx_data.index, tnx_data['Close'], label='10-Year Treasury Yield', color='green')
ax2.set_ylabel('Yield (%)', color='green')
ax2.legend(loc='upper right')

# Title and legend for the entire graph
plt.title('SPY ETF vs. 10-Year U.S. Treasury Yield (2000-2023)')

# Adjust layout
plt.tight_layout()
plt.show()

