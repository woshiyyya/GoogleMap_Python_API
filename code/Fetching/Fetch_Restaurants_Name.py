import urllib.request as request
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import re
import pickle

site = ["https://www.tripadvisor.com/Restaurants-g60763-New_York_City_New_York.html"]

filename = ['Restaurants_Name']

for i in range(len(site)):
    url = urlopen(site[i])
    soup = BS(url,'lxml')
    List = soup.findAll('div',{'class':'ui_column is-9 shortSellDetails'})
    Data = []
    for x in List:
        Name = x.find('a',{'target':'_blank'}).get_text()
        Rating = x.find('div',{'class':'rating rebrand'}).span['class']
        Price = x.find('span',{'class':'item price'}).get_text()
        Cs = BS(str(x.findAll('div',{'class':'cuisines'})),'lxml').findAll('a')
        Viewer = (x.find('div',{'class':'rating rebrand'})).a.get_text()
        Cuisine = []
        for item in Cs:
            Cuisine.append(item.get_text())
        mod = re.compile('[0-9]+')
        Viewer = int("".join(mod.findall(Viewer)))
        Rating = int(mod.findall(Rating[1])[0])
        print(Name,Rating,Price)
        case = dict()
        case['Name'] = Name.strip('\n')
        case['Rating'] = Rating
        case['Cuisine'] = Cuisine
        case['Price'] = Price
        case['Viewer'] = Viewer
        Data.append(case)
    file = open('data\%s.pkl'%filename[i],'wb')
    pickle.dump(Data,file)
    file.close()
    print(i)

