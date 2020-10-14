## scrapy runspider .\getStocks.py -s LOG_FILE=all.log
import scrapy
import re
import requests

class ArticleSpider(scrapy.Spider):
    name = 'stocks'

    def start_requests(self):
        url_head = 'http://97.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112406971740416068926_1601446076156&pn='
        url_tail = '&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1601446076157'
        urls = []
        for i in range(1,6):
            urls.append(url_head+str(i)+url_tail)
        # global count
        # count = 1
        # global count
        print('%-8s %-6s %-8s %10s %10s %12s %10s %10s %12s'%('序号','代码','名称','最新价','涨跌幅(%)','跌涨额(￥)','成交量(手)','成交额(￥)','涨幅(%)'))
        return [scrapy.Request(url = url,callback = self.parse) for url in urls]

    def parse(self,response):
        # global count
        url = response.url
        # print("=====================")
        
        # count = 1
        # global count
        # for i in range(1,6):
        self.get_stock(url)
        # self.get_stock(self,url,count)

    def get_stock(self,url):
        # global count
        json_page = requests.get(url).content.decode(encoding='utf-8')
        # json_page = json_page.read()
        pat = "\"diff\":\[\{.*\}\]"
        table = re.compile(pat,re.S).findall(json_page)
        pat = "\},\{"
        stocks = re.split(pat,table[0])
        # count = 1
        for stock in stocks:
            # print(stock)
            pat = ","
            infs = re.split(pat,stock)
            # print(infs[13])
            pat = ":"
            name = re.split(pat,infs[13])
            money = re.split(pat,infs[1])
            num = re.split(pat,infs[11])
            Quote_change = re.split(pat,infs[2])  # 涨跌幅
            Ups_and_downs = re.split(pat,infs[3])  # 涨跌额
            Volume = re.split(pat,infs[4])  #成交量
            Turnover = re.split(pat,infs[5])  #成交额
            Increase = re.split(pat,infs[6])  #涨幅
            # print(count,num[1],name[1],money[1],Quote_change[1]+"%",Ups_and_downs[1]+"￥",str(Volume[1])+"手",Turnover[1]+"￥",Increase[1]+"%")
            print('%-10s %-10s %10s %10s %15s %15s %18s %12s'%(num[1],name[1],money[1],Quote_change[1],Ups_and_downs[1],Volume[1],Turnover[1],Increase[1]))
            # count += 1
        # return count