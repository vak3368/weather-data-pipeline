import requests
import mysql.connector
from datetime import datetime
import logging
import time

logging.basicConfig(filename='pipeline.log', level=logging.INFO)
logger = logging.getLogger(__name__)

# 100 Cities - India + World
cities = [
    # India (40 cities)
    "Thrissur", "Kochi", "Bangalore", "Chennai", "Mumbai", "Delhi", "Hyderabad", "Pune",
    "Kolkata", "Ahmedabad", "Jaipur", "Lucknow", "Indore", "Chandigarh", "Surat",
    "Bhopal", "Patna", "Vadodara", "Ghaziabad", "Ludhiana", "Visakhapatnam", "Nagpur",
    "Coimbatore", "Meerut", "Nashik", "Faridabad", "Ranchi", "Aurangabad", "Kurnool",
    "Thiruvananthapuram", "Guwahati", "Mysore", "Hubballi", "Kozhikode", "Ernakulam",
    "Kannur", "Alappuzha", "Malappuram", "Palakkad",
    
    # World (60 cities)
    "New York", "Los Angeles", "London", "Paris", "Tokyo", "Sydney", "Dubai", "Singapore",
    "Bangkok", "Hong Kong", "Istanbul", "Moscow", "Toronto", "Mexico City", "São Paulo",
    "Buenos Aires", "Cairo", "Beijing", "Shanghai", "Seoul", "Barcelona", "Rome",
    "Berlin", "Amsterdam", "Madrid", "Vienna", "Prague", "Stockholm", "Copenhagen",
    "Oslo", "Lisbon", "Dublin", "Athens", "Melbourne", "Auckland", "Cape Town",
    "Jakarta", "Manila", "Ho Chi Minh", "Hanoi", "Kuala Lumpur", "Colombo", "Karachi",
    "Lahore", "Dhaka", "Kathmandu", "Tehran", "Baghdad", "Beirut", "Jerusalem",
    "Riyadh", "Kuwait", "Doha", "Abu Dhabi", "Muscat", "Amman", "Damascus",
    "Khartoum", "Nairobi", "Lagos", "Johannesburg",
]

try:
    print(f"✅ Starting weather data fetch for {len(cities)} cities...")
    
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="weather_project"
    )
    
    cursor = connection.cursor()
    
    successful = 0
    failed = 0
    
    # Fetch weather for each city
    for i, city in enumerate(cities, 1):
        try:
            url = f"https://wttr.in/{city}?format=j1"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            
            current = data['current_condition'][0]
            temperature = float(current['temp_C'])
            humidity = int(current['humidity'])
            description = current['weatherDesc'][0]['value']
            
            # Insert data
            sql = "INSERT INTO weather (city, temperature, humidity, description) VALUES (%s, %s, %s, %s)"
            values = (city, temperature, humidity, description)
            cursor.execute(sql, values)
            
            print(f"[{i}/100] ✅ {city}: {temperature}°C, {humidity}%")
            successful += 1
            
            # Small delay to not overload API
            time.sleep(0.5)
            
        except Exception as e:
            print(f"[{i}/100] ❌ {city}: {str(e)[:50]}")
            failed += 1
            time.sleep(0.5)
            continue
    
    connection.commit()
    print(f"\n✅ Done! Saved: {successful} cities, Failed: {failed} cities")
    logger.info(f"Success: Saved weather for {successful}/{len(cities)} cities at {datetime.now()}")
    
    cursor.close()
    connection.close()

except Exception as err:
    print(f"❌ Error: {err}")
    logger.error(f"Error: {err}")