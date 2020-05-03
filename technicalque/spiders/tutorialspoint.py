"""
This file containing code scraping the latest question on python, java and nodejs.
Author: Rutuja Tikhile.
Data:26/4/2020
"""
import scrapy
from ..items import TechnicalqueItem


class TechnicalpySpider(scrapy.Spider):
    name = "tutorials"
    allowed_domains = ['mindmajix.com', 'www.simplilearn.com']

    def __init__(self):
        self.url = "https://mindmajix.com/python-interview-questions"

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse, headers=self.get_headers())

    def parse(self, response):
        python = response.xpath('//div[@class="post-content"]')
        for que in python:
            pythonque = que.xpath('//div[@class="post-content"]/h3/span/text()').extract()
            pythonque = "".join(pythonque)
            items = TechnicalqueItem()
            items['pythonque'] = pythonque
            yield items

        url = "https://mindmajix.com/java-interview-questions"
        yield scrapy.Request(url=url, callback=self.parse_java, headers=self.get_headers())

    def parse_java(self, response):
        java = response.xpath('//div[@class="post-content"]')
        for ques in java:
            javaque = ques.xpath('//div[@class="post-content"]/h3/span/text()').extract()
            javaque = "".join(javaque)
            items = TechnicalqueItem()
            items['javaque'] = javaque
            yield items

        urls = "https://www.simplilearn.com/node-js-interview-questions-and-answers-article"
        yield scrapy.Request(url=urls, callback=self.parse_nodejs, headers=self.get_headers())

    def parse_nodejs(self, response):
        nodejs = response.xpath('//div[@class="desig_author empty-text"]')
        for quess in nodejs:
            nodejsque = quess.xpath('//div[@class="desig_author empty-text"]/ol/li/h3/text()').extract()
            nodejsque = "".join(nodejsque)
            items = TechnicalqueItem()
            items['nodejsque'] = nodejsque
            yield items

    def get_headers(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
            'Accept': 'application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
        }
        return headers