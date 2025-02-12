import duckdb
import streamlit as st
import pandas as pd
import os

# Function to run the ETL script
def run_etl():
    os.system("python etl.py")  # Runs your ETL pipeline before the app loads

# Connect to DuckDB
db_connection = duckdb.connect("weather_data.db")

# Check if 'weather' table exists
try:
    db_connection.execute("SELECT * FROM weather LIMIT 1")  # Quick check
except duckdb.CatalogException:
    st.warning("⚠️ Weather table is missing. Running ETL script...")
    run_etl()  # Run ETL to generate data

# Function to load data
def load_data():
    try:
        df = db_connection.execute("SELECT * FROM weather").df()
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Load and display the data
df = load_data()
st.title("🌤️ Weather Dashboard")

if df is not None and not df.empty:
    st.line_chart(df.set_index("time")["temperature_2m"])
else:
    st.write("⚠️ No data found. Make sure ETL script is running properly.")
