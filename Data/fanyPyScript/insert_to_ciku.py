import sqlite3
import os.path


db_file = os.path.join(os.path.dirname(__file__), '../ciku.db')
conn = sqlite3.connect(db_file)
print('opening db success!')

c = conn.cursor()

c.execute("insert into pinyin () ")
