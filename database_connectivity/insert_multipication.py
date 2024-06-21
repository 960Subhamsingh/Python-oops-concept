# Inserting multiple records into a table using executemany() method

import cx_Oracle
# Load data from a csv file into Oracle table using executemany

try:
    conn = cx_Oracle.connect('system/tiger@localhost:1521/xe')

except cx_Oracle.DatabaseError as er:
    print('There is an error in Oracle database: ' , er)
else:
    try:
        cur = conn.cursor()
        data = [[10007 , 'subham',48000.0],[10008, 'kumar', 65000.1],[10009, 'singh', 75000.0]]
        cur = conn.cursor()
        # Inserting multiple records into employee table.
        cur.executemany('insert into employee values(:1,:2,:3)', data)
    except cx_Oracle.DatabaseError as er:
        print('There is an error in Oracle database:', er)
    except Exception as er:
        print(er)
    else:
        conn.commit()
        print('Multiple records are inserted successfully')

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()