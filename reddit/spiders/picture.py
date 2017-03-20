# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from reddit.items import RedditItem

class PictureSpider(CrawlSpider):
    name = "picture"
    allowed_domains = ["www.reddit.com"]
    start_urls = ['http://www.reddit.com/']

    # https://www.reddit.com/r/pics/?count=25&after=t3_58psse
    # https://www.reddit.com/r/pics/?count=50&after=t3_58owsr

    rules = [

    	Rule(LinkExtractor(allow=[r'/?count=\d+&after=\w*']),
    		callback='parse_item',
    		follow = True)

    ]


   	# div with class = thing
   	# //*[@id="thing_t3_5822z3"]/div[2]/p[1]/a

    def parse_item(self, response):

    	divs = response.css('div.thing')

    	for div in divs:

    		item = RedditItem()

    		item['title'] = div.xpath('div[2]/p[1]/a/text()').extract()
    		item['img_link'] = div.xpath('div[2]/p[1]/a/@href').extract()

    		yield item
    		
    		# title = div.xpath('div[2]/p[1]/a/text()').extract()
    		# img_link = div.xpath('div[2]/p[1]/a/@href').extract()

    		# print title
    		# print img_link