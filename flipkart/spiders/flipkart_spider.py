import scrapy
from ..items import FlipkartItem


class FlipkartSpider(scrapy.Spider):
    name = "mobile"
    allowed_domains = ['www.flipkart.com']

    def __init__(self):
        self.url = "https://www.flipkart.com/mobiles/pr?filterNone=true&sid=tyy%2C4io&p%5B%5D=sort%3Dpopularity&p%5B%5D=facets.brand%255B%255D%3DApple&otracker=clp_metro_expandable_5_5.metroExpandable.METRO_EXPANDABLE_mobile-phones-store_0244AFBL8QS6_wp4&fm=neo%2Fmerchandising&iid=M_89a56dc9-ca57-46d1-b8f4-d253c89d67a0_5.0244AFBL8QS6&ssid=wsv0vkzsts0000001588241002793"

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse, headers=self.get_headers())

    def parse(self, response):
        wrapper = response.xpath('//div[@class="_1UoZlX"]/a')
        for search in wrapper:
            model = search.xpath('.//div[@class="_3wU53n"]/text()').get()
            ratings = search.xpath('.//div[@class="niH0FQ"]/span/div/text()').get()
            specifications = search.xpath('.//div[@class="_3ULzGw"]/ul/li/text()').extract()
            specifications = "".join(specifications)
            price = search.xpath('.//div[@class="_1vC4OE _2rQ-NK"]/text()').get()
            # image_urls = 'https:' + search.xpath('//div[@class="_3SQWE6"]/div/div/div/img/@src').get()
            # image_urls = 'https://rukminim1.flixcart.com/image/416/416/k2jbyq80pkrrdj/mobile-refurbished/y/k/z/iphone-11-64-a-mwlx2hn-a-apple-0-original-imafkg24ymsjav9h.jpeg?q=70'
            # image_urls = search.xpath('//*[@id="container"]/div/div[3]/div[2]/div/div[2]/div[5]/div/div/div/a/div[1]/div[1]/div[1]/div/img').get()
            # image_urlsss = 'https//'.join(image_urls)
            # ('//div[@class="_3BTv9X"]//img[@class="_1Nyybr  _30XEf0"]/@src')
            # print(image_urls)

            items = FlipkartItem()
            items['model'] = model
            items['ratings'] = ratings
            items['specifications'] = specifications
            items['price'] = price
            # items['image_urls'] = image_urls
            yield items

    def get_headers(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
            'Accept': 'application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
        }
        return headers