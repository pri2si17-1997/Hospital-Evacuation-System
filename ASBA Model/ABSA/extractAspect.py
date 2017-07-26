import os
import io
import nltk
import ast
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet
#import loadData
#import tokenizeReviews
import uuid
import pprint

class ExtractAspect():
	def __init__(self):
		self._file = None
		self._previousWord = ''
		self._previousTag = ''
		self._currentWord = ''
		self._aspectList = []
		self._outputDict = {}
		self._inputTupples = None
		self._outputAspect = None
	
	def openFile(self, directoryName):
		self._file = open(os.path.join(directoryName, 'POSTagged.txt'), 'r').read()
		
	def extractAspect(self):
		self._inputTupples = ast.literal_eval(self._file)
		for key, value in self._inputTupples.items():
			for word, tag in value:
				if(tag == 'NN' or tag == 'NNP'):
					if(self._previousTag == 'NN' or self._previousTag == 'NNP'):
						self._currentWord = self._previousWord + ' ' + word
					else:
						self._aspectList.append(self._previousWord.upper())
						self._currentWord = word
				
				self._previousWord = self._currentWord
				self._previousTag = tag
		
		for aspect in self._aspectList:
			if(self._aspectList.count(aspect) > 1): 
				if(self._outputDict.keys() != aspect):
					self._outputDict[aspect] = self._aspectList.count(aspect)

		self._outputAspect = sorted(self._outputDict.items(), key = lambda x: x[1], reverse = True)

	def closeFile(self):
		self._file.close()

	def writeInFile(self, directoryName):
		outputFile = open(os.path.join(directoryName, 'AspectData.txt'), 'w')
		outputFile.write(str(self._outputAspect))
		outputFile.close()

#instanceExtractAspect = ExtractAspect()
#instanceExtractAspect.openFile('../../ExtractReviews/')
#instanceExtractAspect.extractAspect()
#pprint.pprint(instanceExtractAspect._outputAspect)
#instanceExtractAspect.writeInFile('../../ExtractReviews/')
#instanceExtractAspect.closeFile()
