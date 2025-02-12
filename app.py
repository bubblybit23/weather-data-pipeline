import duckdb
import streamlit as st

def load_data():
    db_connection = duckdb.connect("weather_data.db")
    
    # Check if the 'weather' table exists
    try:
        df = db_connection.execute("SELECT * FROM weather").df()
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

df = load_data()

if df is not None:
    st.title("🌤️ Weather Dashboard")
    st.line_chart(df.set_index("time")["temperature_2m"])
else:
    st.write("Data could not be loaded!")
