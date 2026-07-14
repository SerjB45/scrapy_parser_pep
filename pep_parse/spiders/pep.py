import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        links = response.xpath(
            '//*[@id="index-by-category"]//tr//td//a/@href'
        ).getall()
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.xpath('//*[@class="page-title"]//text()').get()
        docs_info = re.search(r'PEP\s+(\d+)\s*–\s*(.+)', title)
        status = response.xpath(
            '//dt[contains(.,"Status")]/following-sibling::dd//text()'
        ).get()
        yield PepParseItem(
            {
                'number': docs_info.group(1),
                'name': docs_info.group(2),
                'status': status
            }
        )
