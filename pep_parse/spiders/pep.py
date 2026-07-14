import re

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import DOMAIN_PEP, NAME_SPIDER_PEP


class PepSpider(scrapy.Spider):
    name = NAME_SPIDER_PEP
    allowed_domains = [DOMAIN_PEP]
    start_urls = [f'https://{d}/' for d in allowed_domains]

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
