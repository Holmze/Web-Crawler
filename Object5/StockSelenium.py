from selenium import webdriver
import time

class Spider():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}
    count = 1
    # def initDriver(self):
        # count = 1
    driver = webdriver.Edge(executable_path='C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
    driver.get('http://quote.eastmoney.com/center/gridlist.html')

    def getInfo(self):
        print("Page",self.count)
        self.count += 1
        self.StockInfo()
        try:
            keyInput = self.driver.find_element_by_class_name("paginate_input")
            keyInput.clear()
            keyInput.send_keys(self.count)
            # keyInput.send_keys(self.count.ENTER)
            GoButton = self.driver.find_element_by_class_name("paginte_go")
            GoButton.click()
            time.sleep(3)
            self.getInfo()
        except:
            print("err")
            time.sleep(3)
            self.getInfo()
            
    def StockInfo(self):
        odds = self.driver.find_elements_by_class_name("odd")
        evens = self.driver.find_elements_by_class_name("even")
        for i in range(len(odds)):
            self.StockDetailInfo(odds[i])
            self.StockDetailInfo(evens[i])

    def StockDetailInfo(self,elem):
        tds = elem.find_elements_by_tag_name("td")
        count = tds[0].text
        # for td in tds:
        #     print(td.text,end = " ")
        # print()
        # Volume
        num = tds[1].text
        name = tds[2].text
        value = tds[4].text
        Quote_change = tds[5].text
        Ups_and_downs = tds[6].text
        print(count,num,name,value,Quote_change,Ups_and_downs)
        # for value in values:
        # print(num,name,values[0].text,values[1].text)

spider = Spider()
# spider.initDriver()
spider.getInfo()