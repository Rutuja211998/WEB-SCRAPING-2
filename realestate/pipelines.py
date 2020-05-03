# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import mysql.connector


class RealestatePipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='findhome'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        # self.curr.execute("""DROP TABLE IF EXISTS property""")
        self.curr.execute(""" create table properties(
                             title text,
                             property_location text,
                             price text,
                             per_sqr_ft text,
                             area text,
                             construction_status text,
                             construction_years text
                             )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute(""" insert into properties values (%s,%s,%s,%s,%s,%s,%s)""", (

            item['title'],
            item['property_location'],
            item['price'],
            item['per_sqr_ft'],
            item['area'],
            item['construction_status'],
            item['construction_years']

        ))
        self.conn.commit()



