# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import hashlib
from scrapy.utils.python import to_bytes


class StoreImgPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        if item is not None:
            folder_name = item['folder_name']
            return f'{folder_name}/{image_guid}.jpg'
        return f'{image_guid}.jpg'
