import cx_Oracle

try:
    conn = cx_Oracle.connect('system/tiger@localhost:1521/xe')
except cx_Oracle.DatabaseError as er:
    print("There is error in the datanbase: " , er)
else:
    try:
        cur = conn.cursor()
        cur.execute('select * from employee where salary > :sal', {'sal': 50000})
        rows = cur.fetchall()
        print(rows)
    except cx_Oracle.DatabaseError as er:
        print('There is error in the Oracle database:', er)
    except Exception as er:
        print('Error: ', er)
    finally:
        if cur:
            cur.close()
finally:
    if conn:
        conn.close()