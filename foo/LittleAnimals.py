from urllib import request
from bs4 import BeautifulSoup
from pprint import pp, pprint
import sqlite3
import conf


def GetLittleAnimals():

    # 小动物图鉴地址
    url = 'https://wiki.biligame.com/dongsen/%E5%B0%8F%E5%8A%A8%E7%89%A9%E5%9B%BE%E9%89%B4'

    page = request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    page.close()

    con = sqlite3.Connection(conf.dbName())
    cursor = con.cursor()
    try:
       sql = "create table LittleAnimal (Name varchar primary key not null,Image varchar ,Gender varchar,Brithday varchar,Character varchar,Mantra varchar,Goal varchar,Motto varchar,PersonalStyle varchar,LikeColor varchar,Pitch varchar,ForeignName varchar,HomePic varchar)" 
       cursor.execute(sql)
    except :
       pass

    tables = soup.findAll('table')
    tab = tables[1]
    i = 0
    for tr in tab.tbody.findAll('tr'):
        for td in tr.findAll('td'):
            try:
                href = td.find('a').attrs['href']
                host = 'https://wiki.biligame.com/'
                navurl = host+href
                #GetLittleAnimalDetail.SayHello('This is ','i')

                #LittleAnimalDetail.GetDeatilAndAddToSqlite(navurl)
                page = request.urlopen(navurl)
                soup = BeautifulSoup(page, 'html.parser')
                page.close()

                #名字
                name = soup.find('a',class_='mw-selflink selflink').getText()
                #pprint(name)

                image=""
                pokeright = soup.find_all('div',class_='box-poke-right')
                for item in pokeright:
                    image = item.find('img').attrs['src']
                    #pprint(image)
                Gender=""
                brith=""
                character=""
                Mantra=""
                Goal=""
                sStyle=""
                sColor=""
                sPitch=""
                Motto=""
                Foreign=""
                pokeleft = soup.find_all('div',class_='box-poke-left')
                for item in pokeleft:
                    #性别
                    Gender = item.find('div',class_='box-title-1').getText().strip().replace(name,'')
                    #pprint(Gender)

                    font = item.find_all('font',class_='box-font')
                    #pprint(font)

                    #生日
                    brith = font[0].getText().strip()
                    #pprint(brith)

                    #性格
                    character = font[1].getText().strip()

                    #口头禅
                    Mantra = font[2].getText().strip()

                    #爱好
                    Goal = font[3].getText().strip()
                    
                    #风格偏好
                    sStyle=font[4].getText().strip()

                    #喜欢颜色
                    sColor=font[5].getText().strip()

                    #音高
                    sPitch=font[6].getText().strip()

                    #座右铭
                    Motto  = item.find('div',class_='box-font').getText()

                    #外文名称
                    Foreign = font[7].getText().strip()
                    #pprint(Foreign)
                
                p = soup.findAll('p')
               
                piclist = []
                p1=p[1]
                p2=p1.find_all("a",class_="image")
                #pprint(p0)
                for img in p2:
                    homePic=img.find('img').attrs['src']
                    #pprint(homePic)
                    piclist.append(homePic)
                    #pprint(piclist)
                    #if "/thumb/" in homePic:
                       #piclist.append(homePic)
                
                #pprint('开始写入数据库...')
                #pprint(piclist)
                sql = f"""insert or replace into LittleAnimal (Name,Image,Gender,Brithday,Character,Mantra,Goal,Motto,PersonalStyle,LikeColor,Pitch,ForeignName,HomePic) values ("{name}","{image}","{Gender}","{brith}","{character}","{Mantra}","{Goal}","{Motto}","{sStyle}","{sColor}","{sPitch}","{Foreign}","{piclist}")"""
                #pprint(sql)
                cursor.execute(sql)
                #pprint(f"add '{name}'")
                i = i + 1
                pprint(f"添加小动物{i}：{name}")   
                    
            except:
                pass
    cursor.close()
    con.commit()
    con.close()

#GetLittleAnimals()
