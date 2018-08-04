
BOT_NAME = 'hackmageddon'

SPIDER_MODULES = ['hackmageddon.spiders']
NEWSPIDER_MODULE = 'hackmageddon.spiders'


DOWNLOAD_DELAY = 3
ITEM_PIPELINES = {'hackmageddon.pipelines.WriteItemPipeline': 100, }

ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 1