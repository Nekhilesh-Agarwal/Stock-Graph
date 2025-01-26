import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Ask the user for the stock symbol
symbol = input("Enter the stock symbol (e.g., GOOG for Google shares): ")

# Initialize the ticker object
ticker = yf.Ticker(symbol)

# Create a figure for the plot with a black background
fig, ax = plt.subplots(figsize=(12, 6), facecolor='black')

# Variable to store the previous closing price
previous_close = None

# Function to fetch and plot live intraday data
def fetch_and_plot(i):
    global previous_close  # Use the global variable to track the previous closing price

    # Fetch live intraday data for today with 1-minute intervals
    intraday_data_df = ticker.history(period="1d", interval="1m")  # Fetching only today's data
    
    # Check if the data is available
    if intraday_data_df.empty:
        print(f"No intraday data available for {symbol}.")
        return  # Return early if no data is available

    # Clear the plot to prevent overlap
    ax.cla()

    # Plot the closing price for each minute of today's trading
    ax.plot(intraday_data_df.index, intraday_data_df['Close'], color='blue', label='Closing Price')

    # Get the current closing price
    current_close = intraday_data_df['Close'].iloc[-1]  # Get the latest closing price

    # Print the current price to the console
    print(f'Current Price: {current_close:.2f} INR')

    # Print the change in closing price
    if previous_close is not None:
        change = current_close - previous_close
        percentage_change = (change / previous_close) * 100
        print(f'Change: {change:.2f} INR ({percentage_change:.2f}%)')

    # Update the previous closing price
    previous_close = current_close

    # Set title and labels with white text
    ax.set_title(f'{symbol} Intraday Stock Price (Live Data)', color='white')
    ax.set_xlabel('Time', color='white')
    ax.set_ylabel('Price (INR)', color='white')

    # Customize the grid and background
    ax.grid(color='dimgray', linestyle=':', linewidth=0.5, alpha=0.7)
    ax.set_facecolor('black')  # Background color
    ax.tick_params(colors='white')  # Tick colors
    ax.xaxis.label.set_color('white')  # X-axis label color
    ax.yaxis.label.set_color('white')  # Y-axis label color
    plt.xticks(color='white')  # X-axis ticks color
    plt.yticks(color='white')  # Y-axis ticks color

# Set up animation for live updates every 10 seconds
ani = FuncAnimation(fig, fetch_and_plot, interval=10000)  # 10000 ms = 10 sec

# Display the live-updating plot
plt.tight_layout()
plt.show()
