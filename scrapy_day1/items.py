# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class QuoteItem(scrapy.Item):
    '''
    quotes.toscrape.com
    '''
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
