# -*- coding: utf-8 -*-
import scrapy
from scrapy_day1.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        """
        1、爬取每页的页面信息
        2、next_page获取下一页的地址，并生成新的url
        :param response:
        :return:
        """
        quotes = response.css(".quote")
        for quote in quotes:
            #初始化items里面给quotes设置的容器
            item = QuoteItem()
            #获取每条信息的text，author，tags信息
            text = quote.css(".text::text").extract_first()
            author = quote.css(".author::text").extract_first()
            tags = quote.css(".tags .tag::text").extract()
            #将上面获取到的每条信息，写入item容器
            item['text'] = text
            item['author'] = author
            item['tags'] = tags
            yield item
        #获取下一页的页数信息，如果还有真的还有下一页，就生成新的url，并返回给parse方法爬取，dont_filter=True(不参加去重，否则只能爬一页数据)
        next_page = response.css(".pager .next a::attr(href)").extract_first()
        if next_page:
            url = response.urljoin(next_page)
            yield scrapy.Request(url=url,callback=self.parse,dont_filter=True)