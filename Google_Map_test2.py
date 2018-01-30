api_key='AIzaSyAexRfBC0Q3uAohdNA0RrMVT47rw0lI0sg'

import googlemaps
from datetime import datetime
import pickle
# Replace the API key below with a valid API key.
gmaps = googlemaps.Client(key=api_key)

# Geocoding and address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Elevation
Result = gmaps.elevation((27.988242,86.924975))

Ans = []

for i in range(17,52,1):
    for j in range(71,136,1):
        print(i,j)
        Result = gmaps.elevation((i,j))
        Ans.append((dict(Result[0]))['elevation'])

print("Fecth Completed!")
file = open('Elevation.pkl','wb')
pickle.dump(Ans,file)
file.close()
        
