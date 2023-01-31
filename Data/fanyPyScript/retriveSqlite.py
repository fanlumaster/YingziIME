'''
取出所有的数据，然后放入 ciku.txt 文件中。

('table', 'pinyin', 'pinyin', 10, 'CREATE TABLE "pinyin" ("jp" TEXT,"key" TEXT,"value" TEXT,"weight" INTEGER DEFAULT 0)')
('table', 'wubi86', 'wubi86', 7, 'CREATE TABLE "wubi86" ("key" TEXT,"value" TEXT,"weight" INTEGER DEFAULT 0)')
('table', 'wubi98', 'wubi98', 9, 'CREATE TABLE "wubi98" ("key" TEXT,"value" TEXT,"weight" INTEGER DEFAULT 0)')
('table', 'xiaohe', 'xiaohe', 6, 'CREATE TABLE "xiaohe" ("key" TEXT,"value" TEXT,"weight" INTEGER DEFAULT 0)')
('table', '仓颉五代', '仓颉五代', 8, 'CREATE TABLE \'仓颉五代\' ("key" TEXT,"value" TEXT,"weight" INTEGER DEFAULT 5000)')
('table', '形意检字法', '形意检字法', 3, 'CREATE TABLE "形意检字法" (\n\t"key"\tTEXT,\n\t"value"\tTEXT,\n\t"weight"\tINTEGER\n)')
'table', '现代五笔', '现代五笔', 4, 'CREATE TABLE "现代五笔" (\n\t"key"\tTEXT,\n\t"value"\tTEXT,\n\t"weight"\tINTEGER\n)')
('table', '郑码', '郑码', 5, 'CREATE TABLE "郑码" (\n\t"key"\tTEXT,\n\t"value"\tTEXT,\n\t"weight"\tINTEGER\n)')
'''

import os.path
import sqlite3


db_file_path = os.path.join(os.path.dirname(__file__), '../ciku.db')

conn = sqlite3.connect(db_file_path)
print('opening db success!')

c = conn.cursor()

# 获取数据库中所有的表的名称
# cursor = c.execute('''select * from sqlite_master where type='table' order by name;
cursor = c.execute('''select * from pinyin;
''')

write_path = os.path.join(os.path.dirname(__file__), './ciku.txt')

with open(write_path, 'ab+') as myfile:
    # 先清空文件中的内容
    myfile.truncate(0)
    for row in cursor:
        cur_line = str(row) + '\n'
        res_content = cur_line.encode()
        myfile.write(res_content)
conn.close()
