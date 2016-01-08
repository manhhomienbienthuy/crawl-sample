# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from stack.items import StackItem


class StackSpider(CrawlSpider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]

    rules = (
        Rule(LinkExtractor(allow=r"questions\?page=[0-5]&sort=newest"),
             callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        questions = response.xpath('//div[@class="summary"]/h3')

        for question in questions:
            question_location = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            full_url = response.urljoin(question_location)
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        item = StackItem()
        item["title"] = response.css(
            "#question-header h1 a::text").extract()[0]
        item["url"] = response.url
        item["content"] = response.css(
            ".question .post-text").extract()[0]
        yield item
