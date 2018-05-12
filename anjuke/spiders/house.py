# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from anjuke.itemloader import AnjukeItemLoader
from anjuke.items import AnjukeItem
import re


class HouseSpider(CrawlSpider):
    name = 'house'
    allowed_domains = ['wh.fang.anjuke.com']
    start_urls = ['https://wh.fang.anjuke.com/loupan/?from=navigation']

    rules = (
        Rule(LinkExtractor(allow=r'/loupan/\d+\.html'), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[contains(@class, "pagination")]//a[contains(., "下一页")]')),
    )

    def parse_item(self, response):
        itemloader = AnjukeItemLoader(item=AnjukeItem(), response=response)
        itemloader.add_xpath('title', '//div[@class="lp-tit"]/h1/text()')
        itemloader.add_xpath('price', '//dd[contains(@class, "price")]/p/em')
        itemloader.add_xpath('around_price', '//dd[@class="around-price"]/span/text()')
        itemloader.add_xpath('house_type', '//dd[@class="ajust"]/div[@class="house-item"]/a/text()')
        itemloader.add_xpath('address', '//span[@class="lpAddr-text"]/text()')
        itemloader.add_xpath('phone', '//div[contains(@class, "tel-box")]/p/strong/text()')
        itemloader.add_xpath('opentime', '//p[contains(@class, "info-new")]', re='<label>最新开盘</label>\s+(.*)<a.*')
        itemloader.add_xpath('completetime', '//p[contains(@class, "info-new")]', re='<label>交房时间</label>\s+(.*)</p>.*')
        itemloader.add_value('url', response.url)
        # pattern = re.compile(r'.*m.anjuke.com.*')
        # if not len(pattern.findall(response.url)) > 0:
        yield itemloader.load_item()