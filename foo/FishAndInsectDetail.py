from urllib import request
from bs4 import BeautifulSoup
from pprint import pprint
import conf
import sqlite3


def GetFishDeatilAndAddToSqlite(navurl):

    page = request.urlopen(navurl)
    soup = BeautifulSoup(page, 'html.parser')
    page.close()

    con = sqlite3.Connection(conf.dbName())
    cursor = con.cursor()
    try:
        sql = "create table Fish (Name varchar primary key not null,Image varchar,Number integer,English varchar ,Japanese varchar,Position varchar,Shape varchar,North varchar,South varchar,Time varchar,Price integer)"
        cursor.execute(sql)
    except:
        pass

    tables = soup.find_all('table')
    tab = tables[0]

    tr = tab.tbody.find_all('tr')
    #pprint(tr[0])

    src = tr[0].find('img').attrs['src']
    inumber = tr[1].find('td').getText().strip()
    sname = tr[2].find('td').getText().strip()
    seng = tr[3].find('td').getText().strip()
    sjap = tr[4].find('td').getText().strip()
    sposition = tr[5].find('td').getText().strip()
    sshape = tr[6].find('td').getText().strip()
    snorth = tr[8].find('td').getText().strip()
    ssouth = tr[9].find('td').getText().strip()
    stime = tr[10].find('td').getText().strip()
    iprice = tr[11].find('td').getText().strip()
    sql = f"""insert or replace into Fish (Name,Image,Number,English ,Japanese ,Position ,Shape ,North ,South ,Time ,Price ) values ("{sname}","{src}","{inumber}","{seng}","{sjap}","{sposition}","{sshape}","{snorth}","{ssouth}","{stime}","{iprice}")"""
    cursor.execute(sql) 
    #pprint(sql)

    cursor.close()
    con.commit()
    con.close()

def GetInsectDeatilAndAddToSqlite(navurl):

    page = request.urlopen(navurl)
    soup = BeautifulSoup(page, 'html.parser')
    page.close()

    con = sqlite3.Connection(conf.dbName())
    cursor = con.cursor()
    try:
        sql = "create table Insect (Name varchar primary key not null,Image varchar,Number integer,English varchar ,Japanese varchar,Position varchar,Weather varchar,North varchar,South varchar,Time varchar,Price integer)"
        cursor.execute(sql)
    except:
        pass

    tables = soup.find_all('table')
    tab = tables[0]

    tr = tab.tbody.find_all('tr')
    #pprint(tr[0])

    src = tr[0].find('img').attrs['src']
    inumber = tr[1].find('td').getText().strip()
    sname = tr[2].find('td').getText().strip()
    seng = tr[3].find('td').getText().strip()
    sjap = tr[4].find('td').getText().strip()
    sposition = tr[5].find('td').getText().strip()
    ssharp = tr[6].find('td').getText().strip()
    snorth = tr[8].find('td').getText().strip()
    ssouth = tr[9].find('td').getText().strip()
    stime = tr[10].find('td').getText().strip()
    iprice = tr[11].find('td').getText().strip()
    sql = f"""insert or replace into Insect (Name,Image,Number,English ,Japanese ,Position ,Weather ,North ,South ,Time ,Price ) values ("{sname}","{src}","{inumber}","{seng}","{sjap}","{sposition}","{ssharp}","{snorth}","{ssouth}","{stime}","{iprice}")"""
    cursor.execute(sql) 
    #pprint(sql)

    cursor.close()
    con.commit()
    con.close()


#url = 'https://wiki.biligame.com//dongsen/%E4%BA%9A%E5%8E%86%E5%B1%B1%E5%A4%A7%E5%87%A4%E8%9D%B6'
#GetInsectDeatilAndAddToSqlite(url)
