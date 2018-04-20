import urllib.request as request
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import re
import pickle

site = ["https://www.tripadvisor.com/Attractions-g60763-Activities-c47-t3-New_York_City_New_York.html",
             "https://www.tripadvisor.com/Attractions-g60763-Activities-c47-t163-New_York_City_New_York.html",
            "https://www.tripadvisor.com/Attractions-g60763-Activities-c47-t26-New_York_City_New_York.html",
            "https://www.tripadvisor.com/Attractions-g60763-Activities-c47-t17-New_York_City_New_York.html",
            "https://www.tripadvisor.com/Attractions-g60763-Activities-c47-t175-New_York_City_New_York.html"]

filename = ['Architectural_Building','POI&Landmarks','Monuments&Statues','Historic_Sites','Churches']

for i in range(len(site)):
    url = urlopen(site[i])
    soup = BS(url,'lxml')
    List = soup.findAll('div',{'class':'listing_info'})
    Data = []
    for x in List:
        Name = x.find('a',{'target':'_blank'}).get_text()
        sub_soup = BS(str(x.find('div',{'class':'rs rating'})),'lxml')
        Rating = sub_soup.span['class']
        Viewer = sub_soup.a.get_text()
        mod = re.compile('[0-9]+')
        Viewer = int("".join(mod.findall(Viewer)))
        Rating = int(mod.findall(Rating[1])[0])
        case = dict()
        case['Name'] = Name
        case['Rating'] = Rating
        case['Viewer'] = Viewer
        Data.append(case)
    file = open('%s.pkl'%filename[i],'wb')
    pickle.dump(Data,file)
    file.close()
    print(i)
