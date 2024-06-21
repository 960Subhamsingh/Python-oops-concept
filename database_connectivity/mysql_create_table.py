import mysql.connector

conn = mysql.connector.connect(host="localhost", user= "root", password="tiger" , database= "data")
# create a databaes connection
# conn = mysql.connector.connect(host="localhost", user= "root", password="tiger", database= "data1")
if(conn.is_connected):
    print("Connected")

cur = conn.cursor()

try:
    # list of all the database in mysql databases
    dbs = cur.execute("show databases")
    #creating a new database  
    # dbs = cur.execute("create database data1")
    # create a table in data1 databases
    dbs = cur.execute("create table Employee(name varchar(20) not null, id int(20) not null primary key, salary float not null, Dept_id int not null)")  
    #adding a column branch name to the table Employee  
    cur.execute("alter table Employee add branch_name varchar(20) not null")  

except:
    conn.rollback()
for x in cur:
    print(x)
conn.close()
