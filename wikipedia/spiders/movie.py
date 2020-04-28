"""
This file containing scarping for the wikipedia using scrapy also successfully saved data in database,
code for saving is present in pipelines.py.
Author: Rutuja Tikhile.
Data:19/4/2020
"""
import scrapy
from ..items import WikipediaItem
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class OscarsSpider(scrapy.Spider):
    name = "oscars"
    allowed_domains = ['www.wikipedia.org']

    def __init__(self):
        self.driver_path = "C:\\Users\\Dell\\Downloads\\chromedriver_win32\\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.url = 'https://www.wikipedia.org/'

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse, headers=self.get_headers())

    def parse(self, response):
        self.driver.get(response.url)

        search_element = self.driver.find_element_by_id("searchInput")

        submit_elem = self.driver.find_elements(By.XPATH, "//button[@class='pure-button pure-button-primary-progressive']")
        search_element.clear()

        about = input("Enter Your Query to Search: ")
        search_element.send_keys(about)
        submit_elem[0].send_keys(Keys.ENTER)
        self.driver.close()

        for href in response.css(r"tr[style='background:#FAEB86'] a[href*='film)']::attr(href)").extract():
            url = response.urljoin(href)
            req = scrapy.Request(url, callback=self.parse_titles)
            yield req

    def parse_titles(self, response):

        items = WikipediaItem()

        for sel in response.css('html').extract():
            items['title'] = response.css(r"h1[id='firstHeading'] i::text").extract()
            items['director'] = response.css(r"tr:contains('Directed by') a[href*='/wiki/']::text").extract()
            items['starring'] = response.css(r"tr:contains('Starring') a[href*='/wiki/']::text").extract()
            items['releasedate'] = response.css(r"tr:contains('Release date') li::text").extract()
            items['runtime'] = response.css(r"tr:contains('Running time') td::text").extract()

        yield items

    def get_headers(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
            'Accept': 'application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
            }
        return headers


# driver.get("https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture")