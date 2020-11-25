# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RankingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    sNo = scrapy.Field()
    name = scrapy.Field()
    location = scrapy.Field()
    info = scrapy.Field()
    path = scrapy.Field()
