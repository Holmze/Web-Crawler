from bs4 import BeautifulSoup as BS
from bs4 import UnicodeDammit
import urllib.request
import re
import requests
import threading

url_head = "https://movie.douban.com/top250?start="
url_tail = "&filter="


def get_movie_info(url,Quote,img_url):
    headers = {"User-Agent":"Mozilla/5.0(Window U;Window NT 6.0 x64;en-US;rv:1.9pre) Gecko/208072421 Minefield/3.0.2pre"}
    req = urllib.request.Request(url,headers=headers)
    data = urllib.request.urlopen(req).read()
    dammit = UnicodeDammit(data,["utf-8","gbk"])
    data = dammit.unicode_markup
    soup = BS(data,"lxml")
    name = soup.select("span[property='v:itemreviewed']")[0].text
    name = re.split(" ",name)[0]
    director = soup.select("span[class='attrs'] a")[0].text
    actors = soup.select("span[class='actor'] a")
    actor_list = ""
    for i in range(3):
        actor_list += (actors[i].text)
        if i < 2:
            actor_list += ","
    time = soup.select("span[property='v:initialReleaseDate']")[0].text
    style = soup.select("span[property='v:genre']")
    style_list = ""
    for i in range(len(style)):
        style_list+=style[i].text
        if i < (len(style)-1):
            style_list += "/"
    score = soup.select("strong[class='ll rating_num']")[0].text
    vote_number = soup.select("span[property='v:votes']")[0].text
    img_file = requests.get(img_url).content
    with open("Object6\images/"+name+".webp","wb") as f:
        f.write(img_file)
        f.close()
        # print(name,"over")
    # <strong class="ll rating_num" property="v:average">9.7</strong>
    # pat = " "
    # nation = re.split(pat,soup.text)
    # print(nation)
    print(name,director,actor_list,time,style_list,score,vote_number,Quote,"Object6\images/"+name+".jpg")

try:
    threads=[]
    headers = {"User-Agent":"Mozilla/5.0(Window U;Window NT 6.0 x64;en-US;rv:1.9pre) Gecko/208072421 Minefield/3.0.2pre"}
    for i in range(10):
        url = url_head+str(i*50)+url_tail
        req = urllib.request.Request(url,headers=headers)
        # print(req)
        data = urllib.request.urlopen(req).read()
        # data = data.read()
        dammit = UnicodeDammit(data,["utf-8","gbk"])
        data = dammit.unicode_markup
        soup = BS(data,"lxml")
        lis = soup.select("ol[class='grid_view'] li")
        count = 0
        urls = []
        for li in lis:
            tag = li.a
            Quote = soup.select("span[class='inq']")[count].text
            # count += 1
            movie_url = tag.get("href")
            tag = li.img
            img_url = tag.get("src")
            if movie_url not in urls:
                count += 1
                print(count)
                T=threading.Thread(target=get_movie_info,args=(movie_url,Quote,img_url))
                T.setDaemon(False)
                T.start() 
                threads.append(T)
                urls.append(movie_url)
            # get_movie_info(movie_url,Quote,img_url)
except Exception as err:
    print(err)
