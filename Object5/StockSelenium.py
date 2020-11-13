from selenium import webdriver
import time
import pymysql

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
        num = tds[1].text #编号
        name = tds[2].text #名称
        value = tds[4].text # 最新价
        Quote_change = tds[5].text # 涨跌幅
        Ups_and_downs = tds[6].text # 涨跌额
        Volume = tds[7].text # 成交量
        Turnover = tds[8].text # 成交额
        amplitude = tds[9].text # 振幅
        highest = tds[10].text # 最高
        lowest = tds[11].text # 最低
        today_begin = tds[12].text # 进开
        last_day = tds[13].text # 昨收
        print(count,num,name,value,Quote_change,Ups_and_downs,Volume,Turnover,amplitude,highest,lowest,today_begin,last_day)
        self.writeMySQL()
        # for value in values:
        # print(num,name,values[0].text,values[1].text)

    def initDatabase(self):
        try:
            serverName = "127.0.0.1"
            # userName = "sa"
            passWord = "02071035"
            self.con = pymysql.connect(host = serverName,port = 3307,user = "root",password = passWord,database = "Stock",charset = "utf8")
            self.cursor = self.con.cursor()
            self.cursor.execute("use Stock")
            print("init DB over")
            self.cursor.execute("select * from stock")
        except:
            print("init err")

    def writeMySQL(self):
        try:
            print()
            self.cursor.execute("insert stock(count,num,name,value,Quote_change,Ups_and_downs,Volume,Turnover,amplitude,highest,lowest,today_begin,last_day) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.count,self.num,self.name,self.value,self.Quote_change,self.Ups_and_downs,self.Volume,self.Turnover,self.amplitude,self.highest,self.lowest,self.today_begin,self.last_day))
            self.con.commit()
        except Exception as err:
            print(err)
            # self.opened = False


spider = Spider()
spider.initDatabase()
spider.getInfo()