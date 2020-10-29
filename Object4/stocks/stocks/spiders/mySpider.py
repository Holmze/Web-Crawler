import scrapy
from stocks.items import StocksItem
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import requests
import re

class MySpider(scrapy.Spider):
    name = "mySpider"
    key = 'NFV'
    url_head = 'http://5.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112406332527910963062_1603964168360&pn='
    url_tail = '&pz=50&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=&fs=b:MK0010&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f11,f62,f128,f136,f115,f152&_=1603964168385'
    urls = []

    def start_requests(self):
        url = MySpider.url_head+'1'+MySpider.url_tail
        print(url)
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response): 
        try:
            url = response.url
            json_page = requests.get(url).content.decode(encoding='utf-8')
            pat = "\"diff\":\[\{.*\}\]"
            table = re.compile(pat,re.S).findall(json_page)
            pat = "\},\{"
            stocks = re.split(pat,table[0])
            count = 1
            for stock in stocks:
                pat = ","
                infs = re.split(pat,stock)
                pat = ":"
                name = re.split(pat,infs[13])
                money = re.split(pat,infs[1])
                num = re.split(pat,infs[11])
                Quote_change = re.split(pat,infs[2])  # 涨跌幅
                Ups_and_downs = re.split(pat,infs[3])  # 涨跌额
                Volume = re.split(pat,infs[4])  #成交量
                Turnover = re.split(pat,infs[5])  #成交额
                Increase = re.split(pat,infs[6])  #涨幅
                print('%-8s %-10s %-10s %10s %10s %15s %15s %18s %12s'%(count,num[1],name[1],money[1],Quote_change[1],Ups_and_downs[1],Volume[1],Turnover[1],Increase[1]))
                count += 1
                item=StocksItem()
                item["name"]=name[1] if name else ""
                item["money"]=money[1] if money else ""
                item["num"] = num[1][1:] if num else ""
                item["Quote_change"] = Quote_change[1] if Quote_change else ""
                item["Ups_and_downs"] = Ups_and_downs[1] if Ups_and_downs else ""
                item["Volume"] = Volume[1] if Volume else ""
                item["Turnover"] = Turnover[1] if Turnover else ""
                item["Increase"] = Increase[1] if Increase else ""
                yield item

        except Exception as err:
            print(err)