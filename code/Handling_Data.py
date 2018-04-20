import pickle
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
Data = pd.read_csv('data\\Distance_Matrix_red.csv')
Data = Data.drop(Data.columns[0],axis=1)
print(Data.shape)

#Visualization
'''
Distance = np.array(Data).reshape((-1,1))
POI_Distance = Distance[0:110]
RST_Distance =  Distance[110:-1]
sns.set(style="whitegrid")
ax = sns.distplot(Distance)
plt.xlim(-10,40)
plt.show(ax)
'''
filename = ['Architectural_Building',                    #1 - 2h - 3
                    'POI&Landmarks',                             
                    'Monuments&Statues',
                    'Historic_Sites',
                    'Churches',
                    'Restaurants_Name']                         #0.3 - 0.5

f = open("data\\Ind_Name_Maps.pkl",'rb')
Map = dict()
for i in range(2):
    Map = pickle.load(f)
#Creat Random distribution visit time for every POI & RST
cost = np.random.normal(loc=2,scale=0.5,size=(110,110))
POI_visit_cost = np.triu(cost,1) + np.triu(cost,1).T
cost = np.random.normal(loc=0.5,scale = 0.1,size=(29,29))
RST_visit_cost = np.triu(cost,1) + np.triu(cost,1).T

# Calculate the cost_on_traffic 
traffic_velocity = [6,12,50,70] #foot bike bus metro
Distance_of_POI = Data.iloc[0:110,0:110]
Cost_of_POI = []
Type = ['foot','bike','bus','metro']
'''
for i in range(4):
    Tem = Distance_of_POI/traffic_velocity[i]
    Tem.to_csv('data\\Traffic_Time\\%s.csv'%Type[i])
'''
for i in range(4):
    Tem = POI_visit_cost +   Distance_of_POI/traffic_velocity[i]
    Cost_of_POI.append(Tem)
    Tem.to_csv('data\\Cost\\Cost_by_%s.csv'%Type[i])
with open('data\\Cost\\Cost_of_POI_Full.pkl','wb') as f:
    pickle.dump(Cost_of_POI,f)
    f.close()





