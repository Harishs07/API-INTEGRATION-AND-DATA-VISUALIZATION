import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Replace this with your actual OpenWeatherMap API key
API_KEY = "d2a93baba6660699471934bee76dd080"
CITY = "Coimbatore"

# OpenWeatherMap API URL
url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data from API
response = requests.get(url)
data = response.json()

# Extract required data
dates, temps, humidity = [], [], []

for entry in data['list']:
    dt = datetime.datetime.strptime(entry['dt_txt'], "%Y-%m-%d %H:%M:%S")
    temp = entry['main']['temp']
    hum = entry['main']['humidity']
    
    dates.append(dt)
    temps.append(temp)
    humidity.append(hum)

# Plotting with seaborn
sns.set(style="whitegrid")

plt.figure(figsize=(14, 6))

# Temperature plot
plt.subplot(1, 2, 1)
sns.lineplot(x=dates, y=temps, color='orange')
plt.title(f"Temperature Forecast - {CITY}")
plt.xlabel("Date/Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)

# Humidity plot
plt.subplot(1, 2, 2)
sns.lineplot(x=dates, y=humidity, color='blue')
plt.title(f"Humidity Forecast - {CITY}")
plt.xlabel("Date/Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
