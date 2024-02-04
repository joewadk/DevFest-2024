from tkinter import N
from flask import Flask
from dotenv import load_dotenv
import requests
from geopy.geocoders import GoogleV3
import os
from datetime import datetime
app = Flask(__name__)

load_dotenv()
# geolocator = GoogleV3(api_key='AIzaSyDfCBbLpQ4gA5irk6up5IpvC2XNXOECoi4')
# location = geolocator.geocode(user_input)

# print(f"latitude : {location.latitude} longitude : {location.longitude}")

API_URL = "https://civicinfo.googleapis.com/civicinfo/v2/representatives?address="
address = "11203"

# query = API_URL + address +  "&key=" + GOOGLE_CLOUD_API

# response = requests.get(query).json()

# print(response)

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