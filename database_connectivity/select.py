# View result set from a select query using fetchall(), fetchmany(int), fetchone()

import  cx_Oracle

try:
    conn = cx_Oracle.connect('system/tiger@localhost:1521/xe')
except cx_Oracle.DatabaseError as er:
    print('There is an error in the Oracle database:', er)
else:
    try:
        cur = conn.cursor()
        # fetchall() is used to fetch all records from result set
        cur.execute('select * from employee')
        rows = cur.fetchall()
        print(rows)
        # fetchmany(int) is used to fetch limited number of records from result set based on integer argument passed in it
        cur.execute('select * from employee')
        rows = cur.fetchmany(3)
        print(rows)
            # fetchone() is used fetch one record from top of the result set
        cur.execute('select * from employee')
        rows = cur.fetchone()
        print(rows)
    except cx_Oracle.DatabaseError as er:
         print('There is an error in the Oracle database:', er)
    except Exception as er:
        print('Error:'+str(er))
    finally:
        if cur:
            cur.close()
finally:
    if conn:
        conn.close()       
