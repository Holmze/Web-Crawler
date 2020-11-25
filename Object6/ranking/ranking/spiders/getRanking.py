import scrapy
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request
import threading
import time
import requests
from urllib.request import urlretrieve

class RankingSpider(scrapy.Spider):
    name = 'ranking'

    def start_requests(self):
        urls = ['https://www.shanghairanking.cn/rankings/bcur/2020']
        return [scrapy.Request(url = url,callback = self.parse) for url in urls]

    def parse(self,response):
        threads = []
        start_time = time.time()
        start_url = "https://www.shanghairanking.cn/rankings/bcur/2020"
        # start_url="http://www.weather.com.cn/weather/101280601.shtml"
        headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre)Gecko/2008072421 Minefield/3.0.2pre"}
        req=urllib.request.Request(start_url,headers=headers)
        data=urllib.request.urlopen(req)
        data=data.read()
        dammit=UnicodeDammit(data,["utf-8","gbk"])
        data=dammit.unicode_markup
        soup=BeautifulSoup(data,"lxml")
        infos = soup.find('tbody').children
        count = 0
        for info in infos:
            # print(info.text)
            name = info.find("a").text
            table = info.findAll("td")
            sNo = table[0].text.replace("\n","").replace(" ","")
            location = table[2].text.replace("\n","").replace(" ","")
            school_tag = info.a
            school_url = "https://www.shanghairanking.cn"+school_tag.get("href")
            # print(sNo,name,location)
            T = threading.Thread(target=self.rankingSpider,args=(school_url,headers,sNo,name,location))
            count+=1
            T.setDaemon(False)
            T.start()
            threads.append(T)
            # self.rankingSpider(school_url,headers)
        print("The End")
        print(time.time()-start_time)

    def rankingSpider(self,url,headers,sNo,name,location):
        # global threads
        # global count
        try:
            urls=[]
            req=urllib.request.Request(url,headers=headers)
            data=urllib.request.urlopen(req)
            data=data.read()
            dammit=UnicodeDammit(data,["utf-8","gbk"])
            data=dammit.unicode_markup
            soup=BeautifulSoup(data,"lxml")
            info=soup.findAll("p")[0].text
            imageLocation = soup.find('td',{'rowspan':'2','class':'univ-logo'}).find('img')['src']
            urlretrieve(imageLocation,'../../../schoolImg/'+name+'.png')
            print(sNo,name,location,info,'../../../schoolImg/'+name+'.png')
        except Exception as err:
            print(err)