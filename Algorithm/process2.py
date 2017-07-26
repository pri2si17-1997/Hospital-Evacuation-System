import os
import io
import json
import gmplot
import folium
from collections import Counter
from pprint import pprint
def roundd(x):
	return float("{0:.5f}".format(str(x)))


with open('filter1.txt','r') as myfile:
	result_set1=json.load(myfile)
	

with open('filter2.txt','r') as myfile:
	result_set2=json.load(myfile)

#pprint(result_set2[0])
#pprint(result_set1[0])
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

map_1 = folium.Map(location=[28.629959389838543, 77.37181663513184], zoom_start=12)
folium.Marker([28.629959389838543, 77.37181663513184 ],icon = folium.Icon(color ='green') , popup='MY Current Location').add_to(map_1)
curent_dir = os.getcwd()
final_dir = 'Reviews'
working_dir = os.path.join(curent_dir, final_dir)
print(working_dir)
for i in cord:
	folium.Marker([float(i[0]),float(i[1]) ], popup=i[2]).add_to(map_1)
for i in range(0, len(final_rs)):
	folium.Marker([float(final_rs[i][1]),float(final_rs[i][2]) ],icon = folium.Icon(color ='red') ,popup=final_rs[i][0]).add_to(map_1)
	print(final_rs[i][0])
	sample_dir = os.path.join(working_dir, final_rs[i][0])
	print(sample_dir)
	with open(os.path.join(sample_dir, 'AspectOpinionResult.txt'),'r') as data:
		d=data.readlines()
		print(d)

	

map_1.save('mthood.html')
