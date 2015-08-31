# -*- coding: utf-8 -*-
import scrapy


class CodeevalScraperItem(scrapy.Item):
    level = scrapy.Field()
    name = scrapy.Field()
    passed = scrapy.Field()
