from urllib import request
from bs4 import BeautifulSoup
from pprint import pprint
import LittleAnimalDetail


def GetLittleAnimals():

    # 小动物图鉴地址
    url = 'https://wiki.biligame.com/dongsen/%E5%B0%8F%E5%8A%A8%E7%89%A9%E5%9B%BE%E9%89%B4'

    page = request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    page.close()

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

                LittleAnimalDetail.GetDeatilAndAddToSqlite(navurl)
                i = i + 1
                pprint(f"添加小动物{i}")
            except:
                pass
