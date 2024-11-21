import time
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

def fetch_and_update_data():
    api_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false"
    response = requests.get(api_url)
    data = response.json()

    df = pd.DataFrame(data)

    top_5 = df.nlargest(5, 'market_cap')

    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_5['name'], y=top_5['market_cap'], palette='Blues_d')
    plt.title('Top 5 Cryptocurrencies by Market Cap', fontsize=16)
    plt.ylabel('Market Cap (USD)', fontsize=12)
    plt.xlabel('Cryptocurrency', fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.tight_layout()
    plot1_path = os.path.join(os.getcwd(), 'top_5_market_cap.png')
    plt.savefig(plot1_path)
    plt.close()

    avg_price = df['current_price'].mean()

    plt.figure(figsize=(6, 6))
    plt.bar(['Average Price'], [avg_price], color='green')
    plt.text(0, avg_price / 2, f"${avg_price:.2f}", ha='center', va='center', fontsize=12, color='white', fontweight='bold')
    plt.title('Average Price of Top 50 Cryptocurrencies', fontsize=14)
    plt.ylabel('Price (USD)')
    plt.tight_layout()
    plot2_path = os.path.join(os.getcwd(), 'average_price.png')
    plt.savefig(plot2_path)
    plt.close()

    price_change_sorted = df.sort_values(by='price_change_24h', ascending=False)
    highest_price_change = price_change_sorted.iloc[0]['price_change_24h']
    lowest_price_change = price_change_sorted.iloc[-1]['price_change_24h']

    highest_change_crypto = price_change_sorted.iloc[0]
    lowest_change_crypto = price_change_sorted.iloc[-1]
    change_data = {
        'Cryptocurrency': [highest_change_crypto['name'], lowest_change_crypto['name']],
        'Price Change (%)': [highest_price_change, lowest_price_change]
    }
    change_df = pd.DataFrame(change_data)

    plt.figure(figsize=(8, 6))
    sns.barplot(x='Cryptocurrency', y='Price Change (%)', data=change_df, palette='coolwarm')
    plt.title('24-Hour Percentage Price Changes')
    plt.ylabel('Price Change (%)')
    plt.tight_layout()
    plot3_path = os.path.join(os.getcwd(), 'price_changes.png')
    plt.savefig(plot3_path)
    plt.close()

    output_file = os.path.join(os.getcwd(), 'cryptocurrency_data.xlsx')
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Data', index=False)
        analysis_df = pd.DataFrame({
            'Metric': ['Top 5 Cryptocurrencies by Market Capitalization', 'Average Price of Top 50 Cryptocurrencies', 'Highest 24-hour Price Change', 'Lowest 24-hour Price Change'],
            'Value': [', '.join(top_5['name'].tolist()), f"${avg_price:.2f}", f"{highest_price_change:.2f}%", f"{lowest_price_change:.2f}%"]
        })
        analysis_df.to_excel(writer, sheet_name='Analysis', index=False)

    print("Data and visualizations updated at", time.strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == "__main__":
    while True:
        fetch_and_update_data()
        time.sleep(300)

