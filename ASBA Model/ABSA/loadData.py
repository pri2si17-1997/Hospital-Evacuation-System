import os
import sys
import pprint

class LoadData:
	def __init__(self, directoryName):
		self._dirName = directoryName
		self._text = []
		#self._sentence = []
		self._file = None
		self._negFile = None
		self._negWord = []

	def openFile(self, fileName):
		self._file = open(os.path.join(self._dirName, fileName), 'r')
		self._negFile = open('negative_word.txt', 'r')

	def readText(self):
		for line in self._file:
			line = line.replace('#', '')
			line = line.strip()
			self._text.append(line)

	def readNegativeWord(self):
		for line in self._negFile:
			line = line.strip()
			self._negWord.append(line)	

	def closeFile(self):
		self._file.close()
		self._negFile.close()

#instanceLoadData = LoadData('../../ExtractReviews/')
#instanceLoadData.openFile('HospitalReviews.txt')
#instanceLoadData.readText()
#instanceLoadData.readNegativeWord()
#pprint.pprint(instanceLoadData._text)
#pprint.pprint(instanceLoadData._negWord)
#instanceLoadData.closeFile()
