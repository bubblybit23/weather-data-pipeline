import duckdb
import pandas as pd

def store_data():
    # Connect to a persistent DuckDB database file
    db_connection = duckdb.connect("weather_data.db")
    
    try:
        df = pd.read_csv('weather_data.csv')  # Load the CSV data
        
        # Ensure table exists before inserting data
        db_connection.execute("""
            CREATE TABLE IF NOT EXISTS weather (
                time TIMESTAMP,
                temperature_2m FLOAT
            )
        """)

        # Insert new data (DuckDB requires INSERT to match the table structure)
        db_connection.execute("INSERT INTO weather SELECT * FROM df")

        print("✅ Data stored in DuckDB!")
    except Exception as e:
        print(f"Error while storing data: {e}")

store_data()
