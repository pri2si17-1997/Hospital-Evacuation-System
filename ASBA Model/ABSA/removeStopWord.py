import nltk
import ast
import re
import pprint
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet

import loadData

class RemoveStopWord():
	def __init__(self, textData):
		self._stopWords = nltk.corpus.stopwords.words("english")
		self._result = None
		self._text = textData

	def removeStopWord(self):
		self._stopWords.append('OMG')
		self._stopWords.append(':-)')
		for index in range(0, len(self._text)):
			for word in self._text[index].split():
				#print(word)
				if word not in self._stopWords:
					self._result = ''.join(word)
	

instanceLoadData = loadData.LoadData('../../ExtractReviews/')
instanceLoadData.openFile('HospitalReviews.txt')
instanceLoadData.readText()
instanceLoadData.closeFile()

instanceRemveStopWord = RemoveStopWord(instanceLoadData._text)
instanceRemveStopWord.removeStopWord()
#pprint.pprint(instanceRemveStopWord._stopWords)
#pprint.pprint(instanceRemveStopWord._result)
#print(instanceRemveStopWord._stopWords)
#print(instanceRemveStopWord._result)
