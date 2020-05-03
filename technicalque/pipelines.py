# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector


class TechnicalquePipeline(object):

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
        self.curr.execute(""" create table ques_tb(
                            pythonque text,
                            javaque text,
                            nodejsque text
                             )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute(""" insert into ques_tb values (%s,%s,%s)""", (
           item['pythonque'],
           item['javaque'],
           item['nodejsque']
        ))
        self.conn.commit()


 # item['java1'],
 #            item['java2'],item['java3'],item['java4'],item['java5'],item['java6'],item['java7'],item['java8'],item['java9'],item['java10'],
 #            item['py1'],item['py2'],item['py3'],item['py4'],item['py5'],item['py6'],item['py7'],item['py8'],item['py9'],item['py10']
# java1
# text,
# java2
# text,
# java3
# text,
# java4
# text,
# java5
# text,
# java6
# text,
# java7
# text,
# java8
# text,
# java9
# text,
# java10
# text,
# py1
# text,
# py2
# text,
# py3
# text,
# py4
# text,
# py5
# text,
# py6
# text,
# py7
# text,
# py8
# text,
# py9
# text,
# py10
# text