import requests,bs4
url = "http://www.shanghairanking.cn/rankings/bcur/2020"
soup = bs4.BeautifulSoup(requests.get(url).content.decode(),"html.parser")
information = []
for child in soup.find("tbody").children:
    res = child.find_all("td")
    information.append([res[0].text.strip() + "    " + res[1].text.strip() + "    " + res[2].text.strip() + "    " +
                        res[3].text.strip() + "    " + res[4].text.strip()])
print("排名  学校名称  省份  学校类型  总分")
for info in information:
    print(info)
