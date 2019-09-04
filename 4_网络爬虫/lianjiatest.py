import requests
from bs4 import BeautifulSoup
import random
import time
import pandas as pd

allinfo = []
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
def getlinks(url):
    index = requests.get(url, headers=header)
    soup = BeautifulSoup(index.text, 'lxml')
    links = soup.select('div > div.title > a')
    for link in links:
        href = link.get('href')  #房子链接
        getinfo(href)
        time.sleep(0.5)
        #print(links[1].get('href'))
def getinfo(url):
    wdata = requests.get(url, headers=header)
    wsoup = BeautifulSoup(wdata.text, 'lxml')
    titles = wsoup.select('div > div.title > h1')
    attentions = wsoup.select('#favCount')
    watch = wsoup.select('#cartCount')
    totalprice = wsoup.select('div.content > div.price > span.total')
    unitprice = wsoup.select('div.price > div.text > div.unitPrice > span')
    roommain = wsoup.select('div.houseInfo > div.room > div.mainInfo')
    roomsub = wsoup.select('body > div.overview > div.content > div.houseInfo > div.room > div.subInfo')
    direction = wsoup.select('div.content > div.houseInfo > div.type > div.mainInfo')
    subdirection = wsoup.select('div.content > div.houseInfo > div.type > div.subInfo')
    area = wsoup.select('div.content > div.houseInfo > div.area > div.mainInfo')
    year = wsoup.select('div.content > div.houseInfo > div.area > div.subInfo')
    communityname = wsoup.select('div.content > div.aroundInfo > div.communityName > a.info')
    regions = wsoup.select('body > div.overview > div.content > div.aroundInfo > div.areaName > span.info > a')


    info = {
        'title': titles[0].get_text().strip(),
        'attention': attentions[0].get_text(),
        'watch': watch[0].get_text(),
        'totalprice': totalprice[0].get_text(),
        'unitprice': unitprice[0].get_text().strip('元/平米'),
        'roommain': roommain[0].get_text(),
        'roomsub': roomsub[0].get_text(),
        'direction': direction[0].get_text(),
        'subdirection': subdirection[0].get_text(),
        'area': area[0].get_text(),
        'year': year[0].get_text(),
        'communityname': communityname[0].get_text(),
        'region': regions[0].get_text(),
        'subregion': regions[1].get_text(),
    }


    allinfo.append(info)
    df = pd.DataFrame(allinfo)
    df.to_excel('lianjiatry.xlsx', sheet_name='Sheet1')



if __name__ == '__main__':
    urls = ['http://bj.lianjia.com/ershoufang/pg{}/'.format(number) for number in range(1,3)]
    for single_url in urls:
        print('正在爬取链家地址'+ single_url)
        getlinks(single_url)
        seconds = random.uniform(2,5)
        time.sleep(seconds)









