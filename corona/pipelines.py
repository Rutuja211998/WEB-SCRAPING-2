# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector


class CoronaPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='Covid19'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" create table cases(
                             coronavirus text,
                             deaths text,
                             recovred text,
                             countries text
                             )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute(""" insert into cases values (%s,%s,%s,%s)""", (

            item['coronavirus_cases'],
            item['deaths_cases'],
            item['recovred_cases'],
            item['countries']
        ))
        self.conn.commit()

