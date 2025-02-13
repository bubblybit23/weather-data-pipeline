import duckdb
import streamlit as st
import os
import pandas as pd

# ---------------------------- #
#       UTILITY FUNCTIONS      #
# ---------------------------- #

def db_exists():
    """
    Checks if the DuckDB database file exists.

    Returns:
        bool: True if the database file exists, False otherwise.
    """
    return os.path.exists("weather_data.db")

def run_etl():
    """
    Runs the ETL (Extract, Transform, Load) pipeline if the database is missing.
    
    This function imports `fetch_data` and `store_data` modules and executes their `main()` functions 
    to fetch new weather data and store it into the database.
    """
    import fetch_data  # Module responsible for fetching weather data from an API
    import store_data  # Module responsible for storing data in DuckDB

    st.warning("⚠️ Database not found! Fetching and storing new data...")

    try:
        fetch_data.main()  # Fetch weather data
        store_data.main()  # Store data into the DuckDB database
        st.success("✅ Data successfully fetched and stored!")
    except Exception as e:
        st.error(f"❌ ETL Process Failed: {e}")

# Check if the database exists, otherwise run the ETL process
if not db_exists():
    run_etl()

# Establish a connection to DuckDB
db_connection = duckdb.connect("weather_data.db")

def load_data():
    """
    Loads weather data from DuckDB into a Pandas DataFrame.

    Returns:
        pd.DataFrame: DataFrame containing the weather data.
    """
    try:
        df = db_connection.execute("SELECT * FROM weather").df()
        return df
    except Exception as e:
        st.error(f"❌ Error loading data: {e}")
        return None

# Load data into a Pandas DataFrame
df = load_data()

# ---------------------------- #
#      STREAMLIT DASHBOARD     #
# ---------------------------- #

# Set the Streamlit app title
st.title("🌤️ Manila Weather Dashboard")

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
