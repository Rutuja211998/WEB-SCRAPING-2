"""
This file containing code scraping form the weather website also here i am using selenium chrome driver
and successfully saved data into database, for saving code is present into pipeline.py file.
Author: Rutuja Tikhile.
Data:22/4/2020
"""
import scrapy
from ..items import WeatherItem
from mail_demo import SMTP_Mail


class WeathersSpider(scrapy.Spider):
    name = "weathersite"
    allowed_domains = ['forecast.weather.gov']

    def __init__(self):
        self.url = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Xp86XmYzbIU'

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse, headers=self.get_headers())

    def parse(self, response):

        wrapper = response.xpath('//ul[@id="seven-day-forecast-list"]')

        all_details = wrapper.xpath('//li[@class="forecast-tombstone"]')

        for detail in all_details:
            day = detail.xpath('.//p[@class="period-name"]/text()')[0].extract()
            forecast = detail.xpath('.//p[@class="short-desc"]/text()').extract()
            temp = detail.xpath('.//p[@class="temp temp-low"]/text()').extract()

            items = WeatherItem()

            items['day'] = day
            items['forecast'] = forecast
            items['temp'] = temp

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













# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# chromedriver="C:\\Users\\Dell\\Downloads\\chromedriver_win32\\chromedriver.exe"
# driver = webdriver.Chrome(chromedriver)
# driver.get("https://www.weather.gov/")
# search_element = driver.find_element_by_id("inputstring")
#
# submit_elem = driver.find_elements(By.XPATH, "//input[@id='btnSearch']")
# search_element.clear()
# about = 'San Francisco, CA, USA'
# about = input("Enter Your Query to Search: ")
# search_element.send_keys(about)
# submit_elem[0].send_keys(Keys.ENTER)
# self.driver.get(response.url)
#
#         search_element = self.driver.find_element_by_id("searchInput")
#
#         submit_elem = self.driver.find_elements(By.XPATH, "//input[@id='btnSearch']")
#
#         search_element.clear()
#         about = 'San Francisco, CA, USA'
#         about = input("Enter Your Query to Search: ")
#         search_element.send_keys(about)
#         submit_elem[0].send_keys(Keys.ENTER)
#         self.driver.close()
# about = response.xpath('//div[@class="col-sm-10 forecast-text"]/text()').extract()