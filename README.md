# 🌤️ Manila Weather Dashboard

An **automated weather data pipeline** built with **Streamlit, DuckDB, GitHub Actions, and Render.com**. This project fetches, stores, and visualizes real-time weather data for **Manila**.

---

## 🚀 Features
✅ **Automated ETL Pipeline** using **GitHub Actions** (Runs every hour)  
✅ **Cloud Deployment** with **Render.com** (No manual execution needed)  
✅ **Stores Weather Data Efficiently** in **DuckDB** (Lightweight & Fast)  
✅ **Interactive Data Visualizations** (Temperature Trends & Analytics)  
✅ **Fetches Latest Weather Data** from **Open-Meteo API**  
✅ **Ensures Data Integrity** by avoiding duplicates  

---

## 📦 Installation

### **1️⃣ Clone this repository**
```sh
git clone https://github.com/yourusername/weather-dashboard.git
```

### **2️⃣ Install dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the application**
```sh
streamlit run app.py
```

---

## ⚙️ How It Works
- **ETL Pipeline:** Automates data fetching & storage via **GitHub Actions**  
- **Database:** Uses **DuckDB** to store structured weather data  
- **Deployment:** Hosted on **Render.com** for real-time dashboard access  
- **Scheduled Updates:** GitHub Actions **fetches new data hourly** & updates `weather_data.db`  
- **Smart Filtering:** Displays only the **latest data** to avoid duplication  

---

## 📂 Project Structure
```
weather-data-pipeline/
├── app.py          # Streamlit dashboard
├── fetch_data.py   # Fetches weather data from API
├── store_data.py   # Stores cleaned data in DuckDB
├── weather_data.db # DuckDB database (auto-updated)
├── requirements.txt # Dependencies
├── .github/workflows/
│   ├── etl.yml     # GitHub Actions ETL automation
└── README.md       # Documentation
```

---

## 📊 Dashboard Preview
![Dashboard Preview](https://github.com/bubblybit23/weather-data-pipeline/blob/main/dashboard_preview.png)

---

## 🔄 Data Processing Flow
1️⃣ **Fetch Data** (`fetch_data.py`) → Retrieves latest weather data via Open-Meteo API  
2️⃣ **Store Data** (`store_data.py`) → Inserts & updates data in DuckDB  
3️⃣ **Automate ETL** (`etl.yml`) → GitHub Actions **fetches & updates** data every hour  
4️⃣ **Deploy to Cloud** (`app.py`) → **Streamlit dashboard** fetches latest stored data  
