import urllib2
import json
from pprint import pprint
import requests
from googlemaps import Client
from datetime import datetime
from collections import Counter
import os
import io
import json
import gmplot
import folium


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

def filter1(key1,place):
	api_key='AIzaSyB7hXzGzrXUuQuPReZlERvxZO9YFakIzVw'
	#(input_lat,input_lng)= get_Lat_Lon()
	#(input_lat,input_lng)=get_Current_Location()
	#print input_lng, input_lat
	(input_lat,input_lng)=get_geopoints_byName(place)
	keyword=key1
	rad='30000'
	response= requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+str(input_lat)+','+str(input_lng)+'&radius='+rad+'&type=hospital&keyword='+keyword+'&key='+api_key)
	d= response.json()
	#print(len(d['results']))
	results=d['results']
	with open('filter1.txt', 'w') as outfile:
		json.dump(results, outfile)


def filter2(key1,place):
	api_key='AIzaSyB7hXzGzrXUuQuPReZlERvxZO9YFakIzVw'
	#(input_lat,input_lng)= get_Lat_Lon()
	#(input_lat,input_lng)=get_Current_Location()
	#print input_lng, input_lat
	(input_lat,input_lng)=get_geopoints_byName(place)
	keyword=key1
	rad='30000'
	response= requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+str(input_lat)+','+str(input_lng)+'&rankby=distance&type=hospital&keyword='+keyword+'&key='+api_key)
	d= response.json()
	#print(len(d['results']))
	results=d['results']
	with open('filter2.txt', 'w') as outfile:
		json.dump(results, outfile)


def get_geopoints_byName(place):
	gmaps=Client(key='AIzaSyB7hXzGzrXUuQuPReZlERvxZO9YFakIzVw')
	
	geocode_result=gmaps.geocode(place)
	#print geocode_result
	if not geocode_result:
		return (0,0)
	else:
		lat=geocode_result[0]['geometry']['location']['lat']
		lon=geocode_result[0]['geometry']['location']['lng']
		poi=geocode_result[0]
		return (lat,lon)


def get_directions(place,dest):
	gmaps=Client(key='AIzaSyB7hXzGzrXUuQuPReZlERvxZO9YFakIzVw')
	now = datetime.now()
	direction_result = gmaps.directions(place,dest,mode="transit",departure_time=now)
	##print direction_result
	distance=direction_result[0]['legs'][0]['distance']
	end_address=direction_result[0]['legs'][0]['end_address']
	travel_mode=direction_result[0]['legs'][0]['steps'][0]['travel_mode']
	instructions=direction_result[0]['legs'][0]['steps'][0]['html_instructions']
	duration=direction_result[0]['legs'][0]['steps'][0]['duration']
	str1=''
	num_steps=len(direction_result[0]['legs'][0]['steps'][0]['steps'])
	for i in range(0,num_steps):
		str1+=str(direction_result[0]['legs'][0]['steps'][0]['steps'][i]['html_instructions'])+'\n'
	return distance['text']+' '+duration['text']+' '+str1

place=raw_input('Enter the Place You want to search : ')
filter1('',place)
filter2('',place)



with open('filter1.txt','r') as myfile:
	result_set1=json.load(myfile)
	

with open('filter2.txt','r') as myfile:
	result_set2=json.load(myfile)


cord= []

for var in result_set1:
	cord.append( [ var['geometry']['location']['lat'],var['geometry']['location']['lng'],var['name'] ] )

for var in result_set2:
	cord.append( [ var['geometry']['location']['lat'],var['geometry']['location']['lng'],var['name'] ] )
count=0
for dif in cord:
	for var in cord:
		if(dif[0]==var[0]):
			count+=1
	dif.append(count)
	count=0
cord1=[]
d=set()
for i in cord:
	cord1.append(tuple(i))
	d.add(tuple(i))

#print(len(d))

'''map_1 = folium.Map(location=[28.629959389838543, 77.37181663513184], zoom_start=12)
folium.Marker([28.629959389838543, 77.37181663513184 ],icon = folium.Icon(color ='green') , popup='MY Current Location').add_to(map_1)
for i in cord:
	folium.Marker([float(i[0]),float(i[1]) ], popup=i[2]).add_to(map_1)

map_1.save('mthood.html')'''

with open('hospitalSearchIndex.json') as data_file:    
    data = json.load(data_file)

final_rs=[]
for i in data:
	for j in cord:
		if i['latitude']==j[0] and i['longitude']==j[1]:# and round(float(i['longitude']),5)==round(float(j[1]),5)):
			final_rs.append([ i['hospital_name'],j[0],j[1] ])
(slat,slon)= get_geopoints_byName(place)
map_1 = folium.Map(location=[slat, slon], zoom_start=12)
folium.Marker([slat, slon ],icon = folium.Icon(color ='green') , popup='MY Current Location').add_to(map_1)
curent_dir = os.getcwd()
final_dir = 'Reviews'
working_dir = os.path.join(curent_dir, final_dir)
print(working_dir)
for i in cord:
	folium.Marker([float(i[0]),float(i[1]) ], popup=i[2]).add_to(map_1)
for i in range(0, len(final_rs)):
	folium.Marker([float(final_rs[i][1]),float(final_rs[i][2]) ],icon = folium.Icon(color ='red') ,popup=final_rs[i][0]+' '+get_directions(place,final_rs[i][0])).add_to(map_1)
	print(final_rs[i][0])
	sample_dir = os.path.join(working_dir, final_rs[i][0])
	print(sample_dir)
	with open(os.path.join(sample_dir, 'AspectOpinionResult.txt'),'r') as data:
		d=data.readlines()
		print(d)

	

map_1.save('mthood1.html')
