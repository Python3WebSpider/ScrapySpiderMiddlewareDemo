from scrapy import Spider, Request

from scrapyspidermiddlewaredemo.items import DemoItem


class HttpbinSpider(Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_url = 'https://httpbin.org/get'
    
    def start_requests(self):
        for i in range(5):
            url = f'{self.start_url}?query={i}'
            yield Request(url, callback=self.parse)
    
    def parse(self, response):
        print('Status', response.status)
        item = DemoItem(**response.json())
        yield item
