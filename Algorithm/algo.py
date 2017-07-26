# Imports 
import json
import googlemaps
import requests
from googlemaps import Client
from datetime import datetime
from collections import Counter


gmaps=googlemaps.Client(key='AIzaSyB7hXzGzrXUuQuPReZlERvxZO9YFakIzVw')
place=raw_input('Enter the Place You want to search : ')
geocode_result=gmaps.geocode(place)
#print geocode_result
if not geocode_result:
 print 'No results Found'
else:
 lat=geocode_result[0]['geometry']['location']['lat']
 lon=geocode_result[0]['geometry']['location']['lng']
 poi=geocode_result[0]
 print lat 
 print lon
 #print poi


now = datetime.now()
direction_result = gmaps.directions("A-10,JIIT Noida, sector-62, Noida","9, Vaibhav Khand, Indirapuram, Ghaziabad, Uttar Pradesh 201014, India",mode="transit",departure_time=now)
##print direction_result

distance=direction_result[0]['legs'][0]['distance']
end_address=direction_result[0]['legs'][0]['end_address']
travel_mode=direction_result[0]['legs'][0]['steps'][0]['travel_mode']
instructions=direction_result[0]['legs'][0]['steps'][0]['html_instructions']
duration=direction_result[0]['legs'][0]['steps'][0]['duration']


## Directions
num_steps=len(direction_result[0]['legs'][0]['steps'][0]['steps'])
for i in range(0,num_steps):
 print direction_result[0]['legs'][0]['steps'][0]['steps'][i]['html_instructions']
 print direction_result[0]['legs'][0]['steps'][0]['steps'][i]['distance']
 print direction_result[0]['legs'][0]['steps'][0]['steps'][i]['duration'] 









 

