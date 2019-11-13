# -*- coding: utf-8 -*-
import scrapy


class KuralproSpider(scrapy.Spider):
    name = 'kuralpro'
    allowed_domains = ['kural.pro/tamil/']
    start_urls = ['http://kural.pro/tamil/']

    def parse(self, response):
        pass
