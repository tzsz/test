# -*- coding: utf-8 -*-
import scrapy


class JavSpider(scrapy.Spider):
    name = 'jav'
    allowed_domains = ['javlibrary.com']
    with open("a.txt", "rt") as f: 
        start_urls = [url.strip() for url in f.readlines()] 
    #start_urls = ['http://javlibrary.com/']

    def parse(self, response):
        pass
