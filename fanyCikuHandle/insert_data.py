'''
insert data to pinyin.db
'''

import sqlite3
import os.path

# db_file = os.path.join(os.path.dirname(__file__), '../fanyCiku/ciku_demo.db')
db_file = os.path.join(os.path.dirname(__file__), '../Data/ciku.db')

db = sqlite3.connect(db_file)

cursor = db.cursor()

cursor.execute(
    '''insert into pinyin (jp, key, value, weight) values ("x'h's", "xiao'hong'shu", '小红书', 60000)''')
cursor.execute(
    '''insert into pinyin (jp, key, value, weight) values (?,?,?,?)''', ["x'h's", "xiao'hong'shu", '小红书', 60002])
db.commit()

# 关闭数据库连接
db.close()
