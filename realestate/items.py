# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RealestateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
    property_location = scrapy.Field()
    price = scrapy.Field()
    per_sqr_ft = scrapy.Field()
    area = scrapy.Field()
    construction_status = scrapy.Field()
    construction_years = scrapy.Field()

    # specification = scrapy.Field()
    # title = scrapy.Field()
    # address = scrapy.Field()
    # description = scrapy.Field()
    # posted_on = scrapy.Field()
    # price = scrapy.Field()



