"""
This file containing scarping for the realestate website using scrapy and i am saving scraped data into database
successfully, code for saving is present in the pipelines.py file .
Author: Rutuja Tikhile.
Data: 25/4/2020
"""
import scrapy
from ..items import RealestateItem


class MakaanSpider(scrapy.Spider):
    name = "makaan"
    allowed_domains = ['makaan.com']

    def __init__(self):
        self.url = "https://www.makaan.com/mumbai-residential-property/buy-property-in-mumbai-city"

    def start_requests(self):
        url = "https://www.makaan.com/mumbai-residential-property/buy-property-in-mumbai-city"
        yield scrapy.Request(url=url, callback=self.parse, headers=self.get_headers())

    def parse(self, response):
        if not response:
            print("Failed to fetch the page")
            return None

        r = response.xpath('.//div[contains(@class,"zero-results-similar-wrap minheight ") ]')
        all_cards = r.xpath('.//ul/li[contains(@class,"cardholder") ]')

        for card in all_cards:
            main_content = card.xpath('.//div[contains(@class,"infoWrap") ]')
            pre_title = main_content.xpath('.//a[contains(@class,"typelink") ]//child::node()/text()').extract()
            mid_title = main_content.xpath(
                './/a[contains(@data-link-type,"project overview")]/ancestor::node()/text()').extract()
            post_title = main_content.xpath(
                './/a[contains(@data-link-type,"project overview")]/child::node()/text()').extract()

            title_preparing = pre_title + list(mid_title) + post_title
            title = "".join(title_preparing)
            property_location = main_content.xpath(
                './/span[contains(@class,"locName") ]/descendant::node()/text()').getall()
            property_location = "".join(property_location)

            x, price, price_unit, per_sqr_ft, area, area_unit, status, construction_status = 8 * " "
            about_property = main_content.xpath('.//tr[contains(@class,"hcol")]/descendant::node()/text()').getall()
            if len(about_property) == 8:
                x, price, price_unit, per_sqr_ft, area, area_unit, status, construction_status = about_property
            price = price + price_unit
            per_sqr_ft = per_sqr_ft.split('/')[0]
            construction_status = status
            construction_years = main_content.xpath('.//ul[contains(@class,"listing-details")]/descendant::node()/text()').get()

            print(price, per_sqr_ft, construction_status, construction_years)

            item =RealestateItem()

            item['title'] = title
            item['property_location'] = property_location
            item['price'] = price
            item['per_sqr_ft'] = per_sqr_ft
            item['area'] = area
            item['construction_status'] = construction_status
            item['construction_years'] = construction_years

            yield item

        next_page_link = response.xpath('.//a[contains(@aria-label,"nextPage") ]/@href').get()
        if next_page_link:
            self.url = next_page_link
        yield scrapy.Request(url=self.url, callback=self.parse, headers=self.get_headers())

    def get_headers(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
            'Accept': 'application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
        }
        return headers
