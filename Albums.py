from urllib import request
from bs4 import BeautifulSoup
from pprint import pprint
import sqlite3
import config


def GetAlbums():
    url = 'https://wiki.biligame.com/dongsen/%E5%94%B1%E7%89%87%E5%9B%BE%E9%89%B4'

    page = request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    page.close()

    con = sqlite3.Connection(config.GetFileName())
    cursor = con.cursor()
    try:
        sql = "create table Album (Name varchar primary key not null,Number integer,ForeignName varchar,Cover varchar ,Source varchar,BuyPrice varchar,SalePrice varchar)"
        cursor.execute(sql)
    except:
        pass

    tables = soup.findAll('table')
    tab = tables[0]
    for tr in tab.tbody.findAll('tr'):
        td = tr.findAll('td')
        snumber = ""
        try:
            #pprint(td[0].getText().strip())
            snumber = td[0].getText().strip()
        except:
            pass
        try:
            #pprint(td[1].getText().strip())
            sname = td[1].getText().strip()
        except:
            pass
        try:
            #pprint(td[2].getText().strip())
            sforeign = td[2].getText().strip()
        except:
            pass
        try:
            td0 = td[3]
            src = td0.find('img').attrs['src']
            #pprint(src)
            simage = src
        except:
            pass
        try:
            #pprint(td[4].getText().strip())
            ssource = td[4].getText().strip()
        except:
            pass
        # try:
            # pprint(td[5].getText().strip())
            #s = td[5].getText().strip()
        # except:
            # pass
        try:
            #pprint(td[6].getText().strip())
            sbuy = td[6].getText().strip()
        except:
            pass
        try:
            #pprint(td[7].getText().strip())
            ssale = td[7].getText().strip()
        except:
            pass
        # try:
            # pprint(td[8].getText().strip())
            #sname = td[8].getText().strip()
        # except:
            # pass
       
        if snumber != "":
            # pprint(f"'{snumber}','{sname}','{sforeign}','{simage}','{ssource}','{sbuy}','{ssale}')")
            sql = f"""insert or replace into Album (Name,Number,ForeignName,Cover ,Source ,BuyPrice ,SalePrice) values ("{sname}","{snumber}","{sforeign}","{simage}","{ssource}","{sbuy}","{ssale}")"""
            cursor.execute(sql)
            #pprint(sql)
    cursor.close()
    con.commit()
    con.close()


#GetAlbums()
