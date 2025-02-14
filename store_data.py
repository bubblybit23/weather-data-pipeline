import duckdb
import pandas as pd

def store_data():
    # Connect to DuckDB
    db_connection = duckdb.connect("weather_data.db")
    
    try:
        df = pd.read_csv("weather_data.csv")
        df['time'] = pd.to_datetime(df['time'])  # Ensure datetime format

        # Ensure table exists
        db_connection.execute("""
            CREATE TABLE IF NOT EXISTS weather (
                time TIMESTAMP PRIMARY KEY,
                temperature_2m FLOAT
            )
        """)

        # Insert only new data (ignore duplicates)
        db_connection.execute("""
            INSERT OR REPLACE INTO weather
            SELECT * FROM df
        """)

        print("✅ Data stored in DuckDB!")
    except Exception as e:
        print(f"❌ Error while storing data: {e}")

if __name__ == "__main__":
    store_data()
