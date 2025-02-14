import requests
import pandas as pd
from datetime import datetime

def fetch_data():
    URL = "https://api.open-meteo.com/v1/forecast?latitude=14.59&longitude=120.98&hourly=temperature_2m"
    response = requests.get(URL)
    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame(data['hourly'])

    # Ensure timestamps are in proper datetime format
    df['time'] = pd.to_datetime(df['time'])

    # Save to CSV (overwrite previous file)
    df.to_csv("weather_data.csv", index=False)

    print("✅ Weather data fetched and saved to CSV!")

if __name__ == "__main__":
    fetch_data()
