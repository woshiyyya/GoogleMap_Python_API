from haversine import haversine
import pandas
import numpy as np
import pickle

filename = ['Architectural_Building',
            'POI&Landmarks','Monuments&Statues',
            'Historic_Sites','Churches','Restaurants_Name']
Data = pandas.DataFrame()
for i in range(len(filename)):
    f = filename[i]
    rd_data = pandas.read_csv("data\\Detail\\%s detailed.csv"%f)
    Type = pandas.DataFrame(np.ones((30,1))*i,columns=['Type'])
    rd_data = pandas.concat([rd_data,Type],axis=1)
    Data = pandas.concat([Data,rd_data])
    print(Data.shape)

#Drop duplicates
Data = Data.drop_duplicates('Name')
Data = Data.reset_index(drop=True)
lat = Data['lat']
lng = Data['lng']

#Drop abnormal datacase
drop = []
for i in range(Data.shape[0]):
    if (lng[i]<-74.258627 or lat[i] < 40.493607 or lng[i] >-73.689959 or lat[i]>40.918552):
        drop.append(i)
Data = Data.drop(drop)
Data = Data.reset_index(drop=True)

Data.to_csv('view.csv')

#Generate location tuple
POI = Data['Name']
lat = Data['lat']
lng = Data['lng']
location = []
case_num = len(lat)
for i in range(case_num):
    location.append((lat[i],lng[i]))
    
#Compute Distance
distant_matrix = np.zeros((case_num,case_num))
for i in range(case_num):
    for j in range(case_num):
        distant_matrix[i][j] = haversine(location[i],location[j])

Map_Ind_to_Name = dict(zip(np.arange(len(POI)),POI))
Map_Name_to_Ind = dict(zip(POI,np.arange(len(POI))))
Map_Ind_to_Type = dict(zip(POI,Data['Type']))

pandas.DataFrame(distant_matrix).to_csv('data\\Distance_Matrix_red.csv')
with open("data\\Ind_Name_Maps.pkl",'wb') as f:
    pickle.dump(Map_Ind_to_Name,f)
    pickle.dump(Map_Name_to_Ind,f)
    pickle.dump(Map_Name_to_Type,f)
    f.close()



