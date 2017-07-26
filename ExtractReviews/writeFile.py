#import necessary libraries
import os
import os.path
import shutil 
import json

class fileWrite:
	def __init__(self, fileName):
		self._fileName = fileName

	def createDirectory(self, placeSearch, placeDetails, reviews):
		current_dir = os.getcwd()
		if placeDetails is True and placeSearch is False and reviews is False:
			#directory_name = r'PlaceSearchDirectory'
			directory_name = r'PlaceDetailsDirectory'
			final_dir = os.path.join(current_dir, directory_name)
			if os.path.exists(final_dir):
				#shutil.rmtree(final_dir)
				#os.makedirs(final_dir)
				return directory_name
			else:
				os.makedirs(final_dir)
				return directory_name

		elif placeSearch is True and placeDetails is False and reviews is False:
			#directory_name = r'PlaceDetailsDirectory'
			directory_name = r'PlaceSearchDirectory'
			final_dir = os.path.join(current_dir, directory_name)
			if os.path.exists(final_dir):
				#shutil.rmtree(final_dir)
				#os.makedirs(final_dir)
				return directory_name
			else:
				os.makedirs(final_dir)
				return directory_name

		elif reviews is True:
			directory_name = r'Reviews'
			final_dir = os.path.join(current_dir, directory_name)
			if os.path.exists(final_dir):
				#shutil.rmtree(final_dir)
				#os.makedirs(final_dir)
				return directory_name
			else:
				os.makedirs(final_dir)
				return directory_name
	
	def createPlaceDetailsDirectory(self):
		current_dir = os.getcwd()
		directory_name = r'PlaceDetailsDirectory'
		final_dir = os.path.join(current_dir, directory_name)
		if os.path.exists(final_dir):
			return directory_name
		else:
			os.makedirs(final_dir)
			return directory_name

	def writeDataInFile(self, fileType, directoryName, data):
		if fileType == 'text':
			fileToWrite = directoryName + "/" + self._fileName + ".txt"
			try:
				#with open(fileToWrite, 'w') as responseFile:
				#responseFile.write(data)
				os.remove(fileToWrite)
			except OSError:
				pass
				#print('Exception Caught. Writing To File Failed.')
			with open(fileToWrite, 'w') as responseFile:
				responseFile.write(data)

		elif fileType == 'json':
			fileToWrite = directoryName + "/" + self._fileName + ".json"
			try:
				#with open(fileToWrite, 'w') as responseFile:
				#	json.dump(json_data, responseFile)
				os.remove(fileToWrite)
			except IOError:
				pass
				#print('Exception Caught. Writing To File Failed.')
			with open(fileToWrite, 'w') as responseFile:
				json.dump(data, responseFile)

