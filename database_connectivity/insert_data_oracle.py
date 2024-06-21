import cx_Oracle
# Inserting a record into a table in Oracle database
try:
    con = cx_Oracle.connect('system/tiger@localhost:1521/xe')
    cursor = con.cursor()
     
    #con.autocommit = True
    # Inserting a record into table employee
    cursor.execute('insert into employee values(121,\'Rahul\',50000.50)')
 
    # commit() to make changes reflect in the database
    con.commit()
    print('Record inserted successfully')
 
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)
 
# by writing finally if any error occurs
# then also we can close the all database operation
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()


