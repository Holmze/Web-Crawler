from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request
# from urllib3 import request

url = 'http://www.weather.com.cn/weather/101230101.shtml'

try:
    headers = {"User-Agent":"Mozilla/5.0(Window U;Window NT 6.0 x64;en-US;rv:1.9pre) Gecko/208072421 Minefield/3.0.2pre"}
    req = urllib.request.Request(url,headers = headers)
    data = urllib.request.urlopen(req)
    data = data.read()
    dammit = UnicodeDammit(data,["utf-8","gbk"])
    data = dammit.unicode_markup
    soup = BeautifulSoup(data,"lxml")
    lis = soup.select("ul[class='t clearfix'] li")
    for li in lis:
        try:
            data = li.select('h1')[0].text
            weather = li.select('p[class="wea"]')[0].text
            temp = li.select('p[class = "tem"]  span')[0].text + "/"+li.select('p[class = "tem"]    i')[0].text
            print(data,weather,temp)
        except Exception as err:
            print(err)
except Exception as err:
    print(err)