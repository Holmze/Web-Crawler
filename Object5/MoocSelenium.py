from selenium import webdriver
import time
import pymysql

class Spider():
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}
    count = 1
    driver = webdriver.Edge(executable_path='C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
    driver.get('https://www.icourse163.org/channel/2001.htm')
    driver.maximize_window()

    def getInfo(self):
        print("Page",self.count)
        self.count += 1
        courses = self.driver.find_elements_by_xpath("//div[@class='_1gBJC']//div[@class='_2mbYw']//div[@class='_3KiL7']")
        titles = self.driver.find_elements_by_xpath("//div[@class='_1gBJC']/div/div//div[@class='_1Bfx4']/div//h3") #课程标题
        schools = self.driver.find_elements_by_xpath("//div[@class='_1gBJC']/div/div//div[@class='_1Bfx4']/div//p") #学校
        teachers = self.driver.find_elements_by_xpath("//div[@class='_1gBJC']/div/div//div[@class='_1Bfx4']/div//div[@class='_1Zkj9']") #授课老师
        for i in range(len(courses)):
            title = titles[i].text
            school = schools[i].text
            teacher = teachers[i].text
            course = courses[i]
            webdriver.ActionChains(self.driver).move_to_element(course).click(course).perform()
            time.sleep(3)
            # print(self.driver.current_url)
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[1])
            # self.getCourseInfo()
            note = self.driver.find_element_by_class_name("course-heading-intro_intro")
            # print(title,school,teacher,note.text)
            self.writeMySQL(title,school,teacher,note.text)
            self.driver.close()
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[0])
        self.nextPage()

    def getCourseInfo(self):
        try:
            note = self.driver.find_element_by_class_name("course-heading-intro_intro")
            print(note.text)
        except:
            notes = None
            print("err")

    def nextPage(self):
        try:
            GoButton = self.driver.find_element_by_xpath("//div[@class='_1lKzE']//a[@class='_3YiUU '][last()]")
            GoButton.click()
            time.sleep(3)
            self.getInfo()
        except:
            print("err")
            time.sleep(3)
            self.getInfo()

    def initDatabase(self):
        try:
            serverName = "127.0.0.1"
            # userName = "sa"
            passWord = "02071035"
            self.con = pymysql.connect(host = serverName,port = 3307,user = "root",password = passWord,database = "Mooc",charset = "utf8")
            self.cursor = self.con.cursor()
            self.cursor.execute("use Mooc")
            print("init DB over")
            self.cursor.execute("select * from mooc")
        except:
            print("init err")

    def writeMySQL(self,title,school,teacher,note):
        try:
            print(title,school,teacher,note)
            self.cursor.execute("insert mooc(title,school,teacher,note) values (%s,%s,%s,%s)",(title,school,teacher,note))
            self.con.commit()
        except Exception as err:
            print(err)
            # self.opened = False

spider = Spider()
spider.initDatabase()
spider.getInfo()