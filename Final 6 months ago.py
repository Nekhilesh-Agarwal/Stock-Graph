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

# Get the date for six months ago
six_months_ago = (datetime.today() - timedelta(days=182)).strftime('%Y-%m-%d')

# Fetch historical data for the past 6 months once
historical_data_df = ticker.history(start=six_months_ago, end=today, interval='1d')
historical_close = historical_data_df['Close'].to_numpy()

# Find peaks in historical closing prices
peaks = find_peaks(historical_close)

# Create a figure for the plot with black background
fig, ax = plt.subplots(figsize=(12, 6), facecolor='black')

# Variable to store the previous closing price
previous_close = None

# Function to fetch and plot both historical and live intraday data
def fetch_and_plot(i):
    global previous_close  # Use the global variable to track the previous closing price

    # Fetch live intraday data for today with 1-minute intervals
    intraday_data_df = ticker.history(period="1d", interval="1m")

    # Check if the intraday data is available
    if intraday_data_df.empty:
        print(f"No intraday data available for {symbol}.")
        return
 # Get the current price (last closing price in intraday data)
    current_price = intraday_data_df['Close'].iloc[-1]

    # Calculate the price change based on the last closing price from historical data
    previous_close = historical_close[-1]
    price_change = current_price - previous_close
    percentage_change = (price_change / previous_close) * 100

    # Print the current price and the price change in the console
    print(f"Current Price: {current_price:.2f} INR")
    print(f"Change: {price_change:.2f} INR ({percentage_change:.2f}%)\n")

    # Clear only the relevant parts of the plot to prevent overlap
    ax.cla()  # Clear the axes

    # Plot historical data (past 6 months) with area under the curve filled in green
    ax.fill_between(historical_data_df.index, historical_data_df['Close'], color='green', alpha=0.5, label='Historical (6 Months)')
    
    # Plot live intraday data (today) with a blue line
    ax.plot(intraday_data_df.index, intraday_data_df['Close'], color='blue', label='Intraday (Today)')

    # Plot small white dots at the peaks of historical data
    peak_dates = historical_data_df.index[peaks]
    peak_prices = historical_data_df['Close'].values[peaks]
    ax.scatter(peak_dates, peak_prices, color='white', s=0.2, zorder=5)  # Small white dots at peaks

    # Set plot title and labels with white text
    ax.set_title(f'{symbol} Stock Price (Intraday + Historical)', color='white')
    ax.set_xlabel('Date/Time', color='white')
    ax.set_ylabel('Price (INR)', color='white')

    # Customize the grid to be darker
    ax.grid(color='dimgray', linestyle=':', linewidth=0.5, alpha=0.7)  # Set color to 'dimgray' for a darker grid
    
    # Set background and text color
    ax.set_facecolor('black')  # Background color
    ax.tick_params(colors='white')  # Tick colors
    ax.xaxis.label.set_color('white')  # X-axis label color
    ax.yaxis.label.set_color('white')  # Y-axis label color
    plt.xticks(color='white')  # X-axis ticks color
    plt.yticks(color='white')  # Y-axis ticks color

    # Adjust x and y axis limits and margins to ensure text is visible
    ax.set_xlim(left=historical_data_df.index[0], right=intraday_data_df.index[-1])  # X-axis limits
    ax.set_ylim(bottom=min(historical_data_df['Close'].min(), intraday_data_df['Close'].min()) - 5, 
                         top=max(historical_data_df['Close'].max(), intraday_data_df['Close'].max()) + 5)  # Y-axis limits
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)  # Adjust margins to prevent cutoff

# Set up animation for live updates every 10 seconds
ani = FuncAnimation(fig, fetch_and_plot, interval=10000)  # 10000 ms = 10 sec

# Display the live-updating plot
plt.tight_layout()
plt.show()
