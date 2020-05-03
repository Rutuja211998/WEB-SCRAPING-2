"""
This file containing scarping for the worldometer website using scrapy and i am saving scraped data into database
successfully, code for saving is present in the pipelines.py file .
Author: Rutuja Tikhile.
Data: 29/4/2020
"""
import scrapy
from ..items import CoronaItem


class CoronaSpider(scrapy.Spider):
    name = "virus"
    allowed_domains = ['www.worldometers.info']

    def __init__(self):
        self.url = "https://www.worldometers.info/coronavirus/country/india/"

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse, headers=self.get_headers())

    def parse(self, response):
        wrapper = response.xpath('//div[@class="content-inner"]')

        for result in wrapper:
            coronavirus = result.xpath('.//div[@class="maincounter-number"]/span/text()')[0].get()
            deaths = result.xpath('.//div[@class="maincounter-number"]/span/text()')[1].get()
            recovred = result.xpath('.//div[@class="maincounter-number"]/span/text()')[2].get()
            countries = result.xpath('//div[@style="text-align:center;width:100%"]/h1/text()').extract()[1]

            items = CoronaItem()

            items['coronavirus_cases'] = coronavirus
            items['deaths_cases'] = deaths
            items['recovred_cases'] = recovred
            items['countries'] = countries
            yield items

        country_list = ['china','south-korea','iran','italy','spain','france','us']
        for country in country_list:
            next_url = f'https://www.worldometers.info/coronavirus/country/{country}'
            yield scrapy.Request(url=next_url, callback=self.parse, headers=self.get_headers())

    def get_headers(self):
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
                'Accept': 'application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
            }
        return headers

