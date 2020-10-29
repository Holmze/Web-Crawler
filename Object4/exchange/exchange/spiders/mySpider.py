# cd c:/mysql/mysql-8.0.22-winx64/mysql-8.0.22-winx64/bin
# teCBywk)M5aq
import scrapy
from exchange.items import ExchangeItem
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit

class MySpider(scrapy.Spider):
    name = "mySpider"
    source_url='http://fx.cmbchina.com/hq/'

    def start_requests(self):
        url = MySpider.source_url
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response): 
        try:
            dammit = UnicodeDammit(response.body, ["utf-8", "gbk"])
            data = dammit.unicode_markup
            # print(type(data))
            selector=scrapy.Selector(text=data)
            # print(type(selector))
            trs=selector.xpath("//div[@id = \"realRateInfo\"]//tr")
            # print(trs)
            # print(trs[0])
            for tr in trs:
                currency=tr.xpath("./td[@class = 'fontbold']/text()").extract_first()
                # print(currency)
                tsp = tr.xpath("./td[@class = 'numberright'][1]/text()").extract_first()
                # print(tsp)
                csp = tr.xpath("./td[@class = 'numberright'][2]/text()").extract_first()
                # print(csp)
                tbp = tr.xpath("./td[@class = 'numberright'][3]/text()").extract_first()
                # print(tbp)
                cbp = tr.xpath("./td[@class = 'numberright'][4]/text()").extract_first()
                # print(cbp)
                time = tr.xpath("./td[@align = 'center'][last()-1]/text()").extract_first()
                print(str(currency).strip(),str(tsp).strip(),str(csp).strip(),str(tbp).strip(),str(cbp).strip(),str(time).strip())
                #detail有时没有，结果None
                item=ExchangeItem()
                item["currency"]=currency.strip() if currency else ""
                item["tsp"]=tsp.strip() if tsp else ""
                item["csp"] = csp.strip()[1:] if csp else ""
                item["tbp"] = tbp.strip() if tbp else ""
                item["cbp"] = cbp.strip() if cbp else ""
                item["time"] = time.strip() if time else ""
                yield item
                #最后一页时trnk为None
            link=selector.xpath("//div[@class='paging']/ul[@name='Fy']/li[@class='next']/a/@href").extract_first()
            if link:
                url=response.urljoin(link)
                yield scrapy.Request(url=url, callback=self.parse)

        except Exception as err:
            print(err)

