"""
Streamlit app to display Manila weather data.

This app reads weather data from a DuckDB database and displays it
using Streamlit. The database is expected to be populated by a
separate ETL (Extract, Transform, Load) process (e.g., a GitHub
Actions workflow).

Functions:
    db_exists(): Checks if the DuckDB database file exists.
    load_data(): Loads weather data from DuckDB into a Pandas DataFrame.

Streamlit Dashboard:
    - Displays a title ("🌤️ Manila Weather Dashboard").
    - Checks for the existence of the database before proceeding.
    - Loads data using load_data().
    - If data is available, displays a dashboard with:
        - Sidebar filters for date range.
        - Summary metrics (average, max, min temperature).
        - Temperature trends chart.
        - Moving average chart.
        - Data details (total data points, time range, columns).
        - Option to show raw data.
    - If data is not available, displays a message indicating that the
      ETL pipeline might be in progress.
"""



import duckdb
import streamlit as st
import os
import pandas as pd

# ---------------------------- #
#       UTILITY FUNCTIONS      #
# ---------------------------- #


DB_PATH = "weather_data.db"  # Path in the repository root

def db_exists():
    return os.path.exists(DB_PATH)
    """Checks if the DuckDB database file exists."""
    return os.path.exists("weather_data.db")

def load_data():
    """Loads weather data from DuckDB into a Pandas DataFrame."""
    try:
        conn = duckdb.connect("weather_data.db") # Connect inside the function
        df = conn.execute("SELECT * FROM weather").df()
        conn.close() # Close the connection after use
        return df
    except duckdb.CatalogException:  # Handle table not found
        st.error("❌ Weather data table not found in the database. Please wait for the ETL pipeline to run.")
        return None  # Return None if the table doesn't exist
    except Exception as e:
        st.error(f"❌ Error loading data: {e}")
        return None
# ---------------------------- #
#      STREAMLIT DASHBOARD     #
# ---------------------------- #

# Set the Streamlit app title
st.title("🌤️ Manila Weather Dashboard")

# Check for database existence *before* attempting to load data
if not db_exists():
    st.error("❌ Database not found! Please wait for the ETL pipeline to update it.")
    st.stop()  # Stop execution if DB is missing

df = load_data()  # ***CALL load_data() HERE***  This is the crucial missing line

if df is not None and not df.empty:
    # Convert 'time' column to datetime for proper analysis
    df['time'] = pd.to_datetime(df['time'])

    # ----------- Sidebar Filters ----------- #
    st.sidebar.header("🔍 Data Filters")
    
    # Date range selector
    start_date = st.sidebar.date_input("Start Date", df["time"].min().date())
    end_date = st.sidebar.date_input("End Date", df["time"].max().date())

    # Filter data based on user-selected date range
    filtered_df = df[(df["time"].dt.date >= start_date) & (df["time"].dt.date <= end_date)]

    # ----------- Summary Metrics ----------- #
    st.subheader("📊 Weather Summary")
    
    # Three columns for displaying key statistics
    col1, col2, col3 = st.columns(3)
    col1.metric("🌡️ Avg Temperature", f"{filtered_df['temperature_2m'].mean():.2f}°C")
    col2.metric("🔥 Max Temperature", f"{filtered_df['temperature_2m'].max():.2f}°C")
    col3.metric("❄️ Min Temperature", f"{filtered_df['temperature_2m'].min():.2f}°C")

    # ----------- Temperature Trends ----------- #
    st.subheader("📈 Temperature Over Time")
    st.line_chart(filtered_df.set_index("time")["temperature_2m"])

    # ----------- Moving Average Trend ----------- #
    st.subheader("📊 Moving Average (7 Days)")
    filtered_df["7-day MA"] = filtered_df["temperature_2m"].rolling(window=7).mean()
    st.line_chart(filtered_df.set_index("time")[["temperature_2m", "7-day MA"]])

    # ----------- Data Details ----------- #
    st.subheader("📂 Data Details")
    st.write(f"**Total Data Points:** {len(filtered_df)}")
    st.write(f"**Time Range:** {filtered_df['time'].min()} → {filtered_df['time'].max()}")
    st.write("**Available Data Columns:**")
    st.write(", ".join(filtered_df.columns))

    # Allow users to see raw data
    if st.checkbox("🔍 Show Raw Data"):
        st.dataframe(filtered_df)

else:
    st.write("⚠️ No data available. Please check the ETL pipeline. It may take some time for the data to be fetched and stored.")
