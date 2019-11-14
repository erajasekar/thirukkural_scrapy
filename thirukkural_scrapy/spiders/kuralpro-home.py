# -*- coding: utf-8 -*-
import scrapy


class KuralproSpider(scrapy.Spider):
    name = 'kuralpro-home'
    allowed_domains = ['kural.pro/tamil/']
    start_urls = ['http://kural.pro/tamil/']

    def parse(self, response):
        print ('[');
        for link in response.xpath("//a/@href").getall():
            index = link.find("adhigaram")
            if (index >= 0):
                print ("'" + link[index+10:] + "',")
        print (']');