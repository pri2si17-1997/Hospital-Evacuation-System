#importing necessary libraries
import io
import json
import pprint
import os
import os.path
import time
import operator

#importing self-made class
import googleVariables
import writeFile
import placeDetailsRequest

googleConstants = googleVariables.googleVar()

def getGoogleConstants():
	global googleApiKey
	global googlePlaceDetailsBaseUrl
	googleApiKey = googleConstants._API_KEY
	googleConstants.getPlaceDetailsBaseUrl()
	googlePlaceDetailsBaseUrl = googleConstants._placeDetailsBaseURL

def writePlaceDetailsDataInFile(fileName, fileType, data):
	writeInFileObject = writeFile.fileWrite(fileName)
	directoryName = writeInFileObject.createPlaceDetailsDirectory()
	print(directoryName)
	writeInFileObject.writeDataInFile(fileType, directoryName, data)

def makeRequest(hospitalName, placeID):
	fileType = 'json'
	googlePlaceDetailsRequestObject = placeDetailsRequest.placeDetails(placeID)
	requestURL = googlePlaceDetailsRequestObject.formURL(googlePlaceDetailsBaseUrl, googleApiKey)
	print(requestURL)
	requestDATA = googlePlaceDetailsRequestObject.makeHTTPRequest(requestURL)
	json_res = requestDATA.json()
	pprint.pprint(json_res)
	writePlaceDetailsDataInFile(hospitalName, fileType, json_res)

def getPlaceIdNameList():
	global placeIDNameList
	placeIDNameList = []
	directoryName = 'PlaceSearchDirectory/'
	fileList = os.listdir(directoryName)
	for files in fileList:
		file_to_read = open(directoryName + files, 'r')
		json_data = json.load(file_to_read)
		for result in json_data['results']:
			placeIDNameList.append({'placeId' : result['place_id'],
						'hospitalName' : result['name']})
				
if __name__ == "__main__":
	getGoogleConstants()
	getPlaceIdNameList()
	#pprint.pprint(placeIDNameList)
	#print(len(placeIDNameList))
	#print(placeIDNameList[0])
	index = 0
	for records in placeIDNameList:
		print(index)
		print(records)
		index += 1
		time.sleep(0.5)
	#	makeRequest(records['hospitalName'], records['placeId'])
	#	time.sleep(2)
	
			

