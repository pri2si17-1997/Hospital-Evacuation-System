import json
import googlemaps
import requests
from googlemaps import Client
from datetime import datetime
from collections import Counter


gmaps=googlemaps.Client(key='AIzaSyB7hXzGzrXUuQuPReZlERvxZO9YFakIzVw')
with open('list.txt','r') as myfile:
 place= myfile.readlines();
 print place[0]
 lent=len(place)
 for i in range(0,lent): 
  geocode_result=gmaps.geocode(place[i])
 #print geocode_result
  if not geocode_result:
   print 'No results Found'
  else:
    with open('somefile2.txt', 'a') as the_file:
     lat=geocode_result[0]['geometry']['location']['lat']
     lon=geocode_result[0]['geometry']['location']['lng']
     the_file.write(str(lat))
     the_file.write(',')
     the_file.write(str(lon)+"\n")
     print(lat,lon) 
   
 
