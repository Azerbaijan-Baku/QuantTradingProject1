import yfinance as yf
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import coint

def get_data(tickers, start, end):
	stock_data = yf.download(tickers, start=start, end=end)['Adj Close']
	return stock_data

def find_cointegrated_pairs(data):
	n = data.shape[1]
	score_matrix = np.zeros((n, n))
	pvalue_matrix = np.ones((n, n))
	keys = data.keys()
	pairs = []
	for i in range(n):
		for j in range(i+1, n):
			stock1 = data[keys[i]]
			stock2 = data[keys[j]]
			result = coint(stock1, stock2)
			score = result[0]
			pvalue = result[1]
			score_matrix[i, j] = score
			pvalue_matrix[i, j] = pvalue
			if pvalue < 0.05:
				pairs.append((keys[i], keys[j], score, pvalue))
	return score_matrix, pvalue_matrix, pairs

def get_expected_return(stock_returns, market_returns, risk_free_rate):
	beta = np.cov(stock_returns, market_returns)[0][1] / np.var(market_returns)
	expected_return = risk_free_rate + beta * (np.mean(market_returns) - risk_free_rate)
	return expected_return


payload=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
gics = payload[0]
tickers = list(gics['Symbol'])

start = '2023-01-01'
end = '2023-10-01'
risk_free_rate = 0.01  # assume a risk-free rate of 1% for simplicity

tickers.remove('BRK.B')
tickers.remove('BF.B')
tickers.append('^GSPC')

stock_data = get_data(tickers, start, end)
stock_data = stock_data.dropna()
print(stock_data)
if stock_data.shape[0] < 2:
	raise ValueError("Insufficient data points!")

returns_data = stock_data.pct_change().dropna()

# Calculate expected returns using CAPM for each stock relative to the market (S&P 500)
market_returns = returns_data['^GSPC']
expected_returns = {}
for ticker in tickers[:-1]:  # excluding S&P 500
	stock_returns = returns_data[ticker]
	expected_return = get_expected_return(stock_returns, market_returns, risk_free_rate)
	expected_returns[ticker] = expected_return

scores, pvalues, pairs = find_cointegrated_pairs(returns_data.drop('^GSPC', axis=1))  # exclude market index for pair finding

right_stocks = set()
for pair in pairs:
	right_stocks.add(pair[0])
	right_stocks.add(pair[1])

wrong_stocks = [ticker for ticker in tickers[:-1] if ticker not in right_stocks]  # excluding S&P 500

# Display results
print("\nCointegrated Pairs with their scores and p-values:")
for pair in pairs:
	print(f"Stock 1: {pair[0]}, Stock 2: {pair[1]}, Score: {pair[2]:.2f}, P-value: {pair[3]:.5f}")

print("\nExpected Returns using CAPM:")
for ticker, expected_return in expected_returns.items():
	print(f"{ticker}: {expected_return*100:.2f}%")

print("\nRight Stocks (Cointegrated with at least one other stock):")
print(right_stocks)

print("\nWrong Stocks (Not cointegrated with any other stock):")
print(wrong_stocks)
