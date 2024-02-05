from tkinter import N
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from geopy.geocoders import GoogleV3
from flask_cors import CORS
from geopy.distance import geodesic
import os
# import openai
import json
import requests
app = Flask(__name__)
CORS(app)
load_dotenv()

# openai.api_key = os.getenv("GPT_KEY")
GOOGLE_CLOUD_API = os.getenv('GOOGLE_CLOUD_API')
geolocator = GoogleV3(api_key=GOOGLE_CLOUD_API)

CARBON_KEY = os.getenv('CARBON_KEY')
url = 'https://www.carboninterface.com/api/v1/estimates'

headers = {
    'Authorization': f'Bearer {CARBON_KEY}',
    'Content-Type': 'application/json',
}


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/carbon_emission', methods=['POST'])
def get_carbon_weight():
    request_data = request.get_json()
    startDest = geolocator.geocode(request_data['user_address'])
    endDest = geolocator.geocode(request_data['source_address'])
    weightItem = request_data['package_weight']

    startCoords = (startDest.latitude, startDest.longitude)
    endCoords = (endDest.latitude, endDest.longitude)
    distance = geodesic(startCoords, endCoords).miles
    distance_str = str(distance)

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
    return jsonify({"carbon": carbon_fp})

app.run(debug=True)
