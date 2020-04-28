"""
This file containing scarping for the quotes.toscrape website using scrapy also pagination
scraping and successfully saved data in database, code for saving is present in pipelines.py.
Author: Rutuja Tikhile.
Data:19/4/2020
"""
import scrapy
from ..items import ScrapingWebItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = [
        # 'http://quotes.toscrape.com/'
        'http://quotes.toscrape.com/page/1/'
    ]
    # def parse(self, response):
    #     title = response.css('title::text').extract()  # ::text because we want only title text
    #     yield {'titletext': title}

    def parse(self, response):

        items = ScrapingWebItem()

        all_div_quotes = response.css("div.quote")

        for quotes in all_div_quotes:  # it gives one by one title+author+tag

            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items ['title'] = title
            items ['author'] = author
            items ['tag'] = tag

            yield items

            next_page = response.css('li.next a::attr(href)').get()
            next_page = 'http://quotes.toscrape.com/page/2/' + str(QuoteSpider.page_number) + '/'
            if QuoteSpider.page_number < 11:
                QuoteSpider.page_number += 1
                yield response.follow(next_page, callback=self.parse())


