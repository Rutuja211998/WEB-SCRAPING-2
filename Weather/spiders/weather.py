"""
This file containing code scraping form the weather website also here successfully saved data into database,
for saving code is present into pipeline.py file.
Author: Rutuja Tikhile.
Data:26/4/2020
"""
import scrapy
from ..items import WeatherItem
from mail_demo import SMTP_Mail


class WeathersSpider(scrapy.Spider):
    name = "weather"
    allowed_domains = ['forecast.weather.gov']

    def __init__(self):
        self.url = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Xp86XmYzbIU'

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse, headers=self.get_headers())

    def parse(self, response):
        wrapper = response.xpath('//div[@id="detailed-forecast-body"]')
        detail_forecast = wrapper.xpath('//div[@class="row row-odd row-forecast"]')
        for forecast in detail_forecast:
            day = forecast.xpath('.//div[@class="col-sm-2 forecast-label"]/b/text()')[0].extract()
            details = forecast.xpath('.//div[@class="col-sm-10 forecast-text"]/text()')[0].extract()

            items = WeatherItem()
            items['day'] = day
            items['details'] = details

            yield items

        user_email = 'rutujatikhile@gmail.com'
        SMTP_Mail().send_mail(user_email)
        print("email sent")

    def get_headers(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
            'Accept': 'application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
        }
        return headers
