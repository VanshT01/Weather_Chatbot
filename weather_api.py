import requests

# OpenWeatherMap API key
API_KEY = '0805788370e1bb9dbb324f76d5ce39c3'

# Fetch weather data from OpenWeatherMap using latitude and longitude
def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": data['current']['temp'],
            "weather_description": data['current']['weather'][0]['description'],
            "daily_forecast": data['daily'][0]['weather'][0]['description']  # Forecast for the next day
        }
    else:
        return {"error": "City not found"}
