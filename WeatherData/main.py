import requests
import matplotlib.pyplot as plt

base_url= "https://api.openweathermap.org/data/2.5/weather?"
api_key='1e0e3115a39812bcf4be382ee59932b6'

url = f"{base_url}&appid={api_key}&units=metric&lang=tr"
cities = ["Istanbul", "Ankara", "Izmir", "Antalya", "Bursa"]
temperatures = []


for city in cities:
    url = f"{base_url}q={city}&appid={api_key}&units=metric&lang=tr"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperatures.append(data["main"]["temp"])
    else:
        print(f"{city} Data could not be obtained for.")


plt.figure(figsize=(10, 6))
plt.plot(cities, temperatures, marker="o", linestyle="-", color="b")
plt.title("instantaneous temperature of cities", fontsize=16)
plt.xlabel("Cities", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.grid(True)
plt.show()
