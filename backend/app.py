from tkinter import N
from flask import Flask
from dotenv import load_dotenv
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic
import os
#import openai
import json
import requests

load_dotenv()
# geolocator = GoogleV3(api_key='AIzaSyDfCBbLpQ4gA5irk6up5IpvC2XNXOECoi4')
# location = geolocator.geocode(user_input)

#openai.api_key = os.getenv("GPT_KEY")
GOOGLE_CLOUD_API = os.getenv('GOOGLE_CLOUD_API')
geolocator = GoogleV3(api_key=GOOGLE_CLOUD_API)

# print(f"latitude : {location.latitude} longitude : {location.longitude}")

API_URL = "https://civicinfo.googleapis.com/civicinfo/v2/representatives?address="
address = "11203"

# query = API_URL + address +  "&key=" + GOOGLE_CLOUD_API

# response = requests.get(query).json()

# print(response)
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

# carbon_url= 'https://www.carboninterface.com/api/v1/estimates'
# carbon_headers ={ 'Authorization': 'Bearer kl1r8VkxPP2a6t3qw1cBQ',
#           'Content-Type': 'application/json'}

# test_carbon_data={
#       "type": "shipping",
#       "weight_value": 200,
#       "weight_unit": "kg",
#       "distance_value": 20000,
#       "distance_unit": "km",
#       "transport_method": "truck"
# }
# carbon_response = requests.post(url=carbon_url, json=test_carbon_data, headers=carbon_headers)
# print(carbon_response.json())
@app.route('/shipping/<zipcode>')
def func(zipcode):
    return zipcode

@app.route('/')
def hello():
    return "wassup"
app.run(debug=False)