from flask import Flask
from dotenv import load_dotenv
import requests
from geopy.geocoders import GoogleV3
import os
from datetime import datetime
app= Flask(__name__)

load_dotenv()
GOOGLE_CLOUD_API = os.getenv('GOOGLE_CLOUD_API')
geolocator = GoogleV3(api_key=GOOGLE_CLOUD_API)

user_input=input("Upload Zip Code ")
location = geolocator.geocode(user_input)

print(f"latitude : {location.latitude} longitude : {location.longitude}")

API_URL = "https://civicinfo.googleapis.com/civicinfo/v2/representatives?address="
address = "11203"

query = API_URL + address +  "&key=" + GOOGLE_CLOUD_API

response = requests.get(query).json()

#print(response)
