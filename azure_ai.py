from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Azure credentials
key = "e39c882a08824e4dbe01ea66e80b1307"
endpoint = "https://vanshtalrejals.openai.azure.com/"

# Authenticate with Azure AI Text Analytics
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=ta_credential)
    return text_analytics_client

# Extract city name (entities) from user query using Azure AI
def extract_city(client, text):
    response = client.recognize_entities(documents=[text])[0]
    cities = [entity.text for entity in response.entities if entity.category == 'Location']
    return cities[0] if cities else None
