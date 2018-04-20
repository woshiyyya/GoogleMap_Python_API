api_key = 'AIzaSyCqKFyoTTLWwmlXZDo1HMlilviKqGUHXzI'
import numpy as np
import googlemaps

gmaps = googlemaps.Client(key=api_key)
Result = gmaps.places_nearby(location = (40.758478,-73.985452),radius=100,type = 'restaurant')
'''
# type(Result)
<class 'dict'>
# Result.keys()
dict_keys(['html_attributions', 'results', 'status'])
# type(Result['result'])
<class 'list'>
# Result['results'][0].keys() 
dict_keys(['geometry', 'icon', 'id',   'name',            'opening_hours',
                 'photos',      'place_id',   'price_level',    'rating',
                 'reference',  'scope',       'types',             'vicinity'])
'''
'''
1. geometry |—— location  —— lat
                     |                      —— lng
                     |—— viewport——northeast{lat, lng}
                                             ——southwest{lat, lng}
2. id——(geocode)

3. opening_hours————  open_now
                                |
                                |———weekday_text

4.place_id

5.rating 

6.price_level —— 1-5

7.vicinity       —— e.g.: '1535 Broadway, New York'

8.types          —— ['restaurant', 'food', 'point_of_interest', 'establishment']








                                








