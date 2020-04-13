from urllib import request
from bs4 import BeautifulSoup
from pprint import pprint
import sqlite3
import config

def GetDeatilAndAddToSqlite(navurl):
    
    page = request.urlopen(navurl)
    soup = BeautifulSoup(page, 'html.parser')
    page.close()

    con = sqlite3.Connection(config.GetFileName())
    cursor = con.cursor()
    try:
       sql = "create table LittleAnimal (Name varchar primary key not null,Image varchar ,Gender varchar,Brithday varchar,Character varchar,Mantra varchar,Goal varchar,Motto varchar,ForeignName varchar)" 
       cursor.execute(sql)
    except :
       pass

    #名字
    name = soup.find('a',class_='mw-selflink selflink').getText()
    #pprint(name)
    
    pokeright = soup.find_all('div',class_='box-poke-right')
    for item in pokeright:
        image = item.find('img').attrs['src']
        #pprint(image)
    
    pokeleft = soup.find_all('div',class_='box-poke-left')

    for item in pokeleft:
        #性别
        Gender = item.find('div',class_='box-title-1').getText().strip().replace(name,'')

        #text = item.find_all('font',class_='box-title-2')
        font = item.find_all('font',class_='box-font')

        #生日
        #brithkey = text[0].getText().strip()
        brith = font[0].getText().strip()
        #性格
        #characterkey = text[1].getText().strip()
        character = font[1].getText().strip()

        #口头禅
        #Mantrakey= text[2].getText().strip()
        Mantra = font[2].getText().strip()

        #目标
        #Goalkey= text[3].getText().strip()
        Goal = font[3].getText().strip()

        #座右铭
        #Mottokey = item.find('div',class_='box-title-2').getText()
        Motto  = item.find('div',class_='box-font').getText()
        #Mottokey= text[4].getText().strip()
        #Motto = font[4].getText().strip()

        #外文名称
        #Foreignkey= text[4].getText().strip()
        Foreign = font[4].getText().strip()
        
        #pprint('开始写入数据库...')
        #pprint(name+image+Gender+brithkey+brith+characterkey+character+Mantrakey+Mantra+Goalkey+Goal+Mottokey+Motto+Foreignkey+Foreign)
        sql = f"insert or replace into LittleAnimal (Name,Image,Gender,Brithday,Character,Mantra,Goal,Motto,ForeignName) values ('{name}','{image}','{Gender}','{brith}','{character}','{Mantra}','{Goal}','{Motto}','{Foreign}')"
        cursor.execute(sql)
        pprint(f"add '{name}'")
    
    cursor.close()
    con.commit()
    con.close()
    #pprint('working')


              
#url = 'https://wiki.biligame.com/dongsen/%E9%98%B3%E6%98%8E'
#GetDeatilAndAddToSqlite(url)
