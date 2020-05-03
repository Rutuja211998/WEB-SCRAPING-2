"""
This file containing code scraping the latest question on python, java and nodejs.
Author: Rutuja Tikhile.
Data:26/4/2020
"""
import scrapy
from ..items import TechnicalqueItem


class TechnicalpySpider(scrapy.Spider):
    name = "ques"
    allowed_domains = ['hackr.io']

    def __init__(self):
        self.url = "https://hackr.io/blog/java-interview-questions"

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse, headers=self.get_headers())

    def parse(self, response):
        java1 = response.xpath('//h4[@id="question-what-is-java"]/strong/text()')[0].extract()
        java2 = response.xpath('//h4[@id="question-what-are-the-features-of-java"]/strong/text()')[0].extract()
        java3 = response.xpath('//h4[@id="question-differentiate-between-jvm-jre-and-jdk"]/strong/text()')[0].extract()
        java4 = response.xpath('//h4[@id="question-how-does-java-enable-high-performance"]/strong/text()')[0].extract()
        java5 = response.xpath('//h4[@id="question-could-you-explain-the-oops-concepts"]/strong/text()')[0].extract()
        java6 = response.xpath('//h4[@id="question-what-do-you-understand-by-java-ides"]/strong/text()')[0].extract()
        java7 = response.xpath('//h4[@id="question-java-is-a-platform-independent-language-why"]/strong/text()')[0].extract()
        java8 = response.xpath('//h4[@id="question-explain-typecasting"]/strong/text()')[0].extract()
        java9 = response.xpath('//h4[@id="questions-explain-access-modifiers-in-java"]/strong/text()')[0].extract()
        java10 = response.xpath('//h4[@id="question-please-explain-method-overriding-in-java"]/strong/text()')[0].extract()
        items = TechnicalqueItem()

        items['java1'] = java1
        items['java2'] = java2
        items['java3'] = java3
        items['java4'] = java4
        items['java5'] = java5
        items['java6'] = java6
        items['java7'] = java7
        items['java8'] = java8
        items['java9'] = java9
        items['java10'] = java10

        yield items

        print("2nd")
        url = "https://hackr.io/blog/python-interview-questions"
        yield scrapy.Request(url=url, callback=self.parse_python, headers=self.get_headers())

    def parse_python(self, response):
        py1 = response.xpath('//h4[@id="question-explain-python"]/strong/text()')[0].extract()
        py2 = response.xpath('//h4[@id="question-what-are-the-distinct-features-of-python"]/strong/text()')[0].extract()
        py3 = response.xpath('//h4[@id="question-why-do-we-use-pythonstartup-environment-variable"]/strong/text()')[0].extract()
        py4 = response.xpath('//h4[@id="question-define-tuples-in-python"]/strong/text()')[0].extract()
        py5 = response.xpath('//h4[@id="question-what-are-the-built-in-types-provided-by-the-python"]/text()')[0].extract()
        py6 = response.xpath('//h4[@id="question-why-do-we-need-a-break-in-python"]/strong/text()')[0].extract()
        py7 = response.xpath('//h4[@id="question-what-is-the-map-function-used-for-in-python"]/text()')[0].extract()
        py8 = response.xpath('//h4[@id="question-what-is-the-lambda-function"]/text()')[0].extract()
        py9 = response.xpath('//h4[@id="question-what-are-python-modules"]/text()')[0].extract()
        py10 = response.xpath('//h4[@id="question-what-is-the-split-function-used-for"]/text()')[0].extract()

        items = TechnicalqueItem()
        items['py1'] = py1
        items['py2'] = py2
        items['py3'] = py3
        items['py4'] = py4
        items['py5'] = py5
        items['py6'] = py6
        items['py7'] = py7
        items['py8'] = py8
        items['py9'] = py9
        items['py10'] = py10

        yield items

    def get_headers(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
            'Accept': 'application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
        }
        return headers


# from selenium import webdriver
# chromedriver="C:\\Users\\Dell\\Downloads\\chromedriver_win32\\chromedriver.exe"
# driver = webdriver.Chrome(chromedriver)
# driver.get("https://hackr.io/blog/java-interview-questions")
# driver.close()
