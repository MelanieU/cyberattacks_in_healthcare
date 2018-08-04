
from scrapy import Spider, Request #inheritance
from hackmageddon.items import HackmageddonItem #defined in items
import re

class HackmageddonSpider(Spider):
	name = "hackmageddon_spider"
	start_urls = ['https://www.hackmageddon.com/2017-master-table/']
	allowed_urls = ['https://www.hackmageddon.com/']

	def parse(self, response):

		result_urls = ['https://www.hackmageddon.com/{}-master-table/'.format(x) for x in range(2017,2019)]

		for url in result_urls:
			yield Request(url=url, callback=self.parse_result_page)

	def parse_result_page(self, response):
		#rows = response.xpath('//*[@id=matches[@id, "tablepress-2018-Master"]]/tbody/tr')
		rows = response.xpath('//*[starts-with(@id, "tablepress-201")]/tbody/tr')

		print(len(rows))
		print('-'*50)

		for row in rows:

			date = row.xpath('./td[2]/text()').extract_first()
			author = row.xpath('./td[3]/text()').extract_first()
			target = row.xpath('./td[4]/text()').extract_first()
			description = row.xpath('./td[5]/a/text()').extract_first()
			url = row.xpath('./td[5]/a/@href').extract_first()
			attack = row.xpath('./td[6]/text()').extract_first()
			target_class = row.xpath('./td[7]/text()').extract_first()
			attack_class = row.xpath('./td[8]/text()').extract_first()
			country = row.xpath('./td[9]/text()').extract_first()

			item = HackmageddonItem()

			item['date'] = date
			item['author'] = author
			item['target'] = target
			item['description'] = description
			item['url'] = url
			item['attack'] = attack
			item['target_class'] = target_class
			item['attack_class'] = attack_class
			item['country'] = country

			yield(item)