from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request
import re
import requests

url = 'http://42.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112405745106134428015_1601432122362&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1601432122363'

json_page = requests.get(url).content.decode(encoding='utf-8')
# json_page = json_page.read()
pat = "\"diff\":\[\{.*\}\]"
# pat = "\"f.\".*,"
# pat = "\"f14\":\".*\","
# pat = "\{.*\},"
table = re.compile(pat,re.S).findall(json_page)
pat = "\},\{"
stocks = re.split(pat,table[0])
for stock in stocks:
    # print(stock)
    pat = ","
    infs = re.split(pat,stock)
    # print(infs[13])
    pat = ":"
    name = re.split(pat,infs[13])
    money = re.split(pat,infs[1])
    print(name[1],money[1])