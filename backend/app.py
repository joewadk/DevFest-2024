from dotenv import load_dotenv
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic
import os
import openai
import json
import requests

load_dotenv()

openai.api_key = os.getenv("GPT_KEY")
GOOGLE_CLOUD_API = os.getenv('GOOGLE_CLOUD_API')
geolocator = GoogleV3(api_key=GOOGLE_CLOUD_API)

startDest = geolocator.geocode(input("Start "))
endDest = geolocator.geocode(input("End "))

startCoords = (startDest.latitude, startDest.longitude)
endCoords = (endDest.latitude, endDest.longitude)
distance = geodesic(startCoords, endCoords).miles

CARBON_KEY = os.getenv('CARBON_KEY')

url = 'https://www.carboninterface.com/api/v1/estimates'

headers = {
    'Authorization': f'Bearer {CARBON_KEY}',
    'Content-Type': 'application/json',
}

data = {
    "type": "shipping",
    "weight_value": 100,
    "weight_unit": "lb",
    "distance_value": distance,
    "distance_unit": "mi",
    "transport_method": "truck"
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json()['data']['attributes']['carbon_lb'])
