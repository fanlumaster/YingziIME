import os.path
import sqlite3


db_file_path = os.path.join(os.path.dirname(__file__), '../ciku.db')

conn = sqlite3.connect(db_file_path)
print('opening db success!')

c = conn.cursor()

# 获取数据库中所有的表的名称
# cursor = c.execute('''select * from sqlite_master where type='table' order by name;
c.execute('''select * from pinyin;
''')

max_value = 0

for row in c:
    # print(row[3])
    if (row[3] > max_value):
        max_value = row[3]

print(max_value)
conn.close()
