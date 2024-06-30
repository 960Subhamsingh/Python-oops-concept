import sqlite3

# connecting databases 
conn = sqlite3.connect('D:/Project/Python_Tutorial/database_connectivity/school.db')

# create table 
table = "CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), SECTION VARCHAR(255));"

# cursor object method
cur = conn.cursor()

conn.execute(table)


# Queries to INSERT records. 
cur.execute('''INSERT INTO STUDENT VALUES (' site', '9th', 'C')''') 
cur.execute('''INSERT INTO STUDENT VALUES ('Raju', '7th', 'A')''') 
cur.execute('''INSERT INTO STUDENT VALUES ('rita', '9th', 'C')''') 
cur.execute('''INSERT INTO STUDENT VALUES ('Shyam', '8th', 'B')''') 
cur.execute('''INSERT INTO STUDENT VALUES ('Moni', '9th', 'C')''') 

data = cur.execute('select * from STUDENT')

for row in data:
    print(data)

# save the data in student table
conn.commit()
# close the table in student table
conn.close()
