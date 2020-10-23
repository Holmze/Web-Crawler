import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDir = 'WebScrapingWithPy//ch6//downloaded/'
baseUrl = 'http://pythonscraping.com'

def getAbsoluteURL(baseUrl,source):
    # print(source)
    if source.startswith('http://www.'):
        url = 'http://{}'.format(source[11:])
        # print("start with http://www",url)
    elif source.startswith('http://'):
        url = source
        # print("start with http://",url)
    elif source.startswith('www.'):
        # url = source[4:]
        url = 'http://{}'.format(source[4:])
        # print("start with www",url)
    else:
        # url = source
        url = '{}/{}'.format(baseUrl,source)
        # print("else",url)
    
    if baseUrl not in url:
        return None
    # print(url)
    return url

def getDownloadPath(baseUrl,absoluteUrl,downloadDir):
    path = absoluteUrl.replace('www.','')
    print(path)
    path = path.replace(baseUrl,'')
    print(path)
    path = downloadDir+path
    print(path)
    directory = os.path.dirname(path)
    print('dir is:',directory)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html,'html.parser')
downloadList = bs.findAll(src=True)
# print(downloadList)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl,download['src'])
    # print(fileUrl)
    if fileUrl is not None and fileUrl[-4:]=='.jpg':
        # print(fileUrl)
        urlretrieve(fileUrl,getDownloadPath(baseUrl,fileUrl,downloadDir))