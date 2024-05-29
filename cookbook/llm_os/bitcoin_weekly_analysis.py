import yfinance as yf
import mplfinance as mpf
import pandas as pd
import datetime

# Step 1: Fetch historical data from yfinance
def fetch_bitcoin_data():
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=365)
    btc_data = yf.download("BTC-USD", start=start_date, end=end_date)
    return btc_data

# Step 2: Resample the data to weekly intervals
def resample_to_weekly(data):
    weekly_data = data.resample('W').agg({
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
        'Volume': 'sum'
    })
    return weekly_data

# Step 3: Generate a candlestick chart
def generate_candlestick_chart(weekly_data, file_name):
    mpf.plot(weekly_data, type='candle', style='charles', volume=True,
             title='Bitcoin Weekly Candlestick Chart',
             ylabel='Price (USD)',
             ylabel_lower='Volume', 
             savefig=file_name)

if __name__ == "__main__":
    # Fetch data
    btc_data = fetch_bitcoin_data()
    # Resample data
    weekly_data = resample_to_weekly(btc_data)
    # Generate candlestick chart
    generate_candlestick_chart(weekly_data, 'bitcoin_weekly_candlesticks.png')