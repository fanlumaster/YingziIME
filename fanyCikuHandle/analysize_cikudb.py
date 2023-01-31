import sqlite3
import os.path

db_file = os.path.join(os.path.dirname(__file__), '../fanyCiku/ciku_demo.db')

db = sqlite3.connect(db_file)

cursor = db.cursor()

'''
# 获取所有表的名称
cursor.execute("select name from sqlite_master where type='table'")
tables = cursor.fetchall()
# print(tables)
'''
'''~output
[('xiaohe',), ('wubi86',), ('symbol',), ('wubi98',), ('English',), ('pinyin',), ('郑码',), ('现代五笔',), ('形意检字法',), ('仓颉五代',)]
'''

'''
# 获取表中的列名
cursor.execute("select * from pinyin")
col_name_list = [tup[0] for tup in cursor.description]
print(col_name_list)
#~output ['jp', 'key', 'value', 'weight']
'''

'''
# 获取前五个数据
# count = 0
# for row in cursor:
#     print(row)
#     count += 1
#     if (count == 5):
#         break

# 获取前八个数据
print(cursor.fetchall()[:8])
'''

'''
# 获取表中数据的总个数
cursor.execute("select count(*) from pinyin")
print(cursor.fetchone()[0]) # 此时表中其实只有一个数据
'''

cursor.execute("select * from pinyin")
for each in cursor.fetchall()[-8:]:
    print(each)
# 插入一条数据
# ['jp', 'key', 'value', 'weight']
cursor.execute(
    '''insert into pinyin (jp, key, value, weight) values ("x'h's", "xiao'hong'shu", '小红书', 60000)''')
db.commit()

# 关闭数据库连接
db.close()
