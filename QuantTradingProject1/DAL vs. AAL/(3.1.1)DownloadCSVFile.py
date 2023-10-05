import yfinance as yf
import pandas as pd

# Define the stock symbols
symbols = ['DAL', 'AAL']

# Define the start and end dates
start_date = "2020-01-01"
end_date = "2023-10-01"

# Create an empty DataFrame to store the data
data = pd.DataFrame()

# Fetch the stock data from Yahoo Finance for both DAL and AAL
for symbol in symbols:
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    if not stock_data.empty:
        data[symbol] = stock_data['Adj Close']
        
        # Calculate the daily percentage change and add it as a new column
        data[f'{symbol}_Change_Pct'] = stock_data['Adj Close'].pct_change() * 100
        
        data[symbol].to_csv(f"{symbol}_stock_prices.csv")
        print(f"Stock price data for {symbol} from {start_date} to {end_date} saved to {symbol}_stock_prices.csv")
    else:
        print(f"No data available for {symbol} in the specified date range.")

# Optionally, you can save the entire DataFrame to a single CSV file if needed
data.to_csv("DAL_AAL_stock_prices.csv")
