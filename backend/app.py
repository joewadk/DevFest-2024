from tkinter import N
from flask import Flask
from dotenv import load_dotenv
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic
import os
#import openai
import json
import requests
app=Flask(__name__)
load_dotenv()
geolocator = GoogleV3(api_key='<google-api>')

#openai.api_key = os.getenv("GPT_KEY")
GOOGLE_CLOUD_API = os.getenv('GOOGLE_CLOUD_API')
geolocator = GoogleV3(api_key=GOOGLE_CLOUD_API)

startDest = geolocator.geocode(input("Start "))
endDest = geolocator.geocode(input("End "))
weightItem = input("State the weight of your item ")

startCoords = (startDest.latitude, startDest.longitude)
endCoords = (endDest.latitude, endDest.longitude)
distance = geodesic(startCoords, endCoords).miles
distance_str = str(distance)

CARBON_KEY = os.getenv('CARBON_KEY')

url = 'https://www.carboninterface.com/api/v1/estimates'

headers = {
    'Authorization': f'Bearer {CARBON_KEY}',
    'Content-Type': 'application/json',
}

data = {
    "type": "shipping",
    "weight_value": int(weightItem),
    "weight_unit": "lb",
    "distance_value": distance,
    "distance_unit": "mi",
    "transport_method": "truck"
}

response = requests.post(url, headers=headers, data=json.dumps(data))
carbon_fp = response.json()['data']['attributes']['carbon_lb']
print(carbon_fp)

# carbon_url= 'https://www.carboninterface.com/api/v1/estimates'
# carbon_headers ={ 'Authorization': 'Bearer <carbon api key>',
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

@app.route('/distance')
def distance():
    return distance_str

@app.route('/carbon_emission')
def carbon_weight():
    return str(carbon_fp)

app.run(debug=False)