import sqlite3

print(sqlite3.sqlite_version)

conn = sqlite3.connect('school.db')

cur = conn.cursor()

cur.execute('select * from student')

 