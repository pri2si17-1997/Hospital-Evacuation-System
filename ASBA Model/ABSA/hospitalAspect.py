import io
import os
import json
import pprint
import readAllDirectory
import loadData
import removeStopWord
import tokenizeReviews
import partOfSpeechTagging
import extractAspect
import aspectOpinion

CONSTANT_DIRECTORY = '../../ExtractReviews/Reviews/'
CONSTANT_FILENAME = 'reviews.txt'

if __name__ == '__main__':
	instanceReadDirectory = readAllDirectory.ReadDirectory(CONSTANT_DIRECTORY)
	instanceReadDirectory.readDirectory()
	#pprint.pprint(instanceReadDirectory._dirList)
	for index in range(0, len(instanceReadDirectory._dirList)):
		print("Process : ", index)
		pprint.pprint(CONSTANT_DIRECTORY + instanceReadDirectory._dirList[index])

		#Loading Review File
		instanceLoadData = loadData.LoadData(CONSTANT_DIRECTORY + instanceReadDirectory._dirList[index])
		instanceLoadData.openFile(CONSTANT_FILENAME)
		instanceLoadData.readText()
		instanceLoadData.readNegativeWord()
		#pprint.pprint(instanceLoadData._text)
		#pprint.pprint(instanceLoadData._negWord)
		instanceLoadData.closeFile()

		#Removing Stop Words
		instanceRemveStopWord = removeStopWord.RemoveStopWord(instanceLoadData._text)
		instanceRemveStopWord.removeStopWord()
		#print(instanceRemveStopWord._stopWords)
		#print(instanceRemveStopWord._result)

		#Tokenizing Data
		instanceTokenizeData = tokenizeReviews.TokenizeData(instanceLoadData._text)
		instanceTokenizeData.tokenizeReview()
		instanceTokenizeData.writeInFile(CONSTANT_DIRECTORY + instanceReadDirectory._dirList[index])
		#pprint.pprint(instanceTokenizeData._tokenizedReview)

		#Part of Speech Tagging
		instancePOSTag = partOfSpeechTagging.POSTagging()
		instancePOSTag.openFile(CONSTANT_DIRECTORY + instanceReadDirectory._dirList[index])
		instancePOSTag.posTagging()
		#instancePOSTag.closeFile()
		#pprint.pprint(instancePOSTag._outputPOSTag)
		instancePOSTag.writeInFile(CONSTANT_DIRECTORY + instanceReadDirectory._dirList[index])

		#Aspect Extraction
		instanceExtractAspect = extractAspect.ExtractAspect()
		instanceExtractAspect.openFile(CONSTANT_DIRECTORY + instanceReadDirectory._dirList[index])
		instanceExtractAspect.extractAspect()
		#pprint.pprint(instanceExtractAspect._outputAspect)
		instanceExtractAspect.writeInFile(CONSTANT_DIRECTORY + instanceReadDirectory._dirList[index])
		#instanceExtractAspect.closeFile()

		#Aspect - Opinion Mapping
		instanceAspectOpinion = aspectOpinion.AspectOpinionMining(instanceLoadData._negWord)
		instanceAspectOpinion.openFiles(CONSTANT_DIRECTORY + instanceReadDirectory._dirList[index])
		instanceAspectOpinion.getAspectOpinion()
		pprint.pprint(instanceAspectOpinion._aspectOpinionTupple)
		pprint.pprint(len(instanceAspectOpinion._aspectOpinionTupple))
		instanceAspectOpinion.writeInFile(CONSTANT_DIRECTORY + instanceReadDirectory._dirList[index])

