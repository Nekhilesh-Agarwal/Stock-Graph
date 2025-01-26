import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime, timedelta
import numpy as np

# Function to identify peaks in the data using NumPy
def find_peaks(data):
    return np.where((data[1:-1] > data[:-2]) & (data[1:-1] > data[2:]))[0] + 1

# Ask the user for the stock symbol
symbol = input("Enter the stock symbol (e.g., GOOG for Google shares): ")

# Initialize the ticker object
ticker = yf.Ticker(symbol)

# Get today's date
today = datetime.today().strftime('%Y-%m-%d')

# Get the date for one year ago
one_year_ago = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')

# Fetch historical data for the past year
historical_data_df = ticker.history(start=one_year_ago, end=today, interval='1d')
historical_close = historical_data_df['Close'].to_numpy()

# Find peaks in historical closing prices
peaks = find_peaks(historical_close)

# Create a figure for the plot with a black background
fig, ax = plt.subplots(figsize=(12, 6), facecolor='black')

# Store the previous intraday price (initially None)
previous_intraday_price = None

# Function to fetch and plot both historical and live intraday data
def fetch_and_plot(i):
    global previous_intraday_price  # Track the previous intraday price

    # Fetch live intraday data for today with 1-minute intervals
    intraday_data_df = ticker.history(period="1d", interval="1m")

    # Check if intraday data is available and non-empty
    if intraday_data_df.empty:
        print(f"No intraday data available for {symbol}.")
        return

    # Get the current price from the latest intraday data
    current_price = intraday_data_df['Close'].iloc[-1]

    # Calculate the price change from the previous value
    if previous_intraday_price is not None:
        price_change = current_price - previous_intraday_price
        percentage_change = (price_change / previous_intraday_price) * 100
    else:
        # No previous value (first run), so no change to display
        price_change = 0.0
        percentage_change = 0.0

    # Update the previous intraday price for the next iteration
    previous_intraday_price = current_price

    # Print the current price and the change in the console
    print(f"Current Price: {current_price:.2f} INR")
    print(f"Change: {price_change:.2f} INR ({percentage_change:.2f}%)\n")

    # Clear the previous plot to avoid overlap
    ax.cla()

    # Plot historical data (1 year) with area under the curve filled in green
    ax.fill_between(historical_data_df.index, historical_data_df['Close'],
                    color='green', alpha=0.5, label='Historical (1 Year)')

    # Plot live intraday data (today) with a blue line
    ax.plot(intraday_data_df.index, intraday_data_df['Close'], 
            color='blue', label='Intraday (Today)')

    # Highlight peaks with small white dots
    peak_dates = historical_data_df.index[peaks]
    peak_prices = historical_data_df['Close'].values[peaks]
    ax.scatter(peak_dates, peak_prices, color='white', s=10, zorder=5)  # Larger dots

    # Set plot title and labels with white text
    ax.set_title(f'{symbol} Stock Price (Intraday + Historical)', color='white')
    ax.set_xlabel('Date/Time', color='white')
    ax.set_ylabel('Price (INR)', color='white')

    # Customize grid and appearance
    ax.grid(color='dimgray', linestyle=':', linewidth=0.5, alpha=0.7)
    ax.set_facecolor('black')  # Set background color to black
    ax.tick_params(colors='white')  # Set tick colors to white
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    plt.xticks(color='white')  # X-axis ticks color
    plt.yticks(color='white')  # Y-axis ticks color

    # Adjust axis limits to fit the data
    ax.set_xlim(left=historical_data_df.index[0], right=intraday_data_df.index[-1])
    ax.set_ylim(bottom=min(historical_data_df['Close'].min(), 
                           intraday_data_df['Close'].min()) - 5,
                top=max(historical_data_df['Close'].max(), 
                        intraday_data_df['Close'].max()) + 5)

    # Adjust margins to prevent cutoff
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)

# Set up animation for live updates every 10 seconds
ani = FuncAnimation(fig, fetch_and_plot, interval=10000)  # 10000 ms = 10 sec

# Display the live-updating plot
plt.tight_layout()
plt.show()