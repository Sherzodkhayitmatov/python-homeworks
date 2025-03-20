{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Failed to get data. Error code: 401\n",
      "Response: {\"cod\":401, \"message\": \"Invalid API key. Please see https://openweathermap.org/faq#error401 for more info.\"}\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "api_key = \"b8afa482baeff8036d291c512f7199cf\"\n",
    "city = \"Tashkent\"\n",
    "url = f\"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric\"\n",
    "\n",
    "response = requests.get(url)\n",
    "\n",
    "if response.status_code == 200:\n",
    "    data = response.json()\n",
    "    \n",
    "    temperature = data[\"main\"][\"temp\"]\n",
    "    humidity = data[\"main\"][\"humidity\"]\n",
    "    weather_description = data[\"weather\"][0][\"description\"]\n",
    "    wind_speed = data[\"wind\"][\"speed\"]\n",
    "      \n",
    "    print(f\"Weather in {city}:\")\n",
    "    print(f\"Temperature: {temperature}°C\")\n",
    "    print(f\"Humidity: {humidity}%\")\n",
    "    print(f\"Condition: {weather_description.capitalize()}\")\n",
    "    print(f\"Wind Speed: {wind_speed} m/s\")\n",
    "      \n",
    "else:\n",
    "    print(f\"Failed to get data. Error code: {response.status_code}\")\n",
    "    print(f\"Response: {response.text}\") \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
