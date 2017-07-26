# Class to define all the google constants. 
class googleVar:
	def __init__(self):
		self._API_KEY = 'AIzaSyD_8gYjw6MLC45SFLJKNbhR1iylcRYsIH0' #API key for making google api call
		#self._API_KEY = 'AIzaSyAwMrsHHX-CZKGmR9Z4i8XbkW7vUR2LONQ' #Alternate API key

	def getPlaceSearchUrl(self):
		self._placeSearchBaseURL = 'https://maps.googleapis.com/maps/api/place/textsearch/json' #Place Search Url

	def getPlaceDetailsBaseUrl(self):
		self._placeDetailsBaseURL = 'https://maps.googleapis.com/maps/api/place/details/json' #Place Details Base URL



		
