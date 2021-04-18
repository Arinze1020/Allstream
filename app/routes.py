from app import app
from collections import OrderedDict
from flask import render_template
from bs4 import BeautifulSoup
import requests 
import itertools 



@app.route("/")
def Home():
    #r = s.get('https://sportshub.fan')
    
    link = []
    name = []
    tim = []
    page1 =requests.get ('https://sportshub.fan')
    soup = BeautifulSoup(page1.content,'html.parser')
    for data in soup.find_all('a',class_='live'):
        url = data.get('href')
        teams = data.text
        link.append("https://sportshub.fan"+url)
        name.append(teams)

    for time in soup.find_all('span',class_='evdesc'):
        times = time.text
        tim.append(times)

    
  
    #link = list(OrderedDict.fromkeys(li))
    #name = list(OrderedDict.fromkeys(team))
    #name.remove('live')
    #link + name
    #print(len(name))
    #print(len(name))
    #print(link+name)
    return render_template("index.html",zipconten = zip(name, link),tim=tim)