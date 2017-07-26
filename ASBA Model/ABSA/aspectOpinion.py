import os
import io
import nltk
import ast
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet
import loadData
import uuid
import pprint

class AspectOpinionMining():
	def __init__(self, negWordLst):
		self._POSTaggedFile = None
		self._AspectFile = None
		self._reviewsTupples = None
		self._aspectTupples = None
		self._aspectOpinionTupple = {}
		self._orientation = {}
		#self._negativeWordSet = {"don't", "never", "nothing", "nowhere", "noone", "none", "not", "hasn't","hadn't","can't","couldn't","shouldn't","won't", "wouldn't", "don't", "doesn't", "didn't", "isn't", "aren't", "ain't"}
		self._negativeWordSet = negWordLst

	def getOrientation(self, word):
		wordSynset = wordnet.synsets(word)
		if(len(wordSynset) != 0):
			word = wordSynset[0].name()
			orientation = sentiwordnet.senti_synset(word)
			if(orientation.pos_score() > orientation.neg_score()):
				return True
			else:	
				return False

	def openFiles(self, directoryName):
		self._POSTaggedFile = open(os.path.join(directoryName, 'POSTagged.txt') , 'r').read()
		self._AspectFile = open(os.path.join(directoryName, 'AspectData.txt') , 'r').read()

	def getAspectOpinion(self):	
		self._reviewsTupples = ast.literal_eval(self._POSTaggedFile)
		self._aspectTupples = ast.literal_eval(self._AspectFile)
		for aspect, number in self._aspectTupples:
			aspectTokens = word_tokenize(aspect)
			count = 0
			for key, value in self._reviewsTupples.items():
				#print('Key : ', key)
				#print('Value : ', value)
				condition = True
				flagNegativeSentance = False
				for subword in aspectTokens:
					if(subword in str(value).upper()):
						condition = condition and True
					else:
						condition = condition and False

				if(condition):
					for negativeWord in self._negativeWordSet:
						if(not flagNegativeSentance):
							if(negativeWord.upper() in str(value).upper()):
								flagNegativeSentance = flagNegativeSentance or True
	
					self._aspectOpinionTupple.setdefault(aspect, [0, 0, 0])
					
					for word, tag in value:
						#print("Word : ", word)
						#print("Tag : ", tag)
						if(tag == 'JJ' or tag == 'JJR' or tag == 'JJS' or tag == 'RB' or tag == 'RBR' or tag == 'RBS'):
							count += 1
							if(word not in self._orientation):
								orientation = self.getOrientation(word)
								self._orientation[word] = orientation	
							else:
								orientation = self._orientation[word]

							if(flagNegativeSentance and orientation is not None):
								orientation = not orientation

							if(orientation == True):
								self._aspectOpinionTupple[aspect][0] += 1
							elif(orientation == False):
								self._aspectOpinionTupple[aspect][1] += 1
							elif(orientation is None):
								self._aspectOpinionTupple[aspect][2] += 1
		
			if count > 0:
				self._aspectOpinionTupple[aspect][0] = round((self._aspectOpinionTupple[aspect][0]/count)*100, 7)	
				self._aspectOpinionTupple[aspect][1] = round((self._aspectOpinionTupple[aspect][1]/count)*100, 7)
				self._aspectOpinionTupple[aspect][2] = round((self._aspectOpinionTupple[aspect][2]/count)*100, 7)
				print(aspect, ':\tPositive -: ', self._aspectOpinionTupple[aspect][0], '\tNegative -: ', self._aspectOpinionTupple[aspect][1], '\tNeutral -: ', self._aspectOpinionTupple[aspect][2])

	def writeInFile(self, directoryName):
		outputAspectOpinion = open(os.path.join(directoryName, 'AspectOpinionResult.txt'), 'w')
		outputAspectOpinion.write(str(self._aspectOpinionTupple))
		outputAspectOpinion.close()

	def closeFile(self):
		self._AspectFile.close()
		self._POSTaggedFile.close()

#instanceLoadData = loadData.LoadData('../../ExtractReviews/')
#instanceLoadData.openFile('HospitalReviews.txt')
#instanceLoadData.readText()
#instanceLoadData.readNegativeWord()
#instanceLoadData.closeFile()

#instanceAspectOpinion = AspectOpinionMining(instanceLoadData._negWord)
#instanceAspectOpinion.openFiles('../../ExtractReviews/')
#instanceAspectOpinion.getAspectOpinion()
#pprint.pprint(instanceAspectOpinion._aspectOpinionTupple)
#pprint.pprint(len(instanceAspectOpinion._aspectOpinionTupple))
#instanceAspectOpinion.writeInFile('../../ExtractReviews/')
