# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import  json

class EvanappstorePipeline(object):
    def __init__(self):
        self.file=open('appstore.json','wb')
    def process_item(self, item, spider):
        # val="{\n"+\
        #     "{0},\n{1},\n{2},\n{3},\n{4}\n".\
        #     format('"appid":"'+item['appid']+'"',\
        #            '"title":"'+item['title']+'"',\
        #            '"intro":"'+item['intro']+'"',\
        #            '"img":"'+item['img']+'"',\
        #            '"recommend":['+item['recommend']+']')\
        #     +"}\n"
        val={'appid':item['appid'],'title':item['title'],'title':item['title'],'intro':item['intro'],'img':item['img'],'recommend':item['recommend']}
        val=json.dumps(val)
        self.file.write(val)
        return item
