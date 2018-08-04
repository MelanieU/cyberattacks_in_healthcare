from scrapy import Item, Field

class GlassdoorItem(Item):
	title = Field()
	size =Field()
	company = Field()
	industry = Field()
	revenue = Field()

	