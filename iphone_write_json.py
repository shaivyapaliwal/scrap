
from urllib import urlopen as ureq
from bs4 import BeautifulSoup as soup
import json

my_url='https://www.flipkart.com/search?q=iphone'
uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()
#html parsing
page_soup = soup(page_html,"html.parser")

items=page_soup.findAll("div", {"class":"_3wU53n"})
disc=page_soup.findAll("div", {"class": "VGWI6T"})

arr=[]
for i, j in zip(items, disc):
    dic={}

    dic['name ']=i.text
    dic['discount ']=j.text
    arr.append(dic)


with open('newjson.json', 'a') as f:
    json.dump(arr, f)
