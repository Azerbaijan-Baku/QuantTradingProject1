import yfinance as yf

# Define the stock symbols
symbols = ['DAL', 'AAL']

# Create empty dictionary to store market caps
market_caps = {}

# Fetch summary data for each symbol
for symbol in symbols:
    ticker = yf.Ticker(symbol)
    info = ticker.info
    
    # Extract the market capitalization if available
    if 'marketCap' in info:
        market_caps[symbol] = info['marketCap']

# Print the market capitalization for each symbol
for symbol, market_cap in market_caps.items():
    print(f'{symbol} Market Cap: {market_cap}')

    #AAL = 8.6 billion, DAL = 23.8 billion (in USD)
