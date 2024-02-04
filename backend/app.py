from tkinter import N
from flask import Flask, jsonify
from dotenv import load_dotenv
from geopy.geocoders import GoogleV3
from flask_cors import CORS
from geopy.distance import geodesic
import os
#import openai
import json
import requests
app=Flask(__name__)
CORS(app)
load_dotenv()
geolocator = GoogleV3(api_key='AIzaSyDfCBbLpQ4gA5irk6up5IpvC2XNXOECoi4')

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

@app.route('/distance', methods=['GET'])
def get_distance():
    return jsonify({"distance": distance_str})

@app.route('/carbon_emission',methods=['GET'])
def get_carbon_weight():
    return jsonify({"carbon": carbon_fp})

app.run(debug=False)