from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request
import time
from urllib.parse import urlparse
import re
from random import random

# def getInternalLinks(bs,includeUrl):
#     includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme,urlparse(includeUrl).netloc)
#     internalLinks = []
#     ## 找出所有以“/”开头的链接
#     for link in bs.find_all('a',href=re.compile('^(/|.*'+includeUrl+')')):
#         if link.attrs['href'] is not None:
#             if link.attrs['href'] not in internalLinks:
#                 if(link.attrs['href'].startswith('/')):
#                     internalLinks.append(includeUrl+link.attr['href'])
#                 else:
#                     internalLinks.append(link.attrs['href'])
#     return internalLinks

def imageSpider(start_url):
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
                    download(url)
            except Exception as err:
                print(err)
        # nextUrl = getInternalLinks(soup,nextUrl)
        # start_url = nextUrl[random(len(nextUrl))]
        return start_url
    except Exception as err:
            print(err)

def download(url): 
    global count
    try:
        count=count+1
        #提取文件后缀扩展名
        if(url[len(url)-4]=="."):
            ext=url[len(url)-4:]
        else:
            ext=""
        req=urllib.request.Request(url,headers=headers)
        data=urllib.request.urlopen(req,timeout=100) 
        data=data.read() 
        fobj=open("Object3/singleThreadImages/"+str(count)+ext,"wb") 
        fobj.write(data)
        fobj.close()
        print("downloaded "+str(count)+ext)
    except Exception as err: 
        print(err)

start_time = time.time()
start_url = "http://www.weather.com.cn/"
# start_url="http://www.weather.com.cn/weather/101280601.shtml"
headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}
count=0
imageSpider(start_url)
# while(start_url is not None):
    # start_url = imageSpider(start_url)
    # print(start_url)
print("time:",time.time()-start_time)