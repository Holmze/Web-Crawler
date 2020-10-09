# 从任意网页开始，随机从一个外链跳到另一个外链
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

page = set()
random.seed(datetime.datetime.now())

## 获取所有内链
def getInternalLinks(bs,includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme,urlparse(includeUrl).netloc)
    internalLinks = []
    ## 找出所有以“/”开头的link
    for link in bs.find_all('a',href=re.compile('^(/|.*'+includeUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks

def getExternalLinks(bs,excludeUrl):
    externalLinks = []
    ## 找出所有以“http” or “www”开头的且不包含当前的URL
    for link in bs.find_all('a',href = re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def getRandomExternalLinks(startingPage):
    html = urlopen(startingPage)
    bs = BeautifulSoup(html,'html.parser')
    externalLinks = getExternalLinks(bs,urlparse(startingPage).netloc)
    if len(externalLinks)==0:
        print('No external links, looking around the site for one')
        domain = '{}://{}'.format(urlparse(startingPage).scheme,urlparse(startingPage).netloc)
        internalLinks = getInternalLinks(bs,domain)
        return getRandomExternalLinks(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLinks = getRandomExternalLinks(startingSite)
    print("Random external link is {}".format(externalLinks))
    followExternalOnly(externalLinks)

followExternalOnly('https://edu.cnblogs.com/campus/fzu/SE2020')