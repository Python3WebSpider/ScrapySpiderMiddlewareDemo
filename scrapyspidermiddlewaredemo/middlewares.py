# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals, Item

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

from scrapyspidermiddlewaredemo.items import DemoItem


class CustomizeMiddleware(object):
    
    def process_spider_input(self, response, spider):
        response.status = 201
        return None
    
    def process_spider_output(self, response, result, spider):
        for i in result:
            if isinstance(i, DemoItem):
                i['origin'] = None
                yield i
    
    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.
        
        # Should return either None or an iterable of Request or item objects.
        pass
    
    def process_start_requests(self, start_requests, spider):
        for request in start_requests:
            url = request.url
            url += '&name=germey'
            request = request.replace(url=url)
            yield request
