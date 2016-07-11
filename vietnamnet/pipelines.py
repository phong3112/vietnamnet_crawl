# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json

class VietnamnetPipeline(object):
    def __init__(self):
        self.content = codecs.open("text", "w", "utf-8")

    def process_item(self, item, spider):
        if not item:
            return

        if item["content"]:
            self.content.write(" ".join(item["content"]).replace("\n", " ") + "\n")

        return item

#class VietnamnetPipeline(object):
#    def process_item(self, item, spider):
#        return item

#    def __init__(self):
#        self.file = open('items.jl', 'wb')

#    def process_item(self, item, spider):
#	split_item = item.split(',')
#        line = json.dumps(dict(item)) + "\n\n"
#        self.file.write(line)
#        return item

