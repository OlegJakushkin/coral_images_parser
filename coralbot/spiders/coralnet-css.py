# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from coralbot.items import ImageItem
import time

class CoralnetCSSSpider(scrapy.Spider):
    name = "coralnet-css"
    start_urls = [
        'https://coralnet.ucsd.edu/label/list/',
    ]

    def parse(self, response):
        for coral, popularity, animal_type ,Duplicatecheck in zip(response.css('table tr[data-label-id] a::attr(href)').extract(),
                                                  response.css('table tr[data-label-id] td > div.meter::attr(title)').extract(),
                                                  response.css('table tr[data-label-id] td::text').extract()[::2],
                                                  response.css('table tr[data-label-id] td img::attr(alt)')):
            if int(popularity[:-1]) > 50 and animal_type == 'Other Invertebrates' and Duplicatecheck != 'Duplicate' :
                yield SplashRequest(response.urljoin(coral), self.parse_images, args={'wait': 20, 'html': 1,
                                                                                      'render_all': 1})

    def parse_names(self,response):
        yield {'name':response.css('div#content-container h1::text').extract_first()}

    def parse_images(self, response):
        folder_name = response.css('div#content-container h1::text').extract_first()
        for image in response.css("div#patches-container span"):
            img_url = image.css("span > img::attr(src)").extract_first()
            yield ImageItem(image_urls=[img_url], folder_name=folder_name)

