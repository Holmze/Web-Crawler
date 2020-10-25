from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from cnblogSpider.items import Article

class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['https://pdos.csail.mit.edu/6.824/']
    start_urls = ['https://pdos.csail.mit.edu/6.824/schedule.html']
    # allowed_domains = ['www.cnblogs.com']
    # start_urls = ['https://www.cnblogs.com/holmze/p/13797920.html']
    ## 使用re匹配，爬取cnblog上的所有个人博客页面
    rules = [Rule(LinkExtractor(allow = r'.*holmze.*'),callback = 'parse_items',follow = True)]

    def parse_items(self,response):
        article = Article()
        article['url'] = response.url
        # print(url)
        article['title'] = response.css('title::text').extract_first()
        # text = response.css('div#cnblogs_post_body::text').extract_first()
        article['text'] = response.xpath('//div[@id="cnblogs_post_body"]//text()').extract()
        article['lastUpdated'] = response.css('span#post-date::text').extract_first()
        # lastUpdated = lastUpdated.replace('This page was last edited on ','')
        # print('URL is: {}'.format(url))
        # print('title is: {} '.format(title))
        # print('text is: {}'.format(text))
        # print('Last updated: {}'.format(lastUpdated))
        return article