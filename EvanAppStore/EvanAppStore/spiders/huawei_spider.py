import scrapy
import re
from scrapy.selector import Selector
from EvanAppStore.items import EvanappstoreItem

class HuaweiSpider(scrapy.Spider):
    name = 'huawei_appstore'
    allowed_domains=["huawei.com"]
    start_urls=[]
    for i in range(1,2):
        start_urls.append('http://appstore.huawei.com/more/all/'+str(i))

    def parse(self, response):
        page=Selector(response)
        divs=page.xpath('//div[@class="game-info  whole"]')
        urls=[]
        for div in divs:
            yield scrapy.Request(div.xpath('.//h4[@class="title"]/a/@href').extract_first(),callback=self.parse_url)



    def parse_url(self, response):
        page=Selector(response)
        item=EvanappstoreItem()

        item['title']=page.xpath('//ul[@class="app-info-ul nofloat"]/li/p/span[@class="title"]/text()').extract_first().encode('utf-8')
        item['url']=response.url
        appid=item['url'].split('/')[-1]
        item['appid']=appid
        item['intro']=page.xpath('//meta[@name="description"]/@content').extract_first().encode('utf-8')

        divs=page.xpath('//div[@class="open-info"]')
        recommend=""
        for div in divs:
            url=div.xpath('./p[@class="name"]/a/@href').extract_first()
            appid=item['url'].split('/')[-1]
            name=div.xpath('./p[@class="name"]/a/text()').extract_first().encode('utf-8')
            recommend+="{0}:{1}; ".format(appid,name)
        item['recommend']=recommend


        yield item
