import nltk
import os
import io
import ast
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet
#import loadData
#import tokenizeReviews
import uuid
import pprint

class POSTagging():
	def __init__(self):
		#self._text = textData;
		self._file = None
		self._inputTuples = None
		self._outputPOSTag = {}

	def openFile(self, directoryName):
		self._file = open(os.path.join(directoryName, 'TokenizedData.txt'), 'r').read()
	
	def posTagging(self):
		#for index in range(0, len(self._tokenizedData)):
		inputTupples = ast.literal_eval(self._file)
		for key, value in inputTupples.items():
			self._outputPOSTag[key] = nltk.pos_tag(nltk.word_tokenize(value))
	
	def closeFile(self):
		self._file.close()

	def writeInFile(self, directoryName):
		outputFile = open(os.path.join(directoryName, 'POSTagged.txt'), 'w')
		outputFile.write(str(self._outputPOSTag))
		outputFile.close()


#instancePOSTag = POSTagging()
#instancePOSTag.openFile('../../ExtractReviews/')
#instancePOSTag.posTagging()
#instancePOSTag.closeFile()
#pprint.pprint(instancePOSTag._outputPOSTag)
#instancePOSTag.writeInFile('../../ExtractReviews/')


	
	
