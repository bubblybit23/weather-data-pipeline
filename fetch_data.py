import requests
import pandas as pd

def fetch_weather_data():
    URL = "https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&hourly=temperature_2m"
    response = requests.get(URL)
    data = response.json()
    df = pd.DataFrame(data['hourly'])
    df.to_csv("weather_data.csv", index=False)
    print("✅ Weather data fetched and saved to CSV!")

fetch_weather_data()
