#!/usr/bin/env python3

#imports
import requests
import datetime  
import reverse_geocoder as rg

#response from api
response_iss = requests.get("http://api.open-notify.org/iss-now.json").json()

#time conversion
epoch_time = response_iss["timestamp"]
date_time = datetime.datetime.fromtimestamp( epoch_time )

#position
lat = response_iss["iss_position"]["latitude"]
lon = response_iss["iss_position"]["longitude"]

#city/country
coords_tuple= (lat, lon)
result_rg = rg.search(coords_tuple, verbose=False)
city = result_rg[0]["name"]
country = result_rg[0]["cc"]

#final product 
print(f"CURRENT LOCATION OF THE ISS: \nTimestamp: {date_time} \nLon: {lon} \nLat: {lat} \nCity/Country: {city}, {country}")


