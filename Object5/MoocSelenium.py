from selenium import webdriver
import time

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
        # self.StockInfo()
        courses = self.driver.find_elements_by_xpath("//div[@class='_1gBJC']//div[@class='_2mbYw']//div[@class='_3KiL7']")
        # course.click()
        titles = self.driver.find_elements_by_xpath("//div[@class='_1gBJC']/div/div//div[@class='_1Bfx4']/div//h3") #课程标题
        schools = self.driver.find_elements_by_xpath("//div[@class='_1gBJC']/div/div//div[@class='_1Bfx4']/div//p") #学校
        teachers = self.driver.find_elements_by_xpath("//div[@class='_1gBJC']/div/div//div[@class='_1Bfx4']/div//div[@class='_1Zkj9']") #授课老师
        # for i in range(len(titles)):
        #     print(titles[i].text,schools[i].text,teachers[i].text)
        for i in range(len(courses)):
            print(titles[i].text,schools[i].text,teachers[i].text)
            course = courses[i]
            webdriver.ActionChains(self.driver).move_to_element(course).click(course).perform()
            time.sleep(5)
            # print(self.driver.current_url)
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[1])
            self.getCourseInfo()
            self.driver.close()
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[0])
        self.nextPage()
    
    def getCourseInfo(self):
        try:
            notes = self.driver.find_elements_by_class_name("course-heading-intro_intro")
            for note in notes:
                print(note.text)
        except:
            print("err")
        # showAll = self.driver.find_element_by_class_name("cover-overflow-wrapper_btn j-btn")
        # showAll.click()


    def nextPage(self):
        try:
            GoButton = self.driver.find_element_by_xpath("//div[@class='_1lKzE']//a[@class='_3YiUU '][last()]")
            GoButton.click()
            time.sleep(5)
            self.getInfo()
        except:
            print("err")
            time.sleep(5)
            self.getInfo()

spider = Spider()
# spider.initDriver()
spider.getInfo()