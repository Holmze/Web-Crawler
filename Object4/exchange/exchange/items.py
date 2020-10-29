# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ExchangeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    currency = scrapy.Field()
    tsp = scrapy.Field()
    csp = scrapy.Field()
    tbp = scrapy.Field()
    cbp = scrapy.Field()
    time = scrapy.Field()
