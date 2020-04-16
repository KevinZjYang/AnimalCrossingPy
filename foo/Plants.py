from urllib import request
from bs4 import BeautifulSoup
from pprint import pprint
import sqlite3
import config


def GetPlants():
    # 获取网页内容
    url = 'https://wiki.biligame.com/dongsen/%E6%A4%8D%E7%89%A9%E5%9B%BE%E9%89%B4'

    page = request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    page.close()

    con = sqlite3.Connection(config.GetFileName())
    cursor = con.cursor()
    try:
        sql = "create table Plant (Name varchar primary key not null,Image varchar ,Price integer)"
        cursor.execute(sql)
    except:
        pass

    tables = soup.findAll('table')
    tab = tables[0]
    for tr in tab.tbody.findAll('tr'):
        td = tr.findAll('td')
        sname = ""
        simage = ""
        iprice = 0
        try:
            td0 = td[0]
            alt = td0.find('img').attrs['alt']
            src = td0.find('img').attrs['src']
            px = '/80px-'
            src = src.replace(px+alt, "")
            src = src.replace("thumb/", "")
            # pprint(src)
            simage = src
        except:
            pass
        try:
            # pprint(td[1].getText().strip())
            sname = td[1].getText().strip()
        except:
            pass
        try:
            # pprint(td[2].getText().strip())
            iprice = td[2].getText().strip()
        except:
            pass
        if sname != "":
            sql = f"insert or replace into Plant (Name,Image,Price) values ('{sname}','{simage}','{iprice}')"
            cursor.execute(sql)

    cursor.close()
    con.commit()
    con.close()

#GetPlants()