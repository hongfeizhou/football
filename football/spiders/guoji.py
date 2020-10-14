import scrapy
from scrapy.selector import Selector
from scrapy.item import Item,Field
from ..items import FootballItem

class GuojiSpider(scrapy.Spider):
    name = 'guoji'
    allowed_domains = ['sports.sina.com.cn']
    start_urls = ['http://data.sports.sina.com.cn/live/']

    def parse(self, response):
        selector = Selector(response)
        articles = selector.xpath('//div[@id="m2"]/table/tr[position()> 2]')
        for article in articles:
            item = FootballItem()
            item['level'] = article.xpath('td[2]/text()').extract()
            item['date'] = article.xpath('td[3]/text()').extract()
            item['state'] = article.xpath('td[4]/span/text()').extract()
            item['home_team'] = article.xpath('td[5]/a/text()').extract()
            item['points'] = article.xpath('td[6]/a/span/font/text()').extract()
            item['away_team'] = article.xpath('td[7]/a/text()').extract()
            yield item
  
    