import scrapy


class EstateSpider(scrapy.Spider):
    name = "estate"
    allowed_domains = ["indomio.me"]
    start_urls = ["https://indomio.me"]

    def parse(self, response):
        pass
