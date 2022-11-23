import sqlite3
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuotetutorialPipeline(object):
    conn = sqlite3.connect('quotes.db')
    curr = conn.cursor()

    def __int__(self):
        self.create_connection()


    def process_item(self, item, spider):
        self.store_items(item)
        return item

    def create_connection(self):
        self.conn = sqlite3.connect('quotes.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute('''
                     DROP TABLE IF EXISTS quotes_tb
                     ''')
        self.curr.execute('''
             CREATE TABLE quotes_tb(
                title text,
                author text,
                tags text
            ) ''')

    def store_items(self, item):
        # self.create_table()
        self.curr.execute('''
        insert into quotes_tb values(?,?,?)
        ''',(
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.conn.commit()
