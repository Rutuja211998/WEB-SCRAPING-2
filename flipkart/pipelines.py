# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector


class FlipkartPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='flipkart'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        # self.curr.execute("""DROP TABLE IF EXISTS """)
        self.curr.execute(""" create table mobiles(
                             model text,
                             price text,
                             ratings text,
                             specifications text
                             )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute(""" insert into mobiles values (%s,%s,%s,%s)""", (

            item['model'],
            item['price'],
            item['ratings'],
            item['specifications']

        ))
        self.conn.commit()

