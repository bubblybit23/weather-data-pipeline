import duckdb
import streamlit as st

def load_data():
    db_connection = duckdb.connect("weather_data.db")
    
    # Ensure the table exists before querying
    db_connection.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            time TIMESTAMP,
            temperature_2m FLOAT
        )
    """)

    try:
        df = db_connection.execute("SELECT * FROM weather").df()
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

df = load_data()

if df is not None and not df.empty:
    st.title("🌤️ Weather Dashboard")
    st.line_chart(df.set_index("time")["temperature_2m"])
else:
    st.write("⚠️ No data found. Make sure to upload `weather_data.csv` first.")
