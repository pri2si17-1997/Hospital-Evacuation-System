import nltk
import os
import io
import ast
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet
import loadData
import uuid
import pprint

class TokenizeData():
	def __init__(self, textData):
		self._tokenizedReview = {}
		self._text = textData
		self._tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
		self._stopWords = nltk.corpus.stopwords.words("english")
		self._uniqueId = 1
	
	def tokenizeReview(self):
		for index in range(0, len(self._text)):
			for sentence in self._tokenizer.tokenize(self._text[index]):
				self._tokenizedReview[self._uniqueId] = sentence
				self._uniqueId += 1

	def writeInFile(self, parentDirectory):
		outputFile = open(os.path.join(parentDirectory, 'TokenizedData.txt'), 'w')
		outputFile.write(str(self._tokenizedReview))
		outputFile.close()
	
#instanceLoadData = loadData.LoadData('../../ExtractReviews/')
#instanceLoadData.openFile('HospitalReviews.txt')
#instanceLoadData.readText()
#instanceLoadData.closeFile()

#instanceTokenizeData = TokenizeData(instanceLoadData._text)
#instanceTokenizeData.tokenizeReview()
#instanceTokenizeData.writeInFile('../../ExtractReviews/')
#pprint.pprint(instanceTokenizeData._tokenizedReview)



