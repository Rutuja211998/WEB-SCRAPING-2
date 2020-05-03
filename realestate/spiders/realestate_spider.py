"""
This file containing scarping for the realestate website using scrapy and i am saving scraped data into database
successfully, code for saving is present in the pipelines.py file .
Author: Rutuja Tikhile.
Data: 24/4/2020
"""
import scrapy
from ..items import RealestateItem


class OtherFeatures(scrapy.Spider):
    name = "realsite"

    def start_requests(self):
        url = "https://www.findhome.com/property-for-rent-in-ernakulam/srp"
        yield scrapy.Request(url=url, callback=self.parse, headers=self.get_headers())

    def parse(self, response):
        if not response:
            print("Failed to fetch the page")
            return None

        wrapper = response.xpath('//div[@id="searchListing"]')
        search_result = wrapper.xpath('//div[@class="list-rigt-blk"]')

        for result in search_result:

            specification = result.xpath('.//ul[@class="prop-specification"]/li/text()').extract()
            title = result.xpath('.//div[@class="title-lst"]/h4/text()').extract()
            address = result.xpath('.//span[@class="sprite-bf loct"]/text()').extract()
            description = result.xpath('.//div[@class="col-xs-12 list-descript"]/text()').extract()
            posted_on = result.xpath('.//span[@class="sprite-bf loct postedDt"]/text()').extract()
            price = result.xpath('.//div[@class="prtlst-price"]/span/text()')[1].extract()

            items = RealestateItem()

            items['specification'] = specification
            items['title'] = title
            items['address'] = address
            items['description'] = description
            items['posted_on'] = posted_on
            items['price'] = price

            yield items

    def get_headers(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
            'Accept': 'application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
            }
        return headers


