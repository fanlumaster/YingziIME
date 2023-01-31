'''
转换词库格式

转换示例：

左左右右	zuo zuo you you	1215
->
["z'z'y'y", "zuo'zuo'you'you", '左左右右', 60000+1215]
'''
import os.path
import sqlite3

sogoutxt_path = os.path.join(os.path.dirname(__file__), './sogou.txt')

# db_file = os.path.join(os.path.dirname(__file__), '../fanyCiku/ciku_demo.db')
db_file = os.path.join(os.path.dirname(__file__), '../Data/ciku.db')

db = sqlite3.connect(db_file)

cursor = db.cursor()

with open(sogoutxt_path, 'rb+') as file:
    all_lines = file.readlines()
    # for line in all_lines[-10:]:
    count = 0
    for line in all_lines:
        cur_line = line.decode().rstrip()
        cur_line_list = cur_line.split('\t')
        col_1_prev = cur_line_list[1].split(' ')
        col_1 = []
        for each in col_1_prev:
            col_1.append(each[0])
        col_1 = "'".join(col_1)
        col_2 = "'".join(col_1_prev)
        col_3 = cur_line_list[0]
        col_4 = int(cur_line_list[2]) + 60000
        # print(cur_line, end='')
        # print(cur_line_list)
        # print(col_1)
        # print(col_2)
        # print(col_3)
        # print(col_4)

        # 插入数据
        cursor.execute(
            '''insert into pinyin (jp, key, value, weight) values (?,?,?,?)''', [col_1, col_2, col_3, col_4])
        count += 1
        print('插入第 ' + str(count) + ' 条数据')

db.commit()
db.close()
