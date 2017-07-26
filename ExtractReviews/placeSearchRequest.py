#importing necessary python libraries
import urllib
import requests #for making request

try: #for python 2.7+
        import urlparse
        from urllib import urlencode
except: #for python 3.5+
        import urllib.parse as urlparse
        from urllib.parse import urlencode

class placeRequest:
	def __init__(self, search_query, searchType):
		self.search_query = search_query
		self.type = searchType

	#Method Overloading.
	def formURL(self, base_url, Api_key, next_page_token = None):
		url_parts = list(urlparse.urlparse(base_url))
		query = dict(urlparse.parse_qsl(url_parts[4]))
		if next_page_token is None:
			query_parameters = {'query' : self.search_query,
				    	    'type' : self.type,
				    	    'key' : Api_key}
		else:
			query_parameters = {'query' : self.search_query,
                                    	    'type' : self.type,
                                    	    'key' : Api_key,
					    'pagetoken' : next_page_token}
		#print(query_parameters)
		query.update(query_parameters)
		url_parts[4] = urlencode(query)
		urlToMakeHTTPRequest = urlparse.urlunparse(url_parts)
		return urlToMakeHTTPRequest

	def makeHTTPRequest(self, url):
		data = requests.get(url)
		return data


