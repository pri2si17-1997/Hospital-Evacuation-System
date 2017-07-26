import os
import io
import json
import pprint

class ReadDirectory():
	def __init__(self, directory):
		self._currentDir = os.getcwd()
		self._directoryName = os.path.join(self._currentDir, directory)
		self._dirList = []

	def readDirectory(self):
		for dirName in os.listdir(self._directoryName):
			self._dirList.append(dirName)
		self._dirList.remove('.json')

#instanceReadDirectory = ReadDirectory('../../ExtractReviews/Reviews/')
#instanceReadDirectory.readDirectory()
#pprint.pprint(instanceReadDirectory._dirList)
