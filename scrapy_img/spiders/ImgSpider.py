"""
DEMO for saving image with scrapy.
"""
import scrapy
from ..items import ScrapyImgItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    start_urls = ["http://automationpractice.com/index.php?id_product=2&controller=product"]

    def parse(self, response):
        item =  ScrapyImgItem()
        img_urls = []

        for img in response.css("#thumbs_list_frame > li"):
            img_urls.append(img.css("a::attr(href)").extract_first())
        item['image_urls'] = img_urls
        yield item