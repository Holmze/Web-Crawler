# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import pymysql

class DangdangPipeline(object):

    opened = False
    count = 0
    def open_spider(self,spider):
        try:
            print("*********************opened*********************")
            # self.con = pymysql.connect(host = "127.0.0.1",post = 3306,user = "root",passwd = "02071035",db = "MyDB",charset = "utf8")
            # serverName = "127.0.0.1:1433"
            serverName = "127.0.0.1"
            # userName = "sa"
            passWord = "*******"
            # port = "1433",user = userName,password = password,
            # ,server='SZS\SQLEXPRESS'
            self.con = pymysql.connect(host = serverName,port = 3306,user = "root",password = passWord,database = "MyDB",charset = "utf8")
            self.cursor = self.con.cursor()
            # self.cursor.execute('use MyDB')
            self.opened = True
            # self.count = 0
            # print(self.count)
        except Exception as err:
            print(err)
            self.opened = False

    def close_spider(self,spider):
        if self.opened>0:
            self.con.commit()
            self.con.close()
            # self.count = 0
            self.opened = False
        print("closed")
        print("一共爬取",self.count,"本书籍")

    def process_item(self, item, spider):
        try:
            print(item["title"])
            print(item["author"])
            print(item["publisher"])
            print(item["date"])
            print(item["price"])
            print(item["detail"])
            print()
            if self.opened:
                self.cursor.execute("insert books(bTitle,bAuthor,bPublisher,bDate,bPrice,bDetail) values (%s,%s,%s,%s,%s,%s)",(item["title"],item["author"],item["publisher"],item["date"],item["price"],item["detail"]))
                self.count+=1
        except Exception as err:
            print(err)
        return item