import scrapy
from ..items import EcommerceItem

class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    page_num = 2
    start_urls = [
        'https://meesho.com/topwear-men/pl/zcm6l?page=1',
        "https://meesho.com/inner-sleepwear-men/pl/2qdtt?page=1",
        "https://meesho.com/track-pants-men/pl/k7nrc?page=1"
    ]

    def parse(self, response):
        items = EcommerceItem()

        name = response.css(".cQhePS::text").getall()
        price = response.css(".hiHdyy::text").getall()
        offer = response.css(".lnonyH::text").getall()
        delivery = response.css(".ezFwfg::text").getall()
        ratings = response.css('.gYxLUd , .kLWVnF , .fpunvK').css("::text").getall()

        items['name'] = name
        items['price'] = price
        items['offer'] = offer
        items['ratings'] = ratings
        #print(items)
        yield(items)

        EcommerceSpider.page_num += 1
        next_Toppage ="https://meesho.com/topwear-men/pl/zcm6l?page=" + str(EcommerceSpider.page_num)
        next_Innerpage = "https://meesho.com/inner-sleepwear-men/pl/2qdtt?page=" + str(EcommerceSpider.page_num)
        next_Trackpage = "https://meesho.com/track-pants-men/pl/k7nrc?page=" + str(EcommerceSpider.page_num)
        if EcommerceSpider.page_num <= 250:
            yield response.follow(next_Toppage,callback=self.parse)
            yield response.follow(next_Innerpage, callback=self.parse)
            yield response.follow(next_Trackpage, callback=self.parse)