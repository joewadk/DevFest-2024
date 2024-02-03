from flask import Flask
from dotenv import load_dotenv
import requests
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic
import os
from datetime import datetime
app= Flask(__name__)

load_dotenv()
GOOGLE_CLOUD_API = os.getenv('GOOGLE_CLOUD_API')
geolocator = GoogleV3(api_key=GOOGLE_CLOUD_API)

startDest = geolocator.geocode(input("Start "))
endDest = geolocator.geocode(input("End "))

startCoords = (startDest.latitude, startDest.longitude)
endCoords = (endDest.latitude, endDest.longitude)

distance = geodesic(startCoords, endCoords).miles
print(distance)