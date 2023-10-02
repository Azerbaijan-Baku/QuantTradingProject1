import yfinance as yf
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

# Define the stock symbols
symbols = ['DAL', 'AAL']

# Fetch the stock data from Yahoo Finance starting from January 1, 2008, to October 1, 2023
data = yf.download(symbols, start="2020-01-01", end="2023-10-01")

# Extract the adjusted closing prices for each stock
closing_prices = data['Adj Close']

# Extract the closing prices for DAL and AAL
dal_prices = closing_prices['DAL']
aal_prices = closing_prices['AAL']

# Remove rows with NaN values in either DAL or AAL prices
filtered_data = pd.concat([dal_prices, aal_prices], axis=1)
filtered_data = filtered_data.dropna()

# Extract the filtered prices for DAL and AAL
filtered_dal_prices = filtered_data['DAL']
filtered_aal_prices = filtered_data['AAL']

# Calculate the linear regression on the filtered data
slope, intercept, r_value, p_value, std_err = stats.linregress(filtered_dal_prices, filtered_aal_prices)

# Create a scatter plot of the filtered stock prices
plt.figure(figsize=(10, 6))
plt.scatter(filtered_dal_prices, filtered_aal_prices, label='Stock Prices')

# Create a range of x values for the regression line
x_values = np.linspace(min(filtered_dal_prices), max(filtered_dal_prices), len(filtered_dal_prices))

# Calculate the corresponding y values for the regression line
y_values = intercept + slope * x_values

# Add the regression line to the plot
plt.plot(x_values, y_values, color='red', label='Linear Regression')

plt.title('Linear Regression of DAL and AAL Stock Prices')
plt.xlabel('DAL Stock Price (USD)')
plt.ylabel('AAL Stock Price (USD)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

# Display regression statistics
print(f"Slope: {slope:.4f}")
print(f"Intercept: {intercept:.4f}")
print(f"R-squared: {r_value**2:.4f}")

#해리 마코위츠 Harry Markowitz's modern portfolio Theory (MPT)
#R-Square = 0.8051