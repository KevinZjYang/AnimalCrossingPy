from urllib import request
from bs4 import BeautifulSoup
from pprint import pprint
import sqlite3

navurl = 'https://wiki.biligame.com/dongsen/%E8%83%A1%E6%8B%89%E6%8B%89'
page = request.urlopen(navurl)
soup = BeautifulSoup(page, 'html.parser')
page.close()
con = sqlite3.Connection("DbTest.db")
cursor = con.cursor()
try:
    sql = "create table LittleAnimal (Name varchar primary key not null,HomePic varchar)" 
    cursor.execute(sql)
except :
    pass

p = soup.findAll('a',class_='image')
piclist = []
name = "name1"
for img in p:
    homePic=img.find('img').attrs['src']
    if "/thumb/" in homePic:
        piclist.append(homePic)
sql = f"""insert or replace into LittleAnimal (Name,HomePic) values ("{name}","{piclist}")"""
cursor.execute(sql)
pprint(piclist)
cursor.close()
con.commit()
con.close()