# Cryptocurrency Data Tracker  

## Overview  
This project is a simple Python-based tool to track cryptocurrency market data in real-time. It fetches data from the [CoinGecko API](https://www.coingecko.com/en/api), performs analysis, creates visualizations, and updates an Excel file every 5 minutes with the latest insights.  

## How It Works  

1. **Fetches Real-Time Data**  
   The script connects to the CoinGecko API and retrieves details about the top 50 cryptocurrencies, including their market cap, current price, price changes, and more. This data is fetched every 5 minutes to ensure it remains up-to-date.  

2. **Performs Analysis**  
   The script analyzes the fetched data and computes the following insights:  
   - **Top 5 Cryptocurrencies by Market Capitalization:** Identifies the 5 cryptocurrencies with the highest market caps.  
   - **Average Price of Top 50 Cryptocurrencies:** Calculates the average current price of the top 50 cryptocurrencies.  
   - **Biggest Price Change:** Finds the cryptocurrency with the largest 24-hour price increase and the one with the largest 24-hour price decrease.  

3. **Creates Visualizations**  
   The script generates the following visualizations:  
   - **Top 5 Cryptocurrencies by Market Cap:** A bar chart that shows the top 5 cryptocurrencies by market capitalization.  
   - **Average Price:** A simple bar chart visualizing the average price of the top 50 cryptocurrencies.  
   - **24-hour Price Change Comparison:** A comparison of the highest and lowest 24-hour price changes.  

4. **Saves Data to Excel**  
   The script generates an Excel file (`cryptocurrency_data.xlsx`) containing:  
   - **Data Sheet:** A detailed sheet with all the fetched information.  
   - **Analysis Sheet:** A summary sheet with insights such as the top 5 cryptocurrencies, average price, and the biggest gainers/losers.  

5. **Updates Every 5 Minutes**  
   The script runs in a loop, fetching new data every 5 minutes, and updates both the Excel file and visualizations to reflect the latest market information.  

## Requirements  
- Python 3.x  
- Libraries:  
  - `requests` - To fetch data from the CoinGecko API  
  - `pandas` - To handle data processing and analysis  
  - `seaborn` & `matplotlib` - For creating visualizations  
  - `openpyxl` - To work with Excel files  

## Install Required Libraries  
To install the required libraries, run:  
```bash  
pip install requests pandas seaborn matplotlib openpyxl
