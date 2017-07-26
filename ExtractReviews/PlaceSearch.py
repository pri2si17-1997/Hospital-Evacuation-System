#Importing Necessary Libraries
import json
import pprint
import io
import os
import os.path
import time

#Importing self-made class
import googleVariables
import placeSearchRequest
import writeFile
import makeSearchQueries

googleConstants = googleVariables.googleVar() #creating instance of googleVar class
def getGoogleConstants():
	global googleApiKey
	global googlePlaceSearchBaseUrl
	googleApiKey = googleConstants._API_KEY
	googleConstants.getPlaceSearchUrl()
	googlePlaceSearchBaseUrl = googleConstants._placeSearchBaseURL

def getNextPageToken(json_data):
	return json_data['next_page_token']

def writePlaceSearchDataIntoFile(fileName, fileType, data, placeSearch = True, placeDetails = False, reviews = False):
	writeInFileObject = writeFile.fileWrite(fileName)
	directoryName = writeInFileObject.createDirectory(placeSearch, placeDetails, reviews)
	print(directoryName)
	writeInFileObject.writeDataInFile(fileType, directoryName, data)

def getFileNameCreated(searchQuery, index, responseFrom = 'googleResponse'):
	return searchQuery + ' ' + responseFrom + ' ' + str(index)

def makeRequest(query):
	global searchType
	fileType = 'json'
	searchType = 'hospital'
	searchQuery = query
	googlePlaceSearchRequestObject = placeSearchRequest.placeRequest(searchQuery, searchType)
	requestURL = googlePlaceSearchRequestObject.formURL(googlePlaceSearchBaseUrl, googleApiKey)
	print("Request URL : ")
	print(requestURL)
	requestData = googlePlaceSearchRequestObject.makeHTTPRequest(requestURL)
	json_data = requestData.json()
	print("Data Received : ")
	pprint.pprint(json_data)
	indexFile = 1
	fileName = getFileNameCreated(searchQuery, indexFile)
	writePlaceSearchDataIntoFile(fileName, fileType, json_data)
	while True:
		try:
			indexFile += 1
			#print("Index : " , indexFile)
			nextPageToken = getNextPageToken(json_data)
			print("Next Page Token : ")
			print(nextPageToken)
			requestURL = googlePlaceSearchRequestObject.formURL(googlePlaceSearchBaseUrl, googleApiKey, nextPageToken)
			print("Request URL : ")
			print(requestURL)
			time.sleep(5)
			requestData = googlePlaceSearchRequestObject.makeHTTPRequest(requestURL)
			json_data = requestData.json()
			print("Data Received : ")
			pprint.pprint(json_data)
			fileName = getFileNameCreated(searchQuery, indexFile)
			writePlaceSearchDataIntoFile(fileName, fileType, json_data)
		except KeyError:
			print('Got Key Error Exception')
			break
	print('Out Of Loop')

if __name__ == "__main__":
	searchQueryInstance = makeSearchQueries.searchQuery('localhost', 27017)
	searchQueryInstance.fetchDistricts()
	searchQueryInstance.makeQueryList()
	queryList = searchQueryInstance._queryList
	queryList.append('Hospitals in Delhi NCR')
	#pprint.pprint(queryList)
	#print(len(queryList))
	getGoogleConstants()
	for query in queryList:
		time.sleep(2)
		makeRequest(query)
	#makeRequest()
