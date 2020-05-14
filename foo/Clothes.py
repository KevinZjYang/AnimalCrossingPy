from urllib import request
from bs4 import BeautifulSoup
from pprint import pprint
from urllib.parse import unquote
import sqlite3
import conf


def GetClothes(url, dbName, i):
    page = request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    page.close()
    con = sqlite3.Connection(conf.dbName())
    cursor = con.cursor()
    try:
        sql = f"""create table {dbName} (Number integer primary key ,Name varchar ,Image varchar ,Type varchar,Color varchar,ZH_TW varchar,Japanese varchar,English varchar,TimmyPrice varchar,BoxPrice varchar,Price integer)"""
        cursor.execute(sql)
    except:
        pass
    tables = soup.findAll('table')
    tab = tables[1]

    for tr in tab.tbody.findAll('tr'):
        for td in tr.findAll('td'):
            try:
                href = td.find('a').attrs['href']
                host = 'https://wiki.biligame.com/'
                navurl = host+href

                page = request.urlopen(navurl)
                soup = BeautifulSoup(page, 'html.parser')
                page.close()

                tables = soup.find_all('table')
                tab = tables[0]

                tr = tab.tbody.find_all('tr')

                sname = tr[0].find('th').getText().strip()
                src = tr[1].find('img').attrs['src']
                stype = tr[2].find('td').getText().strip()
                scolor = tr[3].find('td').getText().strip()

                szhtw = tr[4].find('td').getText().strip()
                sjap = tr[5].find('td').getText().strip()
                seng = tr[6].find('td').getText().strip()
                stimmyprice = tr[7].find('td').getText().strip()
                sboxprice = tr[8].find('td').getText().strip()
                iprice = tr[9].find('td').getText().strip()

                sql = f"""insert or replace into {dbName} (Name,Image,Type,Color,ZH_TW,Japanese,English,TimmyPrice,BoxPrice,Price) values ("{sname}","{src}","{stype}","{scolor}","{szhtw}","{sjap}","{seng}","{stimmyprice}","{sboxprice}","{iprice}")"""
                cursor.execute(sql)
                i = i+1
                pprint(f"添加{i}:'{sname}'")

            except:
                pass
    cursor.close()
    con.commit()
    con.close()


def GetAllClothes():
    # 包
    pprint("开始采集包==========")
    bagUrl = 'https://wiki.biligame.com/dongsen/%E5%8C%85'
    dbName = "Bag"
    i = 0
    GetClothes(bagUrl, dbName, i)

    # 上装
    pprint("开始采集上装==========")
    coatUrl = 'https://wiki.biligame.com/dongsen/%E6%9C%8D%E9%A5%B0%E5%9B%BE%E9%89%B4'
    dbName = "Coat"
    i = 0
    GetClothes(coatUrl, dbName, i)

    # 下装
    pprint("开始采集下装==========")
    pantsUrl = 'https://wiki.biligame.com/dongsen/%E4%B8%8B%E8%A3%85'
    dbName = "Pants"
    i = 0
    GetClothes(pantsUrl, dbName, i)

    # 连衣裙
    pprint("开始采集连衣裙==========")
    dressUrl = 'https://wiki.biligame.com/dongsen/%E8%BF%9E%E8%A1%A3%E8%A3%99'
    dbName = "Dress"
    i = 0
    GetClothes(dressUrl, dbName, i)

    # 帽子
    pprint("开始采集帽子==========")
    hatUrl = 'https://wiki.biligame.com/dongsen/%E5%B8%BD%E5%AD%90'
    dbName = "Hat"
    i = 0
    GetClothes(hatUrl, dbName, i)

    # 头盔
    pprint("开始采集头盔==========")
    helmetUrl = "https://wiki.biligame.com/dongsen/%E5%A4%B4%E7%9B%94"
    dbName = "Helmet"
    i = 0
    GetClothes(helmetUrl, dbName, i)

    # 饰品
    pprint("开始采集饰品==========")
    accessoriesUrl = "https://wiki.biligame.com/dongsen/%E9%A5%B0%E5%93%81"
    dbName = "Accessories"
    i = 0
    GetClothes(accessoriesUrl, dbName, i)

    # 袜子
    pprint("开始采集袜子==========")
    sockUrl = 'https://wiki.biligame.com/dongsen/%E8%A2%9C%E5%AD%90'
    dbName = "Sock"
    i = 0
    GetClothes(sockUrl, dbName, i)

    # 鞋
    pprint("开始采集鞋==========")
    shoeUrl = 'https://wiki.biligame.com/dongsen/%E9%9E%8B'
    dbName = "Shoe"
    i = 0
    GetClothes(shoeUrl, dbName, i)

    


#GetAllClothes()
