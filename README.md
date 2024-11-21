**Cryptocurrency Data Tracker**
This project is a simple Python-based tool to track cryptocurrency market data in real-time. It fetches data from the CoinGecko API, analyzes it, creates cool visualizations, and updates an Excel file every 5 minutes with the latest insights.

**How It Works**
Fetches Real-Time Data: The script connects to the CoinGecko API and grabs details about the top 50 cryptocurrencies, including their market cap, current price, and price changes.

**Performs Analysis:**

Identifies the top 5 cryptocurrencies based on market capitalization.
Calculates the average price of all 50 cryptocurrencies.
Finds the cryptocurrency with the biggest 24-hour price gain and the one with the biggest loss.

**Creates Visualizations:
**
A bar chart showing the top 5 cryptocurrencies by market capitalization.
A simple bar chart of the average price.
A comparison of the highest and lowest 24-hour price changes.
Saves Data to an Excel File: The script generates an Excel file, cryptocurrency_data.xlsx, containing:

A detailed data sheet with all the fetched information.
A summary analysis sheet with insights like top 5 cryptocurrencies, average price, and the biggest gainers/losers.
Updates Every 5 Minutes: The script runs in a loop and updates both the Excel file and visualizations every 5 minutes so you always have the latest data.

