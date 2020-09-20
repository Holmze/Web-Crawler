## 并不完善的一份代码，暂时不支持中文搜索

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

print("please input:")
item = input()
url = 'https://search.jd.com/Search?keyword='+item
html = urlopen(url)
bs = BeautifulSoup(html,'html.parser')
goods = bs.find_all("li",{"data-sku":re.compile("\d+")})
for good in goods:
    # print(good.get_text())
    # print(good)
    good_info = good.find("div",{"class":"p-name p-name-type-2"}).find('em').get_text()
    # print(good_info)
    price = good.find('div',{'class':'p-price'}).strong.i.get_text()
    print(good_info.replace("\n","").replace("\t",""),price,"￥")