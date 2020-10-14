import scrapy
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request
import time
from urllib.parse import urlparse
import re
from random import random

class ArticleSpider(scrapy.Spider):
    name = 'weather'

    def start_requests(self):
        urls = ['http://www.weather.com.cn/']
        return [scrapy.Request(url = url,callback = self.parse) for url in urls]

    def parse(self,response):
        url = response.url
        start_time = time.time()
        # start_url = "http://www.weather.com.cn/"
        # start_url="http://www.weather.com.cn/weather/101280601.shtml"
        headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}
        count=0
        self.imageSpider(url,headers,count)
        # while(start_url is not None):
            # start_url = imageSpider(start_url)
            # print(start_url)
        print(time.time()-start_time)
        # imageSpider(url)
        # print("end")
        # title = response.css('title::text').extract_first()
        # print("======================================")
        # print('URL is: {}'.format(url))
        # print('Title is: {}'.format(title))
        # print("======================================")

    def imageSpider(self,start_url,headers,count):
        try:
            # nextUrl = []
            urls=[]
            req=urllib.request.Request(start_url,headers=headers)
            data=urllib.request.urlopen(req)
            data=data.read()
            dammit=UnicodeDammit(data,["utf-8","gbk"])
            data=dammit.unicode_markup
            soup=BeautifulSoup(data,"lxml")
            images=soup.select("img")
            for image in images: 
                try:
                    src=image["src"]
                    url=urllib.request.urljoin(start_url,src) 
                    if url not in urls:
                        urls.append(url) 
                        print(url)
                        self.download(url,headers,count)
                        count += 1
                except Exception as err:
                    print(err)
            # nextUrl = getInternalLinks(soup,nextUrl)
            # start_url = nextUrl[random(len(nextUrl))]
            return start_url
        except Exception as err:
                print(err)

    def download(self,url,headers,count):
        try:
            if(url[len(url)-4]=="."):
                ext=url[len(url)-4:]
            else:
                ext=""
            req=urllib.request.Request(url,headers=headers)
            data=urllib.request.urlopen(req,timeout=100)
            data=data.read()
            fobj=open("scrapyImages/"+str(count)+ext,"wb")
            fobj.write(data)
            fobj.close()
            print("downloaded "+str(count)+ext)
        except Exception as err:
            print(err)