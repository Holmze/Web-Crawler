# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class StocksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    name = scrapy.Field()
    money = scrapy.Field()
    num = scrapy.Field()
    Quote_change = scrapy.Field()
    Ups_and_downs = scrapy.Field()
    Volume = scrapy.Field()
    Turnover = scrapy.Field()
    Increase = scrapy.Field()