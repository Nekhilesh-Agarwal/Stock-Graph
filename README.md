---

# **Live Stock Price Visualization Using yFinance**

This repository contains Python scripts for visualizing stock price data over various time frames (1 Day, 1 Week, 1 Month, 3 Months, 6 Months, 1 Year, and 5 Years) using `yfinance` and live data updates with interactive charts.

---

## **Features**
- Fetch live stock data for multiple timeframes:
  - **1 Day** 
  - **1 Week**
  - **1 Month**
  - **3 Months**
  - **6 Months**
  - **1 Year**
  - **5 Years**
- Intraday data with 1-minute intervals
- Dynamic and interactive visualizations.
- Highlight key price statistics (closing price, percentage change, etc.) in real-time.
- User-friendly console output and live updates.

---

## **Installation**

1. Clone this repository:
   ```bash
   git clone https://github.com/Nekhilesh-Agarwal/Stock-Graph.git
   cd stock-price-visualization
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Required Libraries**:
   - `yfinance`
   - `matplotlib`

---

## **Usage**

Run the corresponding script based on the time frame you wish to visualize:

### **1 Day**
```bash
python "Final 1 Day.py"
```

### **1 Week**
```bash
python "Final 1 Week.py"
```

### **1 Month**
```bash
python "Final 1 Month.py"
```

### **3 Months**
```bash
python "Final 3 Month.py"
```

### **6 Months**
```bash
python "Final 6 Month.py"
```

### **1 Year**
```bash
python "Final 1 Year.py"
```

### **5 Years**
```bash
python "Final 5 Year.py"
```

### **Input**
When prompted, enter the stock symbol (e.g., `TATAMOTORS.NS` for Tata Motors on NSE, `AAPL` for Apple, etc.).

---


## **Naming Conventions**
In `yfinance`, stock tickers follow these conventions:
- **NSE Stocks**: Append `.NS` (e.g., `TATAMOTORS.NS`).
- **BSE Stocks**: Append `.BO` (e.g., `500325.BO`).
- **US Stocks**: Use the symbol as-is (e.g., `AAPL`).
- **Cryptocurrency**: Use symbols like `BTC-USD` or `ETH-USD`.

---

## **Contributing**
If you have suggestions or want to enhance this project, feel free to fork the repo, make changes, and submit a pull request.

---
