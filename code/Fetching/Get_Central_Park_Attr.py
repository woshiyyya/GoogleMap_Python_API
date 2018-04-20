# Fetch attractions in Central Park
from urllib.request import urlopen
from bs4 import BeautifulSoup
import bs4
import pickle

site = "https://www.centralpark.com/things-to-do/attractions"
HTML = urlopen(site)
soup = BeautifulSoup(HTML,'lxml')
Name_lable = soup.find('select',{'id':"finder-list-items"})
Ans = []
for i in Name_lable.option.next_siblings:
    print(type(i))
    if type(i) == bs4.element.Tag:
        Ans.append(i['title'])
file = open("Attr_in_CentralPark.pkl",'wb')
pickle.dump(Ans,file)
file.close()
