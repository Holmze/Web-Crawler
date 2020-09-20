from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
# bs = BeautifulSoup(html.read(),'html.parser')
# html.read()
bs = BeautifulSoup(html,'html.parser')
# print(bs.h1)
# print(bs.html.body.h1)
# print(bs.body)
# print("----------------")
# nameList = bs.findAll('tr')
# for name in nameList:
#     # print(name.get_text())
#     print(name)
###### children
for child in bs.find('table',{'id':'giftList'}).children:
    print(child)

print("----------------")

######## next_siblings：遍历table下的所有兄弟节点，不包括表格标题
for sibling in bs.find('table',{'id':'giftList'}).tr.next_siblings:
    print(sibling)

####### parents
print("-------------------")
print(bs.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())