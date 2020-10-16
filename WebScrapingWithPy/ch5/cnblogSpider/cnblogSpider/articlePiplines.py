# scrapy runspider .\articlePiplines.py -s LOG_FILE=all.log
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from cnblogSpider.items import Article

class ArticleSpider(CrawlSpider):
    name = 'articlesPiplines'
    allowed_domains = ['www.cnblogs.com']
    start_urls = ['https://www.cnblogs.com/holmze/']
    # start_urls = ['https://www.cnblogs.com/holmze/p/13797920.html']
    ## 使用re匹配，爬取cnblog上的所有个人博客页面
    rules = [Rule(LinkExtractor(allow = r'.*holmze\/p.*'),callback = 'parse_items',follow = True)]

    def parse_items(self,response):
        article = Article()
        article['url'] = response.url
        # print(url)
        article['title'] = response.css('title::text').extract_first()
        # text = response.css('div#cnblogs_post_body::text').extract_first()
        article['text'] = response.xpath('//div[@id="cnblogs_post_body"]//text()').extract()
        article['lastUpdated'] = response.css('span#post-date::text').extract_first()
        # print(article['lastUpdated'])
        # print(article['lastUpdated'],":",article['title'])
        # lastUpdated = lastUpdated.replace('This page was last edited on ','')
        # print('URL is: {}'.format(url))
        # print('title is: {} '.format(title))
        # print('text is: {}'.format(text))
        # print('Last updated: {}'.format(lastUpdated))
        return article