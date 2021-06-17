# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsArticlesItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    headline = scrapy.Field()
    text = scrapy.Field()
    author = scrapy.Field()
    timestamp = scrapy.Field() 
    section = scrapy.Field()
