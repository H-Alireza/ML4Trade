import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Fetch financial data
symbol = 'AAPL'  # Replace with the symbol of the stock you want to analyze
start_date = '2022-05-01'  # Replace with your desired start date
end_date = '2023-01-31'  # Replace with your desired end date

# Fetch financial data using yfinance
df = yf.download(symbol, start=start_date, end=end_date)

# Set parameters
min_touches = 2  # Minimum number of touches to consider a level as support/resistance
bounce_tolerance = 0.01  # Tolerance for considering a bounce, expressed as a percentage

# Find support and resistance levels
support_levels = []
resistance_levels = []

for i in range(len(df)):
    price = df['Close'][i]
    for level in support_levels:
        if abs(price - level) / level <= bounce_tolerance:
            support_levels.remove(level)
            support_levels.append(price)
            break
    else:
        support_levels.append(price)
    for level in resistance_levels:
        if abs(price - level) / level <= bounce_tolerance:
            resistance_levels.remove(level)
            resistance_levels.append(price)
            break
    else:
        resistance_levels.append(price)

# Filter support and resistance levels based on number of touches
support_levels = [level for level in support_levels if str(level) in df['Low'].astype(str).values]
resistance_levels = [level for level in resistance_levels if str(level) in df['High'].astype(str).values]

# Print support and resistance levels
print('Support levels:', support_levels)
print('Resistance levels:', resistance_levels)

# Plot chart with support and resistance levels
plt.figure(figsize=(12, 6))
plt.plot(df['Close'])
for level in support_levels:
    plt.axhline(level, color='green', linestyle='--', label='Support')
for level in resistance_levels:
    plt.axhline(level, color='red', linestyle='--', label='Resistance')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Financial Chart with Support and Resistance Levels')
plt.show()
