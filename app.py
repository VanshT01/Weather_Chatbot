from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import requests

# Azure AI credentials
AZURE_KEY = "e39c882a08824e4dbe01ea66e80b1307"
AZURE_ENDPOINT = "https://vanshtalrejals.openai.azure.com/"

# OpenWeatherMap API key
WEATHER_API_KEY = '0805788370e1bb9dbb324f76d5ce39c3'

# Authenticate Azure AI Text Analytics client
def authenticate_client():
    ta_credential = AzureKeyCredential(AZURE_KEY)
    text_analytics_client = TextAnalyticsClient(endpoint=AZURE_ENDPOINT, credential=ta_credential)
    return text_analytics_client

# Extract city name from user query using Azure AI
def extract_city(client, text):
    response = client.recognize_entities(documents=[text])[0]
    cities = [entity.text for entity in response.entities if entity.category == 'Location']
    return cities[0] if cities else None

# Fetch weather data from OpenWeatherMap using latitude and longitude
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": data['main']['temp'],
            "weather_description": data['weather'][0]['description']
        }
    else:
        return {"error": "City not found"}

# Main function to handle the process
def get_city_weather(user_query):
    client = authenticate_client()
    city = extract_city(client, user_query)
    
    if city:
        weather_data = get_weather(city)
        return {
            "city": city,
            "weather": weather_data
        }
    else:
        return {"error": "No city found in the query"}

# Example user query
user_query = "What's the weather like in Amherst, MA?"

# Run the function and print the result
result = get_city_weather(user_query)
print(result)
