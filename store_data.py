import duckdb

def store_data():
    db_connection = duckdb.connect("weather_data.db")
    db_connection.execute("CREATE TABLE IF NOT EXISTS weather AS SELECT * FROM read_csv_auto('weather_data.csv')")
    print("✅ Data stored in DuckDB!")

store_data()
