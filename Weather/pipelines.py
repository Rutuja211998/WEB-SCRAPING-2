# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector


class WeatherPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='weather'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" create table weather_tb(
                             day text,
                             details text
                             )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute(""" insert into weather_tb values (%s,%s)""", (
            item['day'],
            item['details']
        ))
        self.conn.commit()