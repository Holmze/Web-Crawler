from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
import re

match_url = 'https://www.whoscored.com/Matches/1491970/Live/Spain-LaLiga-2020-2021-Real-Sociedad-Real-Madrid'
# html = urlopen(url)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
req = Request(url=match_url, headers=headers)  
urlopen(req).read() 

# bs = BeautifulSoup(html,'html.parser')
# match_info = bs.findAll('div',{'class':'match-centre-info'})
# print(match_info)