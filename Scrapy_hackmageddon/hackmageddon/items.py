from scrapy import Item, Field
import re

class HackmageddonItem(Item):
	date = Field()
	author = Field()
	target = Field()
	description = Field()
	url = Field()
	attack = Field()
	target_class = Field()
	attack_class = Field()
	country = Field()