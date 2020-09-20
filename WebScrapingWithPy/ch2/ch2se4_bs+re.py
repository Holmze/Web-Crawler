from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html,'html.parser')
images = bs.find_all('img',{'src':re.compile('\.\.\/img\/gifts.*\.jpg')})
for images in images:
    print(images['src'])