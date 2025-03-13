import requests

api_key = "b8afa482baeff8036d291c512f7199cf"
city = "Tashkent"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]
      
    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_description.capitalize()}")
    print(f"Wind Speed: {wind_speed} m/s")
      
else:
    print(f"Failed to get data. Error code: {response.status_code}")
    print(f"Response: {response.text}")
