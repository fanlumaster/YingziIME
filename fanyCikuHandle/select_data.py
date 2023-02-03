import sqlite3
import os.path

db_file = os.path.join(os.path.dirname(__file__), '../Data/ciku.db')

db = sqlite3.connect(db_file)
cursor = db.cursor()

cursor.execute("select * from pinyin")

# 打印最后 n 个数据
n = 1000
for each in cursor.fetchall()[-n:]:
    print(each)

# 找出词库中有 # 的词语
# for each in cursor.fetchall():
#     if (each[2][0] == '#'):
#         print(each)

# 关闭数据库连接
db.close()
