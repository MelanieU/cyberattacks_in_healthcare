
BOT_NAME = 'glassdoor'

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36"

SPIDER_MODULES = ['glassdoor.spiders']
NEWSPIDER_MODULE = 'glassdoor.spiders'


DOWNLOAD_DELAY = 3
ITEM_PIPELINES = {'glassdoor.pipelines.WriteItemPipeline': 100, }

ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 1