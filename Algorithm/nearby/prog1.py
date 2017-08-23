from pprint import pprint
from googleplaces import GooglePlaces, types, lang
YOUR_API_KEY = 'AIzaSyCfJt7vD0QNEdfky2lOH2Ghler5Zj_Gr2I'
google_places = GooglePlaces(YOUR_API_KEY)
query_result = google_places.nearby_search(location='JIIT Noida , Sector 62, Noida', radius=100000, keyword='Heart',rankby='distance' ,types=[types.TYPE_HOSPITAL])
'''if query_result.has_attributions:
    print query_result.html_attributions


for place in query_result.places:
    # Returned places from a query are place summaries.
    print place.name
    print place.geo_location
    print place.place_id'''
'''
    # The following method has to make a further API call.
    place.get_details()
    # Referencing any of the attributes below, prior to making a call to
    # get_details() will raise a googleplaces.GooglePlacesAttributeError.
    print place.details # A dict matching the JSON response from Google.
    print place.local_phone_number
    print place.international_phone_number
    print place.website
    print place.url'''
