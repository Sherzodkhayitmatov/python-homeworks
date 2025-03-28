from bs4 import BeautifulSoup

with open(r"D:\python\python-homeworks\weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

    
rows = soup.find("table").find("tbody").find_all("tr")

weather_data = []

for row in rows:
    cols = row.find_all("td")
    day = cols[0].text.strip()
    temp = int(cols[1].text.strip().replace("°C", ""))
    condition = cols[2].text.strip()
    weather_data.append((day, temp, condition))
    
print("5-days weather forecast:")
for day, temp, condition in weather_data:
    print(f"{day}: {temp}°C, {condition}")
    
highest_temp = max(weather_data, key=lambda x: x[1])
print(f"\nHighest temperature is {highest_temp}°C.")

sunny_days = [day for day, temp, condition in weather_data if condition =="Sunny"]
print(f"\nSunny days:", ", ".join(sunny_days))

avg_temp = sum(temp for _, temp, in weather_data) / len(weather_data)
print(f"Average weather: {avg_temp}°C")


    