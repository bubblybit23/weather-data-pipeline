# Manila Weather Dashboard 🌤️

A **Streamlit** app that fetches, stores, and visualizes weather data for **Manila** using **DuckDB**.

## Features 🚀
- **Fetches & stores** real-time weather data.
- **Displays temperature trends** with interactive charts.
- **Uses DuckDB** for efficient queries.
- **Shows raw data** for exploration.

## 📦 Installation

### **1️⃣ Clone this repository**

git clone https://github.com/yourusername/weather-dashboard.git

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Run the application

streamlit run app.py

## How It Works ⚙️  
- **Checks & loads data** from `weather_data.db`  
- **Fetches data** if missing and stores it  
- **Displays dashboard** with trends & raw data  

## Project Structure 📁  
'''
weather-data-pipeline/
├── app.py          # Streamlit dashboard
├── fetch_data.py   # Fetch weather data
├── store_data.py   # Store data in DuckDB
├── weather_data.db # DuckDB database
├── requirements.txt # Dependencies
└── README.md       # Documentation
'''


## Future Improvements 📌  
- Add **humidity & precipitation** data.  
- Include **date range filters**.  
- Perform **trend analysis**.  

