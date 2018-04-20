api_key='AIzaSyAexRfBC0Q3uAohdNA0RrMVT47rw0lI0sg'
import googlemaps
import pickle
import pandas
import numpy as np

columns = ['Name','lat','lng','rating','viewer','Cusine','Price','begin_day','end_day']
Weekday_Map = {'Monday':1,'Tuesday':2,'Wednesday':3,
               'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7}
gmaps = googlemaps.Client(key=api_key)
f = 'Restaurants_Name'
file = open('data\%s.pkl'%f,'rb')
Data = pickle.load(file)
file.close()
data_slice = []
for case in Data:
    Name = case['Name']
    print(Name)
    geocode = dict(gmaps.geocode(Name)[0])
    place_id = geocode['place_id']
    info = (gmaps.place(place_id = place_id))['result']
    data_slice.append(Name)
    data_slice.append(info['geometry']['location']['lat'])
    data_slice.append(info['geometry']['location']['lng'])
    data_slice.append(case['Rating']/10)
    data_slice.append(case['Viewer'])
    data_slice.append(" ".join(case['Cuisine']))
    data_slice.append(case['Price'])
    if 'opening_hours' in info.keys():
        open_time = info['opening_hours']['weekday_text']
        begin_day = Weekday_Map[(open_time[0].split(':'))[0]]
        end_day = Weekday_Map[(open_time[-1].split(':'))[0]]                  
        data_slice.append(begin_day)
        data_slice.append(end_day)
    else:
        data_slice.append(0)
        data_slice.append(0)
data = np.array(data_slice).reshape(len(Data),9)
data_frame = pandas.DataFrame(data,columns=columns)
data_frame.to_csv("data\Detail\%s detail.csv"%f)
  
