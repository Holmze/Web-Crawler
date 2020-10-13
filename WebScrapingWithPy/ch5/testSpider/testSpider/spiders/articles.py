from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule

class ArticleSpider(CrawlSpider):
    name = 'articles'
    print(name)
    allowed_domains = ['www.cnblogs.com']
    print(name)
    start_urls = ['https://www.cnblogs.com/holmze/p/13797920.html']
    print(start_urls)
    rules = [Rule(LinkExtractor(allow = r'.*'),callback = 'parse_items',follow = True)]
    print(rules)

    def parse_items(self,response):
        print(response)
        url = response.url
        print(url)
        title = response.css('title::text').extract_first()
        text = response.xpath('//div[@id="post_list"]//text()').extract()
        # lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
        # lastUpdated = lastUpdated.replace('This page was last edited on ','')
        print('URL is: {}'.format(url))
        print('title is: {} '.format(title))
        print('text is: {}'.format(text))
        # print('Last updated: {}'.format(lastUpdated))