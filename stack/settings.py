# -*- coding: utf-8 -*-

BOT_NAME = 'stack'

SPIDER_MODULES = ['stack.spiders']
NEWSPIDER_MODULE = 'stack.spiders'

ITEM_PIPELINES = ['stack.pipelines.StackPipeline', ]
