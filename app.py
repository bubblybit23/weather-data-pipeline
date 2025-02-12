import duckdb
import streamlit as st
import os
import pandas as pd

# Function to check if the database exists
def db_exists():
    return os.path.exists("weather_data.db")

# Function to run ETL script if the database is missing
def run_etl():
    import fetch_data
    import store_data

    st.warning("⚠️ Database not found! Fetching and storing new data...")
    
    # Run ETL scripts to populate the database
    fetch_data.main()
    store_data.main()

# Check if the database exists, else run ETL
if not db_exists():
    run_etl()

# Connect to DuckDB
db_connection = duckdb.connect("weather_data.db")

# Load data
def load_data():
    try:
        df = db_connection.execute("SELECT * FROM weather").df()
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

df = load_data()

st.title("🌤️ Weather Dashboard")

if df is not None and not df.empty:
    st.line_chart(df.set_index("time")["temperature_2m"])
else:
    st.write("⚠️ No data available. Please check the ETL pipeline.")
