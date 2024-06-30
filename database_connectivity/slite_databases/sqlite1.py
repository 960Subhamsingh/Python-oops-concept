
import sqlite3

conn = sqlite3.connect('D:/Project/Python_Tutorial/database_connectivity/school.db')

# SQL string to Create a database table
# named person.
create_table = '''CREATE TABLE person(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  age INTEGER NOT NULL
                  );'''

conn.execute(create_table)

print(f'total_changes = {conn.total_changes}\n')

insert_data = '''INSERT INTO person(name, age)
                  VALUES ("Yogesh",21),
                  ("Vishal", 22),
                  ("Ajit",22),
                  ("Ashish",21),
                  ("Tanvi", 20);'''

conn.execute(insert_data)

print(f'total_changes = {conn.total_changes}\n')

select_data = 'select * from person'

cursor = conn.execute(select_data)

