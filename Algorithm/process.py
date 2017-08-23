import urllib2
import json
from pprint import pprint
import requests
from googlemaps import Client
from datetime import datetime
from collections import Counter
#from gmaps import gmaps
#from googleplaces import GooglePlaces, types, lang

def get_Current_Location():
	f = urllib2.urlopen('http://freegeoip.net/json/')
	json_string = f.read()
	f.close()
	location = json.loads(json_string)
	#pprint(location)
	lat=location['latitude']
	lng=location['longitude']
	location_city = location['city']
	location_state = location['region_name']
	location_country = location['country_name']
	#print location_city +','+location_state+','+location_country+','+str(lat)+','+str(lng)
	return (lat,lng)

def filter1(key1):
	api_key='AIzaSyB7hXzGzrXUuQuPReZlERvxZO9YFakIzVw'
	#(input_lat,input_lng)= get_Lat_Lon()
	(input_lat,input_lng)=get_Current_Location()
	#print input_lng, input_lat
	keyword=key1
	rad='30000'
	response= requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+str(input_lat)+','+str(input_lng)+'&radius='+rad+'&type=hospital&keyword='+keyword+'&key='+api_key)
	d= response.json()
	#print(len(d['results']))
	results=d['results']
	with open('filter1.txt', 'w') as outfile:
		json.dump(results, outfile)


def filter2(key1):
	api_key='AIzaSyB7hXzGzrXUuQuPReZlERvxZO9YFakIzVw'
	#(input_lat,input_lng)= get_Lat_Lon()
	(input_lat,input_lng)=get_Current_Location()
	#print input_lng, input_lat
	keyword=key1
	rad='30000'
	response= requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+str(input_lat)+','+str(input_lng)+'&rankby=distance&type=hospital&keyword='+keyword+'&key='+api_key)
	d= response.json()
	#print(len(d['results']))
	results=d['results']
	with open('filter2.txt', 'w') as outfile:
		json.dump(results, outfile)

def get_geopoints_byName():
	gmaps=Client(key='AIzaSyB7hXzGzrXUuQuPReZlERvxZO9YFakIzVw')
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


def get_directions():
	gmaps=Client(key='AIzaSyB7hXzGzrXUuQuPReZlERvxZO9YFakIzVw')
	now = datetime.now()
	direction_result = gmaps.directions("A-10,JIIT Noida, sector-62, Noida","9, Vaibhav Khand, Indirapuram, Ghaziabad, Uttar Pradesh 201014, India",mode="transit",departure_time=now)
	##print direction_result
	distance=direction_result[0]['legs'][0]['distance']
	end_address=direction_result[0]['legs'][0]['end_address']
	travel_mode=direction_result[0]['legs'][0]['steps'][0]['travel_mode']
	instructions=direction_result[0]['legs'][0]['steps'][0]['html_instructions']
	duration=direction_result[0]['legs'][0]['steps'][0]['duration']
	print distance['text'],duration['text']
	## Directions
	num_steps=len(direction_result[0]['legs'][0]['steps'][0]['steps'])
	str1=''
	for i in range(0,num_steps):
		str1+=str(direction_result[0]['legs'][0]['steps'][0]['steps'][i]['html_instructions'])+'\n'
		#print direction_result[0]['legs'][0]['steps'][0]['steps'][i]['distance']
		#print direction_result[0]['legs'][0]['steps'][0]['steps'][i]['duration']
	return str1 



print get_directions()
#filter2('')
###get_geopointsealth)