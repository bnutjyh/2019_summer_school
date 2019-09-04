from lxml import etree
import requests
import pandas as pd
import time
import random

infoall = []
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
def getlinks(url):
    #url = 'https://bj.lianjia.com/ershoufang/'
    index = requests.get(url,headers=header)
    dat = etree.HTML(index.text)
    titles = dat.xpath('//div[@class="title"]/a/text()')
    addresses = dat.xpath('//div[@class="houseInfo"]/a/text()')
    room_numbers = dat.xpath('//div[@class="houseInfo"]/a/text()[1]')
    squares = dat.xpath('//div[@class="houseInfo"]/text()[2]')
    unitprices = dat.xpath('//div[@class="unitPrice"]/span/text()')

    #info = {'title':titles,'address':addresses,'room_number':room_numbers,'square':squares,'unitprice':unitprices}
    for i in range(len(unitprices)):
        info = {
            'title': titles[i],
            'address': addresses[i],
            'room_number': room_numbers[i],
            #'squares': squares[i],
            'unitprice': unitprices[i]
        }
        infoall.append(info)
    df = pd.DataFrame(infoall)
    df.to_excel('1.xlsx', sheet_name='Sheet1')

urls = ['https://bj.lianjia.com/ershoufang/pg{}/'.format(str(i)) for i in range(1,3)]
for single_url in urls:
    print('正在爬取链家地址'+single_url)
    getlinks(single_url)
    seconds = random.uniform(1,3)
    time.sleep(seconds)

