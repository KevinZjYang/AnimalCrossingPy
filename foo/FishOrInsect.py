from urllib import request
from bs4 import BeautifulSoup
from pprint import pprint
import FishAndInsectDetail

def GetFishes():
    # 鱼图鉴地址
    url = 'https://wiki.biligame.com/dongsen/%E5%8D%9A%E7%89%A9%E9%A6%86%E5%9B%BE%E9%89%B4'

    page = request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    page.close()

    tables = soup.findAll('table')
    tab = tables[2]
    
    i = 0
    for tr in tab.tbody.findAll('tr'):
        for td in tr.findAll('td'):
            try:
                href = td.find('a').attrs['href']
                host = 'https://wiki.biligame.com/'
                navurl = host+href
                #pprint(navurl)
                FishAndInsectDetail.GetFishDeatilAndAddToSqlite(navurl)
                i=i+1
                pprint(f"添加鱼{i}")
            except:
                pass

def GetInsects():
    # 昆虫图鉴地址
    url = 'https://wiki.biligame.com/dongsen/%E8%99%AB%E5%9B%BE%E9%89%B4'

    page = request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    page.close()

    tables = soup.findAll('table')
    tab = tables[2]
    
    i = 0
    for tr in tab.tbody.findAll('tr'):
        for td in tr.findAll('td'):
            try:
                href = td.find('a').attrs['href']
                host = 'https://wiki.biligame.com/'
                navurl = host+href
                i=i+1
                #pprint(navurl)
                FishAndInsectDetail.GetInsectDeatilAndAddToSqlite(navurl,i)
               
                pprint(f"添加昆虫{i}")
            except:
                pass
#GetFishes()