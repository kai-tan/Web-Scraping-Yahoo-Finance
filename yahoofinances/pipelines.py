# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
# import pymongo

# class MongodbPipeline(object):
#     collection_name = "stocks_data"
    
#     def open_spider(self, spider):
#         self.client = pymongo.MongoClient("mongodb+srv://kai:g0073297x@cluster0-uaxcp.mongodb.net/test?retryWrites=true&w=majority")
#         self.db = self.client["yahoo_finances"]

#     def close_spider(self, spider):
#         self.client.close()

#     def process_item(self, item, spider):
#         self.db[self.collection_name].insert(item)
#         return item



from pymongo import MongoClient


# class MongodbPipeline(object):
#     collection = "stocks_data"

#     def __init__(self, mongo_uri, mongo_db):
#         self.mongo_uri= mongo_uri
#         self.mongo_db= mongo_db
    
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             mongo_uri=crawler.settings.get('MONGO_URI'),
#             mongo_db= crawler.settings.get('MONGO_DB')
#         )
    
#     def open_spider(self, spider):
#         self.client= MongoClient(self.mongo_uri)
#         self.db= self.client[self.mongo_db]
    
#     def close_spider(self, spider):
#         self.client.close()
    
#     def process_item(self, item, spider):
#         self.db[self.collection].insert_one(dict(item))
#         return item


class YahooFinancesPipeline(object):
    def process_item(self, item, spider):
        return item