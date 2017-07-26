import os
import io
import json
import pprint

class ReadFiles():
	def __init__(self, directory):
		self._currentDirectory = os.getcwd()
		self._directoryName = os.path.join(self._currentDirectory, directory)
		#self._directoryName = directory
		self._fileList = []
		self._reviewTextFile = open('HospitalReviews.txt', 'a')

	def readAllFIles(self):
		for fileName in os.listdir(self._directoryName):
			#print(fileName)
			self._fileList.append(fileName)

	def loadJson(self, fileName):
		with open(os.path.join(self._directoryName, fileName)) as data_file:
			json_data = json.load(data_file)
		#pprint.pprint(json_data)
		return json_data

	def getLatitude(self, json_data):
		try:
			return json_data['result']['geometry']['location']['lat']
		except KeyError:
			print('KeyError Received', KeyError)
			return ''

	def getLongitude(self, json_data):
		try:
			return json_data['result']['geometry']['location']['lng']
		except KeyError:
			print('KeyError Received', KeyError)
			return ''

	def getId(self, json_data):
		try:
			return json_data['result']['id']
		except KeyError:
			print('KeyError Received', KeyError)
			return ''

	def getName(self, json_data):
		try:
			return json_data['result']['name']
		except KeyError:
			print('KeyError Received', KeyError)
			return ''

	def getInternationalPhoneNumber(self, json_data):
		try:
			return json_data['result']['international_phone_number']
		except KeyError:
			print('KeyError Received', KeyError)
			return ''

	def getRating(self, json_data):
		try:
			return json_data['result']['rating']
		except KeyError:
			print('KeyError Received', KeyError)
			return ''

	def getAddress(self, json_data):
		try:
			return json_data['result']['formatted_address']
		except KeyError:
			print('KeyError Received', KeyError)
			return ''
	
	def getReviews(self, json_data):
		listReviews = []
		try:
			for data in json_data['result']['reviews']:
				listReviews.append({
							'id' : data['time'],
							'Review' : data['text']
							})
			return listReviews
		except KeyError:
			pass
			return listReviews

	def createReviewTextFile(self, json_data):
		try:
			for data in json_data['result']['reviews']:
				if data['text'] != '':
					self._reviewTextFile.write(data['text'] + '\n')
		except KeyError:
			pass
	
	def createJsonFile(self, data):
		with open('hospitalSearchIndex.json', 'w') as outFile:
			json.dump(data, outFile)

	def createDirectory(self, directoryName):
		finalDir = os.path.join(self._currentDirectory, directoryName)
		if os.path.exists(finalDir):
			return directoryName
		else:
			os.makedirs(finalDir)
			return directoryName

	def reviewTextFile(self, directoryName, json_data):
		try:
			with open(os.path.join(directoryName, 'reviews.txt'), 'w') as reviewFile:
				for data in json_data['result']['reviews']:
                        		if data['text'] != '':
                                		reviewFile.write(data['text'] + '\n')
			reviewFile.close()
		except KeyError:
			pass


instanceReadFile = ReadFiles('PlaceDetailsDirectory')
instanceReadFile.readAllFIles()
DirectoryName = instanceReadFile.createDirectory('Reviews')
print(DirectoryName)

hospitalDetailsNCR = []

for index in range(0, len(instanceReadFile._fileList)):
	print("Process Number : ", index)
	hospitalInfo = []
	#hospitalDetailsNCR = []
	file_info = instanceReadFile.loadJson(instanceReadFile._fileList[index])
	hospitalInfo.append({
				'hospital_name' : instanceReadFile.getName(file_info),
				'hospital_id' : instanceReadFile.getId(file_info),
				'international_phone_number' : instanceReadFile.getInternationalPhoneNumber(file_info),
				'rating' : instanceReadFile.getRating(file_info),
				'address' : instanceReadFile.getAddress(file_info),
				'latitude' : instanceReadFile.getLatitude(file_info),
				'longitude' : instanceReadFile.getLongitude(file_info),
				'reviews' : instanceReadFile.getReviews(file_info)
				})

	hospitalDetailsNCR.append({
					'hospital_name' : instanceReadFile.getName(file_info),
					'latitude' : instanceReadFile.getLatitude(file_info),
					'longitude' : instanceReadFile.getLongitude(file_info)
					})
	#pprint.pprint(hospitalInfo)
	#DirName = instanceReadFile.createDirectory(DirectoryName + '/' + instanceReadFile.getName(file_info))
	#with open(os.path.join(DirName, instanceReadFile.getName(file_info) + '.json'), 'w') as output_file:
	#	json.dump(hospitalInfo, output_file)
	#instanceReadFile.reviewTextFile(DirName, file_info)
	#instanceReadFile.createReviewTextFile(file_info)

pprint.pprint(hospitalDetailsNCR)
instanceReadFile.createJsonFile(hospitalDetailsNCR)
