#importing necessary python libraries
import urllib
import requests #for making request

try: #for python 2.7+
        import urlparse
        from urllib import urlencode
except: #for python 3.5+
        import urllib.parse as urlparse
        from urllib.parse import urlencode

class placeDetails:
	def __init__(self, place_id):
		self._place_id = place_id

	def formURL(self, base_url, Api_key):
		url_parts = list(urlparse.urlparse(base_url))
		query = dict(urlparse.parse_qsl(url_parts[4]))
		query_parameters = {'placeid' : self._place_id,
				    'key' : Api_key}
		query.update(query_parameters)
		url_parts[4] = urlencode(query)
		urlToMakeHTTPRequest = urlparse.urlunparse(url_parts)
		return urlToMakeHTTPRequest

	def makeHTTPRequest(self, url):
		data = requests.get(url)
		return data


