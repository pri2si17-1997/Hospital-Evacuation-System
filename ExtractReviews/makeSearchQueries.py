import pymongo
from pymongo import MongoClient
import pprint

class searchQuery:
	def __init__(self, serverName, portNo):
		self._dbClient = MongoClient(serverName, portNo)
		self._queryList = []
		self._districtList = []
		self._stateList = ['Uttar Pradesh', 'Haryana', 'Rajasthan', 'Delhi']
		self._prefix = 'Hospitals in '
		self._dbName = self._dbClient.DBMinor

	def fetchDistricts(self):
		collectionName = self._dbName.StateDistrictNCR
		for state in self._stateList:
			results = collectionName.find({"StateName" : state})
			for result in results:
				districts = result['Districts']
				for district in districts:
					self._districtList.append(district['districtName'])

	def makeQueryList(self):
		for district in self._districtList:
			self._queryList.append(self._prefix + district)

#Debugging Script
#searchQueryInstance = searchQuery('localhost', 27017)
#searchQueryInstance.fetchDistricts()
#searchQueryInstance.makeQueryList()
#print(searchQueryInstance._queryList)
#print(searchQueryInstance._dbName)
#print(searchQueryInstance._districtList)
