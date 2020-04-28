# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# Scraped data -> Item Container -> Json/csv files
# Scraped data -> Item Container -> Pipeline -> SQL/ database
# import sqlite3
import mysql.connector


class ScrapingWebPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        # self.conn = sqlite3.connect("myquote_db")
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='myquotes'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS scrapyquote_tb""")  # because we create one same
        self.curr.execute(""" create table scrapyquote_tb(
                             title text,
                             author text,
                             tag text
                             )""")

    def process_item(self, item, spider):
        self.store_db(item)
        # print("Pipeline :" + item['title'][0])  # this should printout quote
        # if we did'nt add [0] it gives typeerror: must be str not list, so [0] will contain string
        # if we don't write [0] its returns a kind of a dict
        return item

    def store_db(self, item):
        self.curr.execute(""" insert into scrapyquote_tb values (%s,%s,%s)""",(
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.conn.commit()