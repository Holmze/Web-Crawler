from urllib.request import urlopen
from bs4 import BeautifulSoup
# from urllib import urlretrieve
import requests

url = 'http://xcb.fzu.edu.cn/'
html = urlopen(url)
bs = BeautifulSoup(html,'html.parser')
name = 1
for imgs in bs.find('div',{'class':'content'}).find_all('img'):
    # if 'src' in imgs.attrs:
    #     print(imgs)
    img = imgs['src']
    if img[-3:] != 'gif':
        if img[:4] == 'http':
            path = img
        else:
            path = url+img
    else:
        continue
    print(path)
    # img_data = urlopen(path)
    # img_data = img_data.read()
    img_file = requests.get(path).content
    with open("Object1：爬取学生信息\images/"+str(name)+".jpg","wb") as f:
        f.write(img_file)
        f.close()
        print(name,"over")
        name += 1
