# 🌍 Weather Data Pipeline

**A complete end-to-end data engineering project** that demonstrates ETL concepts, automation, and data analysis.

## 📋 Project Overview

This project fetches real-time weather data from 100+ cities worldwide, stores it in a MySQL database, analyzes it with Python + Pandas, and provides beautiful visualizations.

Perfect for learning data engineering fundamentals!

## ✨ Features

✅ **Real-time API Integration** - Fetches weather from wttr.in  
✅ **Automated Pipeline** - Runs hourly (Task Scheduler/Cron)  
✅ **Data Validation** - Validates before inserting to database  
✅ **MySQL Storage** - Relational database design  
✅ **Error Handling** - Graceful error handling with logging  
✅ **Data Analysis** - Pandas-based statistical analysis  
✅ **10 Beautiful Visualizations** - Production-ready charts  
✅ **Scalable** - Easily extends to 1000+ cities  

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.8+ |
| **Data Source** | wttr.in API (free) |
| **Database** | MySQL |
| **Data Analysis** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Notebook** | Jupyter |
| **Automation** | Task Scheduler (Windows) / Cron (Linux/Mac) |

## 📁 Project Structure
weather-pipeline/
├── fetch_weather.py # Main ETL script (100 cities)
├── weather_10_visualizations.py # All visualizations
├── weather_analysis.ipynb # Jupyter notebook
├── pipeline.log # Execution logs
├── requirements.txt # Python dependencies
├── README.md # This file
└── run_weather.bat # Windows batch file

## 🚀 Quick Start

### **1. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **2. Setup MySQL Database**

```sql
CREATE DATABASE weather_project;
USE weather_project;

CREATE TABLE weather (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    humidity INT,
    description VARCHAR(100),
    date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### **3. Configure Script**

Edit `fetch_weather.py` and update MySQL credentials:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",  # ← Change this!
    database="weather_project"
)
```

### **4. Run Script**

```bash
python fetch_weather.py
```

**Expected Output:**
✅ Starting weather data fetch for 100 cities...
[1/100] ✅ Thrissur: 28.5°C, 65%
[2/100] ✅ Kochi: 29.1°C, 70%
...
[100/100] ✅ Johannesburg: 22.3°C, 45%

✅ Done! Saved: 100 cities, Failed: 0 cities

### **5. Analyze Data**

```bash
jupyter notebook weather_analysis.ipynb
```

## 📊 Data Analysis

### **Quick Statistics**

```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:password@localhost/weather_project')
df = pd.read_sql("SELECT * FROM weather", engine)

# Basic stats
print(f"Total records: {len(df)}")
print(f"Avg temp: {df['temperature'].mean():.1f}°C")
print(f"Avg humidity: {df['humidity'].mean():.1f}%")

# Top hottest cities
print(df.nlargest(5, 'temperature')[['city', 'temperature']])
```

### **Key Insights (Sample)**

- **Total Cities:** 100 (India + World)
- **Hottest City:** Delhi (42°C)
- **Coldest City:** Oslo (8°C)
- **Global Average Temp:** 25.3°C
- **Global Average Humidity:** 62%
- **Most Common Weather:** Cloudy

## 📈 Visualizations

The project includes **10 production-ready visualizations:**

1. Top 15 Hottest Cities
2. Top 15 Coldest Cities
3. Temperature Distribution (Histogram)
4. Humidity Distribution (Histogram)
5. Weather Conditions (Pie Chart)
6. Temperature vs Humidity (Scatter Plot)
7. Top 10 Most Humid Cities
8. Temperature Categories (Pie + Bar)
9. India vs World Comparison
10. Analytics Dashboard

### Generate Visualizations

```bash
# Option 1: Run via Python
python weather_10_visualizations.py

# Option 2: Run Jupyter notebook
jupyter notebook weather_analysis.ipynb
```

## ⏰ Automation Setup

### **Windows (Task Scheduler)**

1. Create `run_weather.bat`:
```batch
@echo off
cd C:\Users\yourusername\weather-pipeline
python fetch_weather.py
```

2. Open Task Scheduler
3. Create Basic Task
4. Trigger: Daily, repeat every 1 hour
5. Action: Run `run_weather.bat`
6. Done! ✅

### **Linux/Mac (Cron)**

```bash
crontab -e

# Add this line:
0 * * * * python /path/to/weather-pipeline/fetch_weather.py
```

## 📊 Data Growth Over Time

| Timeline | Records | Data Points |
|----------|---------|------------|
| Day 1 | 100 | 100 |
| Day 7 | 700 | 700 |
| Week 2 | 1,400 | 1,400 |
| Month 1 | 4,200 | 4,200 |

## 🎓 Learning Outcomes

This project teaches:

### Data Engineering Concepts
- ✅ ETL (Extract → Transform → Load)
- ✅ Data validation & quality checks
- ✅ Database design
- ✅ Error handling & logging
- ✅ Automation & scheduling

### Technical Skills
- ✅ REST API integration
- ✅ Python scripting
- ✅ MySQL/SQL
- ✅ Pandas data manipulation
- ✅ Data visualization (Matplotlib/Seaborn)
- ✅ Jupyter notebooks
- ✅ Git & GitHub

### Production Concepts
- ✅ How real pipelines work
- ✅ Reliability & error handling
- ✅ Scalability
- ✅ Monitoring

## 🐛 Troubleshooting

### **"No module named 'requests'"**
```bash
pip install requests
```

### **"MySQL connection failed"**
1. Verify MySQL is running
2. Check credentials
3. Ensure database exists

### **"Table doesn't exist"**
Run the SQL setup script above.

### **"API connection error"**
Check your internet connection and API status.

## 🚀 Next Steps

- [ ] Deploy to cloud (AWS Lambda)
- [ ] Add email alerts for failures
- [ ] Create real-time dashboard (Streamlit)
- [ ] Add machine learning predictions
- [ ] Implement data quality checks
- [ ] Create API for data access
- [ ] Deploy with Docker

## 📚 Resources

- [Data Engineering Fundamentals](https://www.freecodecamp.org/news/what-is-data-engineering/)
- [wttr.in API Documentation](https://wttr.in/about)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Apache Airflow](https://airflow.apache.org/)

## 💡 Key Learnings

- **Netflix, Uber, Google use this exact pattern** at massive scale
- Start simple, scale gradually
- Automation > Manual work
- Real data > Tutorial data
- Build systems, not scripts

## 📱 Connect

**GitHub:** [@yourusername](https://github.com/yourusername)  
**LinkedIn:** [Your LinkedIn Profile](https://linkedin.com)  

## 📄 License

MIT License - Feel free to use this for learning and projects!

---

**⭐ If this helps you, please give it a star!**

Last Updated: August 2026  
Status: Active ✅ (Automated pipeline running 24/7)