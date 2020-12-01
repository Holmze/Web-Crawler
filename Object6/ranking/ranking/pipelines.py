# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class RankingPipeline:
    def open_spider(self,spider):
        try:
            print("*******************opened MySQL*******************")
            # self.con = pymysql.connect(host = "127.0.0.1",post = 3306,user = "root",passwd = "02071035",db = "MyDB",charset = "utf8")
            # serverName = "127.0.0.1:1433"
            serverName = "127.0.0.1"
            # userName = "sa"
            passWord = "02071035"
            self.con = pymysql.connect(host = serverName,port = 3306,user = "root",password = passWord,database = "ranking",charset = "utf8")
            self.cursor = self.con.cursor()
            self.cursor.execute('use ranking')
        except Exception as err:
            print(err)
            self.opened = False

    def close_spider(self,spider):
        # if self.opened>0:
        self.con.commit()
        self.con.close()
            # self.count = 0
            # self.opened = False
        print("closed")
        # print("一共爬取",self.count,"种外汇")

    def process_item(self, item, spider):
        print("Process item")
        try:
            # print("insert")
            # if self.opened:
            self.cursor.execute("insert ranking(sNo,sName,location,info,path) values (%s,%s,%s,%s,%s)",(item["sNo"],item["name"],item["location"],item["info"],item["path"]))
            # print("insert ranking(sNo,sName,location,info,path) values (%s,%s,%s,%s,%s)",(item["sNo"],item["name"],item["location"],item["info"],item["path"]))
        except Exception as err:
            print(err)
        return item
