import streamlit as st
import duckdb
import pandas as pd

def load_data():
    db_connection = duckdb.connect("weather_data.db")
    df = db_connection.execute("SELECT * FROM weather").df()
    return df

df = load_data()

st.title("🌤️ Weather Dashboard")
st.line_chart(df.set_index("time")["temperature_2m"])
