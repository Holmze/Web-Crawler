from selenium import webdriver
import time
import pymysql

class Spider():

    driver = webdriver.Edge(executable_path='C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
    driver.get('https://www.icourse163.org')
    driver.maximize_window()

    def sign_up(self):
        signUpButton = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div[3]/div[3]/div")
        signUpButton.click()
        time.sleep(1)
        # /html/body/div[16]/div[2]/div/div/div/div/div[2]/span
        otherWayButton = self.driver.find_element_by_xpath("/html/body/div[13]/div[2]/div/div/div/div/div[2]/span")
        otherWayButton.click()
        time.sleep(1)
        phoneNumber2SignUp = self.driver.find_element_by_xpath("/html/body/div[13]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[1]/ul/li[2]")
        phoneNumber2SignUp.click()
        time.sleep(3)

        # switch iframe
        temp_iframe_id = self.driver.find_elements_by_tag_name('iframe')[1].get_attribute('id') # choose iframe what you want
        self.driver.switch_to.frame(temp_iframe_id)

        phoneNumberInput = self.driver.find_element_by_xpath("//*[@id='phoneipt']")
        # keyInput = self.driver.find_element_by_class_name("paginate_input")
        phoneNumberInput.clear()
        phoneNumberInput.send_keys("15059575971")
        time.sleep(1)
        passWordInput = self.driver.find_element_by_xpath("//input[@class='j-inputtext dlemail']")
        passWordInput.clear()
        passWordInput.send_keys("sherlock1035")
        time.sleep(1)
        autoSignUp = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[7]/div/span")
        autoSignUp.click()
        signUpButton = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[6]/a")
        signUpButton.click()
        time.sleep(3)

    def Go2MyCourse(self):
        time.sleep(2)
        agreeButton = self.driver.find_element_by_xpath("//*[@id='privacy-ok']")
        agreeButton.click()
        time.sleep(2)
        MyCourse = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div[3]/div[4]")
        MyCourse.click()

    def get_course_info(self):
        courses = self.driver.find_elements_by_class_name("course-card-wrapper")
        for i in range(len(courses)):
            course = courses[i]
            # name = names[i]
            # school = schools[i]
            time.sleep(1)
            # name = self.driver.find_element_by_xpath()
            # print(course)
            self.get_course_detail(course)

    def get_course_detail(self,course):
        course_info = course.text.split("\n")
        name = course_info[0]
        school = course_info[1]
        state = course_info[2]
        date = course_info[3]
        # print(course_info)
        
        course.click()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        # self.getCourseInfo()
        teachers = self.driver.find_elements_by_class_name("f-fcgreen")
        for i in range(len(teachers)):
            teachers[i] = teachers[i].text
        note = self.driver.find_element_by_xpath("//*[@id='courseLearn-inner-box']/div/div[1]/div/div[3]/div/div[2]/div/div").text
        teacherss=""
        for teacher in teachers:
            if teacher != teachers[-1]:
                teacherss += (teacher+" ")
        print(course,name,school,date,teacherss,note)
        # self.writeMySQL(name,school,date,teacherss,note)
        # print(title,school,teacher,note.text)
        # self.writeMySQL(title,school,teacher,note.text)
        self.driver.close()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

    def initDatabase(self):
            try:
                serverName = "127.0.0.1"
                # userName = "sa"
                passWord = "02071035"
                self.con = pymysql.connect(host = serverName,port = 3307,user = "root",password = passWord,database = "MyMooc",charset = "utf8")
                self.cursor = self.con.cursor()
                self.cursor.execute("use MyMooc")
                print("init DB over")
                # self.cursor.execute("select * from mooc")
            except:
                print("init err")

    def writeMySQL(self,name,school,date,teachers,note):
        try:
            print(name,school,date,teachers,note)
            self.cursor.execute("insert Mooc(name,school,date,teachers,note) values (%s,%s,%s,%s,%s)",(name,school,date,teachers,note))
            self.con.commit()
        except Exception as err:
            print(err)
            # self.opened = False


spider = Spider()
spider.initDatabase()
spider.sign_up()
spider.Go2MyCourse()
spider.get_course_info()