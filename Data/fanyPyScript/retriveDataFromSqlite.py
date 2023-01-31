import os.path
import sqlite3


db_file_path = os.path.join(os.path.dirname(__file__), '../ciku.db')

conn = sqlite3.connect(db_file_path)
print('opening db success!')

c = conn.cursor()

c.execute('''select * from pinyin;
''')
col_name_list = [tuple[0] for tuple in c.description]
print(col_name_list)

conn.close()
