# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class CnblogspiderPipeline:
#     def process_item(self, item, spider):
#         return item

from datetime import datetime
from cnblogSpider.items import Article
from string import whitespace

class CnblogspiderPipeline(object):
    def process_item(self,article,spider):
        dateStr = article['lastUpdated']
        # if article['lastUpdated'] is not None:
        #     article['lastUpdated'] = article['lastUpdated'].strip()
        #     article['lastUpdated'] = datetime.strptime(article['lastUpdated'],'%Y-%B-%d %H:%M')
        # print(dateStr)
        article['text'] = [line for line in article['text'] if line not in whitespace]
        article['text'] = ''.join(article['text'])
        article['title'] = str(article['title']).split('-')[0]
        print(article['lastUpdated'],":",article['title'],"in",article['url'])
        # print(article['text'])
        return article