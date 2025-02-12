import duckdb
import pandas as pd

def store_data():
    # Connect to DuckDB (the database file will be created if it doesn't exist)
    db_connection = duckdb.connect("weather_data.db")
    
    # Check if the CSV file exists, then load data into the 'weather' table
    try:
        df = pd.read_csv('weather_data.csv')  # Load the CSV data
        db_connection.execute("CREATE TABLE IF NOT EXISTS weather AS SELECT * FROM df")  # Create the table
        print("✅ Data stored in DuckDB!")
    except Exception as e:
        print(f"Error while storing data: {e}")

store_data()
