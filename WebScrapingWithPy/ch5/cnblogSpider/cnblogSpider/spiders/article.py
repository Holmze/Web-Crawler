import scrapy

class ArticleSpider(scrapy.Spider):
    name = 'article'

    def start_requests(self):
        urls = ['https://cn.bing.com/?FORM=Z9FD1'
        ,'https://edu.cnblogs.com/campus/fzu/SE2020/homework/11277'
        ,'https://www.cnblogs.com/easteast/'
        # ,'https://github.com/Holmze/031804103-051806129'
        ]
        return [scrapy.Request(url = url,callback = self.parse) for url in urls]

    def parse(self,response):
        url = response.url
        title = response.css('title::text').extract_first()
        # print("======================================")
        print('URL is: {}'.format(url))
        print('Title is: {}'.format(title))
        # print("======================================")