from urllib import urlopen as ureq
from bs4 import BeautifulSoup as soup
import json


arr=[]
count=0
for x in range(3):

    my_url='https://www.flipkart.com/search?page='+str(x+1)+'&q=ipad&viewType=list'
    uClient = ureq(my_url)
    page_html = uClient.read()
    uClient.close()
    #html parsing
    page_soup = soup(page_html,"html.parser")

    items=page_soup.findAll("a", { "class":"_1UoZlX"})
    print(len(items))
    count=0


    for i in items:
        count=count+1
        dic={}
        print(count)
        k= i.findAll("div", {"class": "_3wU53n"})
        dic['name ']= k[0].text


        l= i.findAll("div", {"class": "VGWI6T"})

        if l==[]:
            dic ['disc']= "NONE"
        else:
            dic['disc ' ]= l[0].text


        arr.append(dic)

    with open('newjson.json', 'a') as f:
        json.dump(arr, f)
