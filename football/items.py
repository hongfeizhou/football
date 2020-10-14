# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FootballItem(scrapy.Item):
    # define the scrapy.fields for your item here like:
    # name = scrapy.Field()
    level = scrapy.Field()
    date = scrapy.Field()
    state = scrapy.Field()
    home_team = scrapy.Field()
    away_team = scrapy.Field()
    points = scrapy.Field()